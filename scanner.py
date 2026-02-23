import json
import subprocess
import time
import requests
import os
import ipaddress
import concurrent.futures
import itertools
import threading
import urllib.parse
import socket
import re

print_lock = threading.Lock()

def get_ips_from_file(file_path):
    ip_list = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line: continue
                try:
                    if "/" in line:
                        for ip in ipaddress.IPv4Network(line, strict=False).hosts(): ip_list.append(str(ip))
                    else:
                        ip_list.append(str(ipaddress.IPv4Address(line)))
                except ValueError:
                    if re.match(r'^[a-zA-Z0-9.-]+$', line): ip_list.append(line)
        return list(dict.fromkeys(ip_list))
    except FileNotFoundError: return None

def generate_simple_link(base_link, new_ip, index):
    temp_link = re.sub(r'(@)([^/?#:]+)', r'\g<1>' + new_ip, base_link, count=1)
    if '#' in temp_link:
        temp_link = temp_link[:temp_link.rfind('#')]
    new_name = urllib.parse.quote(f"💎Diamond IP {index}")
    return f"{temp_link}#{new_name}"

def link_to_json(link, new_ip, port):
    try:
        parsed = urllib.parse.urlparse(link)
        original_domain = parsed.hostname
        qs = dict(urllib.parse.parse_qsl(parsed.query))
        
        security = qs.get("security", "none")
        network = qs.get("type", "tcp")
        sni = qs.get("sni", original_domain)
        ws_host = qs.get("host", original_domain)
        ws_path = qs.get("path", "/")
        
        fp = qs.get("fp", "chrome")
        alpn_raw = qs.get("alpn", "h2,http/1.1")
        alpn = alpn_raw.split(",") if alpn_raw else []
        
        outbound = {
            "tag": "proxy", "protocol": parsed.scheme, "settings": {},
            "streamSettings": {"network": network, "security": security}
        }

        port_num = int(parsed.port) if parsed.port else 443

        if parsed.scheme == "vless":
            outbound["settings"]["vnext"] = [{"address": new_ip, "port": port_num, "users": [{"id": parsed.username, "encryption": "none"}]}]
        elif parsed.scheme == "trojan":
            outbound["settings"]["servers"] = [{"address": new_ip, "port": port_num, "password": parsed.username}]
        else: return None

        if security == "tls":
            outbound["streamSettings"]["tlsSettings"] = {"allowInsecure": True, "serverName": sni, "fingerprint": fp, "alpn": alpn}
        if network == "ws":
            outbound["streamSettings"]["wsSettings"] = {"path": ws_path, "headers": {"Host": ws_host}}

        return {
            "log": {"loglevel": "none"},
            "inbounds": [{"listen": "127.0.0.1", "port": port, "protocol": "http", "settings": {"allowTransparent": False}}],
            "outbounds": [outbound],
            "routing": {"domainStrategy": "AsIs", "rules": [{"type": "field", "network": "tcp,udp", "outboundTag": "proxy"}]}
        }
    except Exception: return None

