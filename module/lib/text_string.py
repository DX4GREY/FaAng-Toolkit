from colorama import Fore
def menus():
    menu = [
        "UDP       layer4 => UDP Attack", 
        "TCP       layer4 => TCP Attack", 
        "", 
        "GET       layer7 => 'Requests GET' Attack", 
        "POS       layer7 => 'Requests POST' Attack", 
        "SOC       layer7 => Socket Attack" , 
        "HTTP2     layer7 => HTTP 2.0 Request Attack", 
        "SPOOF     layer7 => HTTP Spoof Socket Attack  ", 
        "HEAD      layer7 => Head Request Attack", 
        "SKY       layer7 => Sky method", 
        "CFREQ    layer7 => Bypass CF UAM, CAPTCHA, BFM (request)", 
        "CFSOC    layer7 => Bypass CF UAM, CAPTCHA, BFM (socket)", 
        "CFB      layer7 => Bypass CF Attack"
    ]
    return menu

def logos():
    logo = f"""
{Fore.MAGENTA} █████▒▄▄▄          ▄▄▄       ███▄    █   ▄████ 
▓██   ▒▒████▄       ▒████▄     ██ ▀█   █  ██▒ ▀█▒
▒████ ░▒██  ▀█▄     ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░
{Fore.RESET}░▓█▒  ░░██▄▄▄▄██    ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓
░▒█░    ▓█   ▓██▒    ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒
 ▒ ░    ▒▒   ▓▒█░    ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ 
 ░       ▒   ▒▒ ░     ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░ ░     ░   ▒        ░   ▒      ░   ░ ░ ░ ░   ░ 
             ░  ░         ░  ░         ░       ░ 
                                                 
THE OWNER OF THESE TOOLS (Dx4) WILL NOT BE RESPONSIBLE 
FOR ANY DAMAGE CAUSED BY THE USER OWN THEREFORE,
USE THESE TOOLS ONLY TO TEST YOUR OWN SITE FOR {Fore.GREEN}VULNERABILITIES 
{Fore.RESET}ATTACKING SITES OWNED BY OTHERS, {Fore.YELLOW}FAANG SHOULD 
NOT BE USED FOR ILLEGAL ACTIVITIES{Fore.RESET}, BY USING THIS SOFTWARE, 
{Fore.RED}YOU MUST AGREE TO BE FULLY RESPONSIBLE FOR DAMAGE 
CAUSED BY FAANG IN ANY WAY TO YOUR OWN{Fore.RESET}. THE CREATORS 
DO NOT WANT PEOPLE TO USE FAANG IF THEY HAVE NO 
EXPERIENCE WITH ATTACKS INCLUDING. ANY ATTACK WILL CAUSE 
TEMPORARY DAMAGE, BUT {Fore.YELLOW}LONG TERM DAMAGE{Fore.RESET} IS POSSIBLE. 
FAANG SHOULD NOT ADVISE PEOPLE TO DO {Fore.RED}ILLEGAL ACTIVITIES{Fore.RESET}.
"""
    return logo