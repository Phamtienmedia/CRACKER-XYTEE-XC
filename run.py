import os, sys, time, glob

try:
    from colorama import Fore, Style, init
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, Style, init

init(autoreset=True, strip=False)

def banner():
    os.system('clear')
    Y, R, G, W, M, C = Fore.YELLOW + Style.BRIGHT, Fore.RED + Style.BRIGHT, Fore.GREEN + Style.BRIGHT, Fore.WHITE + Style.BRIGHT, Fore.MAGENTA + Style.BRIGHT, Fore.CYAN + Style.BRIGHT

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
    print(f" {R}[{W}●{R}] {W}PROJECT     : {Y}XYTEEE-XC")
    print(f" {R}[{W}●{R}] {W}CRACKER     : {R}PHAM TIEN MEDIA")
    print(f" {R}[{W}●{R}] {W}STATUS      : {G}BYPASS ACTIVE")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"\n {G}[+] {W}Admin's scam system has been bypassed.")
    print(f" {G}[+] {W}Free tool for everyone. Enjoy!")
    print(f"\n {W}>>> {Y}Press {R}ENTER {Y}to start {W}<<<")
    input()

if __name__ == "__main__":
    banner()
    sys.path.append(os.getcwd())
    try:
        # Tự động tìm file xcmain.cpython-312.so và lấy tên 'xcmain' để load
        # Lệnh này sẽ tìm bất cứ file nào bắt đầu bằng xcmain và kết thúc bằng .so
        __import__("xcmain").email_verification_system()
    except Exception as e:
        # Nếu load trực tiếp thất bại, dùng glob để quét tên chính xác
        try:
            target = glob.glob("xcmain*.so")[0].split('.')[0]
            __import__(target).email_verification_system()
        except:
            exit(f"\n{Fore.RED}[!] Error: {str(e)}")