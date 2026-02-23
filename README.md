# 💎 sMb Scanner (Anti-DPI V2ray Engine)

![Version](https://img.shields.io/badge/Version-1.0-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Termux-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

> **🌍 Choose your language / زبان خود را انتخاب کنید:**
> * [🇺🇸 English Documentation](#-english-documentation)
> * [🇮🇷 راهنمای فارسی](#-راهنمای-فارسی)

---

## 🇺🇸 English Documentation

**sMb Scanner** is an advanced, multi-threaded Anti-DPI V2ray IP Scanner designed specifically for Android (via Termux). It actively tests Cloudflare, Gcore, Fastly, and custom IPs using real-world downloading stress tests to find the best **"Diamond IPs"** that bypass strict DPI (Deep Packet Inspection) filters.

### 🚀 Key Features
* **Real Stress Testing:** Instead of simple and fake pings, it downloads real files via the Xray core to filter out "Zombie IPs" that drop under heavy load.
* **Auto Link Generation:** Automatically injects the clean IP into your base config link and generates ready-to-use configs with `💎Diamond IP` remarks.
* **Anti-DPI Engine:** Simulates real browser fingerprints (Chrome) and ALPN to bypass Cloudflare Worker restrictions and DPI systems.
* **Multi-threaded:** Fast scanning using multiple concurrent Xray cores.

### 📱 Installation (For Android/Termux)

1. Download and install **Termux** from [F-Droid](https://f-droid.org/en/packages/com.termux/) or GitHub (⚠️ Do NOT use the Google Play version as it's deprecated).
2. Open Termux and run the following commands one by one:

```bash
# Update packages and install Git
pkg update -y && pkg upgrade -y
pkg install git -y

# Clone the repository
git clone [https://github.com/smblue07/sMb-Scanner.git](https://github.com/smblue07/sMb-Scanner.git)

# Enter the directory
cd sMb-Scanner

# Run the auto-installer (Installs Python, dependencies, and Xray core)
bash install.sh
