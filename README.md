# FaAng - DDoS Tools
<img src="https://img.shields.io/badge/Python-3.11-red"></img> <img src="https://img.shields.io/badge/FaAng-BETA-blue"></img> <img src="https://img.shields.io/badge/Kali Linux-2023.1-green"></img> <img src="https://img.shields.io/badge/Ubuntu-20.04-yellow"></img><br>

<h2>List In Script</h2>
<b>[1]</b> UDP       layer4 => UDP Attack<br>
<b>[2]</b> TCP       layer4 => TCP Attack<br>
<b>[3]</b> GET       layer7 => 'Requests GET' Attack<br>
<b>[4]</b> POS       layer7 => 'Requests POST' Attack<br>
<b>[5]</b> SOC       layer7 => Socket Attack<br>
<b>[6]</b> HTTP2     layer7 => HTTP 2.0 Request Attack<br>
<b>[7]</b> SPOOF     layer7 => HTTP Spoof Socket Attack<br>
<b>[8]</b> HEAD      layer7 => Head Request Attack<br>
<b>[9]</b> SKY       layer7 => Sky method<br>
<b>[10]</b> CFREQ    layer7 => Bypass CF UAM, CAPTCHA, BFM (request)<br>
<b>[11]</b> CFSOC    layer7 => Bypass CF UAM, CAPTCHA, BFM (socket)<br>
<b>[12]</b> CFB    layer7 => Bypass CF Attack<br>

# INSTALLATION
  
Installation support for Kali Linux, Ubuntu And Termux

Just enter this command
```bash
curl -s https://raw.githubusercontent.com/DX4GREY/FaAng-Toolkit/main/install.sh | bash -s
```

How to uninstall
```bash
faang --uninstall
```

# HOW TO RUN
1. Open terminal and type command
```bash
faang [type] [method] [target] [thread] [time]
```

if python not installed, try install manually

Linux
```bash
sudo apt install python
```
Termux
```bash
pkg install python
```

and if done, install again this script
```bash
curl -s https://raw.githubusercontent.com/DX4GREY/FaAng-Toolkit/main/install.sh | bash -s
```
# DESCRIPTION
This script appears to be a DDoS (Distributed Denial of Service) toolkit developed in Python. It is designed to launch various types of DDoS attacks, both on layer 4 (transport layer) and layer 7 (application layer). The script offers multiple attack methods and options, allowing users to target specific websites or servers with a flood of requests, thereby overwhelming the target's resources and causing it to become inaccessible to legitimate users.

The script includes features such as handling UDP and TCP flood attacks, sending GET and POST requests to exhaust web server resources, spoofing HTTP requests, utilizing HTTP 2.0, using socket-based attacks, and bypassing security mechanisms like Cloudflare (CF). Additionally, the script seems to provide a login mechanism, allowing users to authenticate and access the DDoS attack functionalities.

The script's interface displays a menu of attack options, where users can select the attack method, specify the target, set the number of threads, and specify the duration of the attack. The script also provides a countdown timer for the duration of the attack.

It's important to note that DDoS attacks are illegal and unethical unless performed with proper authorization for security testing purposes. Such attacks can cause significant harm to targeted systems and networks. If you're interested in cybersecurity or ethical hacking, I would recommend focusing on learning defensive techniques and security best practices rather than engaging in offensive activities like DDoS attacks.

# WARNING
THE OWNER OF THESE TOOLS (Dx4) WILL NOT BE RESPONSIBLE FOR ANY DAMAGE CAUSED BY THE USER OWN THEREFORE, USE THESE TOOLS ONLY TO TEST YOUR OWN SITE FOR vulnerabilities ATTACKING SITES OWNED BY OTHERS, FAANG SHOULD NOT BE USED FOR ILLEGAL ACTIVITIES, BY USING THIS SOFTWARE, YOU MUST AGREE TO BE FULLY RESPONSIBLE FOR DAMAGE CAUSED BY FAANG IN ANY WAY TO YOUR OWN. THE CREATORS DO NOT WANT PEOPLE TO USE FAANG IF THEY HAVE NO EXPERIENCE WITH ATTACKS INCLUDING. ANY ATTACK WILL CAUSE TEMPORARY DAMAGE, BUT LONG TERM DAMAGE IS POSSIBLE. RAVEN-STORM SHOULD NOT ADVISE PEOPLE TO DO ILLEGAL ACTIVITIES.
