#!/bin/bash

# Cek apakah Wine terinstal
if ! command -v wine &> /dev/null; then
    echo "Wine tidak terinstal. Silakan instal Wine terlebih dahulu."
    exit 1
fi

# Jalankan Winbox menggunakan Wine
WINEPREFIX="$HOME/.wine_winbox" wine /usr/local/bin/winbox.exe