def test_ip(ip, base_link, port_allocator):
    port = next(port_allocator)
    temp_filename = f"temp_{port}.json"
    
    local_json = link_to_json(base_link, ip, port)
    if not local_json: return None

    with open(temp_filename, "w", encoding="utf-8") as f: json.dump(local_json, f)
        
    xray_process = None
    try:
        xray_process = subprocess.Popen(["./xray", "-c", temp_filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        port_ready = False
        start_wait = time.time()
        while time.time() - start_wait < 5:
            if xray_process.poll() is not None: break
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                    port_ready = True
                    break
            except: time.sleep(0.2)
        
        if port_ready:
            session = requests.Session()
            session.trust_env = False
            session.proxies = {'http': f'http://127.0.0.1:{port}', 'https': f'http://127.0.0.1:{port}'}
            
            ping_start = time.time()
            res_ping = session.get("https://www.gstatic.com/generate_204", timeout=4)
            if res_ping.status_code != 204: return None
            ping_time = int((time.time() - ping_start) * 1000)
            
            stress_start = time.time()
            res_stress = session.get("https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js", timeout=8)
            
            if res_stress.status_code == 200 and len(res_stress.content) > 100000:
                duration = time.time() - stress_start
                speed_kbps = int((len(res_stress.content) / 1024) / duration)
                
                if speed_kbps < 10:
                    with print_lock: print(f"[🐌 ZOMBIE]  Target: {ip:<18} | Speed: {speed_kbps} KB/s (Too Slow)")
                    return None
                else:
                    with print_lock: print(f"[💎 DIAMOND] Target: {ip:<18} | Speed: {speed_kbps} KB/s | Ping: {ping_time}ms")
                    return (ip, speed_kbps, ping_time)
            else: return None
        else: return None
            
    except requests.exceptions.RequestException:
        with print_lock: print(f"[❌ TIMEOUT] Target: {ip:<18} | Blocked by DPI")
        return None
    finally:
        if xray_process:
            try: xray_process.terminate(); xray_process.wait(timeout=1)
            except: pass
        if os.path.exists(temp_filename):
            try: os.remove(temp_filename)
            except: pass

def kill_xray():
    os.system("pkill -f xray > /dev/null 2>&1")

def show_banner():
    os.system('clear')
    banner = r"""
  ███████╗███╗   ███╗██████╗     ███████╗██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
  ██╔════╝████╗ ████║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
  ███████╗██╔████╔██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
  ╚════██║██║╚██╔╝██║██╔══██╗    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
  ███████║██║ ╚═╝ ██║██████╔╝    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
  ╚══════╝╚═╝     ╚═╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
  ===========================================================================================
             🔥 sMb Anti-DPI Scanner [TERMUX / ANDROID EDITION] 🔥
  ===========================================================================================
    """
    print(banner)

def main():
    while True:
        show_banner()
        kill_xray()
        
        if not os.path.exists("xray"):
            print("[ERROR] 'xray' core not found in the current directory!")
            print("Please run 'bash install.sh' first.")
            input("\nPress Enter to exit...")
            break
            
        print("Paste your WORKING Base Config Link (vless://...)")
        base_link = input("Link: ").strip()
        if not base_link: continue
        
        print("\nSelect Target List:")
        print("1. Cloudflare")
        print("2. Gcore")
        print("3. Fastly")
        print("4. Custom (ips.txt)")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        cdn_files = {
            "1": ("cloudflare.txt", ["104.17.2.1", "172.64.1.0/29"]),
            "2": ("gcore.txt", ["146.185.210.1", "92.223.73.1"]),
            "3": ("fastly.txt", ["151.101.1.57", "146.75.113.57"]),
            "4": ("ips.txt", ["cip1.nasbasan.ir", "104.17.2.158"])
        }
        
        if choice not in cdn_files:
            print("[ERROR] Invalid choice!"); time.sleep(2); continue
            
        file_name, sample_ips = cdn_files[choice]
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                for ip in sample_ips: f.write(ip + "\n")
                
        ips = get_ips_from_file(file_name)
        if not ips: 
            print("[ERROR] No IPs found!"); time.sleep(2); continue

        MAX_THREADS = 10 
        port_allocator = itertools.count(20000)
        
        print(f"\n[*] Extracted {len(ips)} targets.")
        print(f"[*] Starting sMb TEST ENGINE with {MAX_THREADS} threads...\n")
        print("-" * 65)
        
        working_ips = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            futures = [executor.submit(test_ip, ip, base_link, port_allocator) for ip in ips]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result: working_ips.append(result)

        print("-" * 65)
        print("\n" + "=" * 65)
        print("         💎 READY TO USE DIAMOND LINKS 💎")
        print("=" * 65)
        if working_ips:
            working_ips.sort(key=lambda x: x[1], reverse=True)
            with open("diamond_configs.txt", "w", encoding="utf-8") as f:
                for index, (ip, speed, delay) in enumerate(working_ips, 1):
                    final_link = generate_simple_link(base_link, ip, index)
                    print(f"💎 Speed: {speed} KB/s | Ping: {delay}ms | Diamond IP {index}")
                    print(f"{final_link}\n")
                    f.write(f"{final_link}\n")
            print("[INFO] Links saved to 'diamond_configs.txt'. Use 'cat diamond_configs.txt' to view!")
        else:
            print("All targets were zombies or blocked. No diamonds found this time.")
            
        kill_xray()
        
        print("\n" + "-" * 65)
        print("What would you like to do next?")
        print("[1] Run another scan (New List / New Link)")
        print("[2] Exit")
        
        end_choice = input("\nEnter your choice (1-2): ").strip()
        if end_choice != '1': break

if __name__ == "__main__":
    main()