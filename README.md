\# 💎 sMb Scanner (Termux Edition)



\*\*sMb Scanner\*\* is an advanced, multi-threaded Anti-DPI V2ray IP Scanner designed specifically for Android (Termux). It tests Cloudflare, Gcore, Fastly, and custom IPs using real-world downloading stress tests to find the best "Diamond IPs" that bypass strict DPI (Deep Packet Inspection) filters.



\## 🚀 Features

\* \*\*Real Stress Testing:\*\* Instead of simple pings, it downloads files via Xray core to filter out "Zombie IPs" that drop under load.

\* \*\*Auto Link Generation:\*\* Automatically injects the clean IP into your base config link with `💎Diamond IP` remarks.

\* \*\*Anti-DPI Engine:\*\* Simulates real browser fingerprints (Chrome) and ALPN to bypass Cloudflare Worker restrictions.

\* \*\*Multi-threaded:\*\* Fast scanning using multiple concurrent Xray cores.



\## 📱 Installation (For Android/Termux)



1\. Download and install \*\*Termux\*\* from F-Droid or GitHub (Do NOT use the Google Play version).

2\. Open Termux and run the following commands one by one:



```bash

\# Clone the repository

pkg install git -y

git clone \[https://github.com/smblue07/sMb-Scanner.git](https://github.com/smblue07/sMb-Scanner.git)



\# Enter the directory

cd sMb-Scanner



\# Run the auto-installer

bash install.sh

