#!/bin/bash

echo "=========================================="
echo "    sMb Scanner Auto-Installer (Termux)   "
echo "=========================================="

echo "[*] Updating Termux packages..."
pkg update -y && pkg upgrade -y

echo "[*] Installing required packages (python, wget, unzip)..."
pkg install python wget unzip -y

echo "[*] Installing Python requests module..."
pip install requests

echo "[*] Downloading Xray Core for Android (arm64)..."
wget -q --show-progress https://github.com/XTLS/Xray-core/releases/download/v1.8.4/Xray-linux-arm64-v8a.zip -O xray.zip

echo "[*] Extracting Xray..."
unzip -o xray.zip xray
rm xray.zip

echo "[*] Setting executable permissions..."
chmod +x xray

echo "=========================================="
echo "✅ Installation Complete!"
echo "🚀 To run the scanner, type: python scanner.py"
echo "=========================================="