from os import system as c
import time
import random
import os

# Colors
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

# Logo
def logo():
    c('clear')
    print(f"""{R}
██╗    ██╗██╗███████╗██╗███████╗
██║    ██║██║██╔════╝██║██╔════╝
██║ █╗ ██║██║███████╗██║█████╗  
██║███╗██║██║╚════██║██║██╔══╝  
╚███╔███╔╝██║███████║██║███████╗
 ╚══╝╚══╝ ╚═╝╚══════╝╚═╝╚══════╝
{P}     HACKING WORLD - ROOT WIFI HACK PRANK
{A}-------------------------------------------------
""")

# Root Check
def check_root():
    if os.path.exists("/system/xbin/su") or os.path.exists("/system/bin/su"):
        print(f"{G}[✓] Root Permission Granted")
        time.sleep(1)
        return True
    else:
        print(f"{R}[!] Root Permission Not Found!")
        time.sleep(1)
        exit()

# Wifi Hack
def wifi_hack():
    logo()
    print(f"{Y}[+] Checking Root Permission...\n")
    time.sleep(1)
    check_root()

    wifi_name = input(f"{C}[+] Enter Wifi Name: ")

    print(f"\n{Y}[*] Scanning for {wifi_name}...")
    for i in range(1, 6):
        print(f"{C}[*] Signal Strength: {random.randint(80,100)}%")
        time.sleep(0.7)

    print(f"\n{G}[✓] Locked on {wifi_name}")
    time.sleep(1)
    print(f"{Y}[*] Starting Bruteforce Attack...")
    time.sleep(2)

    passwords = ["admin123", "password2024", "superwifi", "123456789", "hackzone"]
    for pw in passwords:
        print(f"{C}[*] Trying Password: {pw}")
        time.sleep(1.2)

    found_pass = random.choice(passwords)
    print(f"\n{G}[✓] Password Found: {R}{found_pass}")
    print(f"{P}[!] Note: Connect manually from your settings.")
    input(f"\n{C}Press Enter To Exit...")

# Start Tool
wifi_hack()