#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import requests
from urllib.parse import urljoin

# Direktori
BIN_DIR = "/usr/local/bin"
ICON_DIR = "/usr/share/icons/hicolor"
DESKTOP_DIR = "/usr/share/applications"

def errMsg():
    print("PENGUNAAN:")
    print("Untuk menginstal:")
    print("sudo python3 betmenb0x.py install")
    print("Untuk menghapus:")
    print("sudo python3 betmenb0x.py remove")
    sys.exit(1)

def command_exists(command):
    try:
        subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def depInst():
    print("Memeriksa dependensi...", end="")
    if command_exists("wine") and command_exists("wget") and command_exists("curl"):
        print("SELESAI")
        return

    print("Beberapa dependensi tidak tersedia. Menginstal wine dan dependensi...")
    distribution = subprocess.check_output(['sed', '-n', 's/^ID=//p', '/etc/os-release']).decode().strip()
    try:
        if distribution in ['fedora', 'rhel', 'centos', 'ign']:
            subprocess.run(['dnf', '-q', '-y', 'install', 'wine', 'wget', 'curl'], check=True)
        elif distribution in ['ubuntu', 'debian', 'elementary', 'zorin', 'linuxmint', 'kali', 'neon', 'pop', 'deepin']:
            subprocess.run(['apt-get', '-q', '-y', 'update'], check=True)
            version_id = subprocess.check_output(['grep', '^VERSION_ID=', '/etc/os-release']).decode().strip().split('=')[1].strip('"')
            if int(version_id.split('.')[0]) >= 18:
                wine_pkg = "wine-stable"
            else:
                wine_pkg = "wine"
            subprocess.run(['apt-get', '-q', '-y', 'install', wine_pkg, 'wget', 'curl'], check=True)
        elif distribution == 'arch':
            subprocess.run(['sed', '-i', '/\[multilib\]/,/Include/'"s/^#//"'/etc/pacman.conf'], check=True)
            subprocess.run(['pacman', '-Sy', '--noconfirm'], check=True)
            subprocess.run(['pacman', '-Sq', '--noconfirm', 'wine', 'wget', 'curl'], check=True)
        else:
            print("GAGAL: Distribusi tidak didukung")
            sys.exit(1)
        print("SELESAI")
    except subprocess.CalledProcessError:
        print("GAGAL: Instalasi dependensi gagal")
        sys.exit(1)

def wbDl():
    if os.path.isfile("winbox.exe"):
        print("Menggunakan winbox.exe yang telah diunduh sebelumnya")
        return

    print("Mengunduh Winbox...", end="")
    url_base = "https://mt.lv/"
    url = urljoin(url_base, "winbox")
    if "x86_64" in os.uname().machine:
        url += "64"

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open("winbox.exe", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("SELESAI")
    else:
        print("GAGAL: Unduhan gagal")
        sys.exit(1)

def filesCp():
    print("Menyalin file...", end="")
    os.makedirs(BIN_DIR, exist_ok=True)
    os.makedirs(DESKTOP_DIR, exist_ok=True)

    shutil.copy2("winbox.exe", BIN_DIR)
    shutil.copy2("winbox.sh", BIN_DIR)
    os.chmod(os.path.join(BIN_DIR, "winbox.sh"), 0o755)
    os.chmod(os.path.join(BIN_DIR, "winbox.exe"), 0o755)

    icon_files = [f for f in os.listdir("icons") if f.startswith("winbox-") and f.endswith(".png")]
    for icon_file in icon_files:
        size = icon_file.split("-")[1].split(".")[0]
        icon_path = os.path.join(ICON_DIR, f"{size}x{size}", "apps")
        os.makedirs(icon_path, exist_ok=True)
        shutil.copy2(os.path.join("icons", icon_file), os.path.join(icon_path, "winbox.png"))

    print("SELESAI")

def lncCrt():
    print("Membuat peluncur aplikasi...", end="")
    desktop_entry = f"""[Desktop Entry]
Name=Winbox
GenericName=Alat konfigurasi untuk RouterOS
Comment=Alat konfigurasi untuk RouterOS
Exec={BIN_DIR}/winbox.sh
Icon=winbox
Terminal=false
Type=Application
StartupNotify=true
StartupWMClass=winbox.exe
Categories=Network;RemoteAccess;
Keywords=winbox;mikrotik;
"""

    with open(os.path.join(DESKTOP_DIR, "winbox.desktop"), "w") as f:
        f.write(desktop_entry)

    subprocess.run(['xdg-desktop-menu', 'forceupdate', '--mode', 'system'], check=True)
    print("SELESAI")

def filesRm():
    print("Menghapus peluncur...", end="")
    for root, _, files in os.walk(DESKTOP_DIR):
        for file in files:
            if file == "winbox.desktop":
                os.remove(os.path.join(root, file))
    print("SELESAI")

    print("Menghapus ikon...", end="")
    for root, dirs, _ in os.walk(ICON_DIR):
        for dir in dirs:
            icon_path = os.path.join(root, dir, "apps", "winbox.png")
            if os.path.isfile(icon_path):
                os.remove(icon_path)
    print("SELESAI")

    print("Menghapus file...", end="")
    os.remove(os.path.join(BIN_DIR, "winbox.exe"))
    os.remove(os.path.join(BIN_DIR, "winbox.sh"))
    print("SELESAI")

def main():
    if len(sys.argv) != 2:
        errMsg()

    action = sys.argv[1]
    if action == 'install':
        if not command_exists("wine"):
            depInst()
        wbDl()
        filesCp()
        lncCrt()
    elif action == 'remove':
        filesRm()
    else:
        errMsg()

if __name__ == "__main__":
    main()
