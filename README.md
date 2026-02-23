# 💎 sMb Scanner (Anti-DPI V2ray Engine)

![Version](https://img.shields.io/badge/Version-1.0-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Termux-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

> **🌍 Choose your language / زبان خود را انتخاب کنید:**
> * [🇺🇸 English Documentation](#english-docs)
> * [🇮🇷 راهنمای فارسی](#persian-docs)

---

<a id="english-docs"></a>
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
```

### 🛠️ Usage

After installation, simply run the scanner:
```bash
python scanner.py
```
1. Paste your working base config link (e.g., `vless://...`).
2. Choose your target CDN (Cloudflare, Gcore, Fastly, or Custom IPs).
3. Wait for the scan to finish.
4. View your Diamond links by typing: `cat diamond_configs.txt`
5. Copy the generated links and paste them into v2rayN, v2rayNG, or V2Box!

---

<a id="persian-docs"></a>
## 🇮🇷 راهنمای فارسی

اسکنر **sMb Scanner** یک ابزار پیشرفته، چندرشته‌ای و ضد فیلترینگ (Anti-DPI) است که به طور اختصاصی برای اجرا در اندروید (محیط ترموکس) طراحی شده است. این ابزار به جای پینگ گرفتن ساده، آی‌پی‌های کلادفلر، جی‌کور، فستلی و... را زیر بار دانلود واقعی تست می‌کند تا **«آی‌پی‌های الماس 💎»** که از سد فیلترینگ عبور می‌کنند را استخراج کند.

### 🚀 ویژگی‌های کلیدی
* **تست استرس واقعی:** به جای گول خوردن با پینگ‌های فیک، برنامه یک فایل واقعی را از طریق هسته Xray دانلود می‌کند. آی‌پی‌های ضعیف (زامبی) در این مرحله حذف می‌شوند!
* **تولید خودکار لینک:** نیازی به جایگذاری دستی آی‌پی‌ها نیست؛ برنامه خودش آی‌پی تمیز را داخل لینک کانفیگ شما می‌کارد و لینک‌های آماده با نام `💎Diamond IP` تحویلتان می‌دهد.
* **موتور ضد فیلترینگ:** شبیه‌سازی دقیق اثر انگشت مرورگر کروم (Fingerprint) و ALPN برای جلوگیری از مسدود شدن توسط کلادفلر و سیستم‌های DPI.
* **سرعت بالا (Multi-threaded):** اسکن همزمان چندین آی‌پی برای رسیدن به سریع‌ترین نتیجه در گوشی.

### 📱 آموزش نصب (مخصوص اندروید / ترموکس)

۱. برنامه **Termux** را از [F-Droid](https://f-droid.org/en/packages/com.termux/) یا گیت‌هاب دانلود و نصب کنید. (⚠️ نسخه گوگل‌پلی خراب است، از آن استفاده نکنید).
۲. ترموکس را باز کرده و دستورات زیر را خط به خط کپی و اجرا کنید:

```bash
# آپدیت مخازن و نصب گیت
pkg update -y && pkg upgrade -y
pkg install git -y

# دریافت کدهای اسکنر از گیت‌هاب
git clone [https://github.com/smblue07/sMb-Scanner.git](https://github.com/smblue07/sMb-Scanner.git)

# ورود به پوشه اسکنر
cd sMb-Scanner

# اجرای نصب‌کننده خودکار (نصب پایتون، پیش‌نیازها و هسته Xray)
bash install.sh
```

### 🛠️ نحوه استفاده

بعد از پایان نصب، برای اجرای اسکنر کافیست دستور زیر را وارد کنید:
```bash
python scanner.py
```
۱. لینک کانفیگِ سالم و پایه خود را (مثلا `vless://...`) وارد کنید.
۲. لیست هدف خود را انتخاب کنید (کلادفلر، فستلی، جی‌کور یا لیست دلخواه).
۳. منتظر بمانید تا تست‌های سنگین دانلود انجام شود.
۴. در پایان، برای دیدن لینک‌های الماسِ استخراج شده دستور زیر را بزنید: 
```bash
cat diamond_configs.txt
```
۵. لینک‌ها را کپی کرده و در برنامه v2rayNG (یا برنامه‌های مشابه) پیست کنید و از اینترنت آزاد لذت ببرید!


---
---

## 💖 Support & Donate / حمایت مالی

If this tool helped you bypass internet restrictions and saved your time, you can support its future development by buying me a coffee! ☕

اگر این پروژه برای شما مفید بود و باعث شد به اینترنت آزاد دسترسی پیدا کنید، می‌توانید با حمایت مالی خود به من برای توسعه و آپدیت‌های بعدی این ابزار انگیزه بدهید! ☕


**🪙 Crypto Wallets (TRC20 Network):**
* **USDT (Tether):** `TU2J1k4mCMtLQdjHcfgP49bTzxjyUQJYM9`
* **TRX (Tron):** `TU2J1k4mCMtLQdjHcfgP49bTzxjyUQJYM9`

---
*Created with ❤️ by **[sMb](https://github.com/smblue07)***

