import os
import sys
import time

try:
    from colorama import Fore, Style, init
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, Style, init

init(autoreset=True, strip=False)

def banner():
    os.system('clear')
    Y = Fore.YELLOW + Style.BRIGHT
    R = Fore.RED + Style.BRIGHT
    G = Fore.GREEN + Style.BRIGHT
    W = Fore.WHITE + Style.BRIGHT
    M = Fore.MAGENTA + Style.BRIGHT
    C = Fore.CYAN + Style.BRIGHT

    print(f"""
{Y}    ██╗  ██╗██╗   ██╗████████╗███████╗███████╗
{Y}    ╚██╗██╔╝╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝
{Y}     ╚███╔╝  ╚████╔╝    ██║   █████╗  ███████╗
{Y}     ██╔██╗   ╚██╔╝     ██║   ██╔══╝  ╚════██║
{Y}    ██╔╝ ██╗   ██║      ██║   ███████╗███████║
{Y}    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
    """)

    print(f" {M} [ ANDROID BYPASS SYSTEM - CRACKED BY PT MEDIA ]")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    info = [
        ("PROJECT   ", "XYTEEE-XC", Y),
        ("CRACKER   ", "PHAM TIEN MEDIA", R),
        ("TELEGRAM  ", "@PTien205", C),
        ("WHATSAPP  ", "+84877667153", C),
        ("STATUS    ", "LOCAL BYPASS ACTIVE", G)
    ]

    for label, value, color in info:
        print(f" {R}[{W}●{R}] {W}{label.ljust(12)}: {color}{value}")
        time.sleep(0.03)

    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"\n {G}[+] {W}This cracked tool is 100% FREE.")
    print(f" {G}[+] {W}Admin's scam license system has been bypassed.")
    print(f"\n {W}>>> {Y}Press {R}ENTER {Y}to start the tool {W}<<<")
    input()

if __name__ == "__main__":
    banner()
    
    sys.path.append(os.getcwd())
    
    try:
        print(f"{Fore.YELLOW}[*] Initializing local module: xcmain...")
        __import__("xcmain").email_verification_system()
        
    except ImportError:
        print(f"\n{Fore.RED}[!] ERROR: 'xcmain.so' NOT FOUND!")
        print(f"{Fore.WHITE}[*] Make sure 'xcmain.so' is in the same folder as this 'run.py'.")
    except Exception as e:
        print(f"\n{Fore.RED}[!] SYSTEM ERROR: {str(e)}")
        print(f"{Fore.YELLOW}[*] Hint: Check your Python version (Python 3.12 required).")