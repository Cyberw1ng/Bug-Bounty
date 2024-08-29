import webbrowser
import time
import sys
import pyfiglet

def display_banner():
    banner = pyfiglet.figlet_format("DorkOpen", font="slant")
    print(banner)
    print("Created by Karthikeyan Nagaraj")

def open_dorks(file_path, domain=None):
    with open(file_path, 'r') as file:
        dorks = file.readlines()

    count = 0
    while count < len(dorks):
        for _ in range(10):
            if count < len(dorks):
                dork = dorks[count].strip()
                if domain:
                    dork = dork.replace('site:example.com', f'site:{domain}')
                if dork:
                    url = f"https://www.google.com/search?q={dork}"
                    webbrowser.open(url)
                    time.sleep(1)  # Delay to prevent overwhelming the browser
                count += 1
        if count < len(dorks):
            input("Can I open the next 10 dorks? Press Enter to continue...")

if __name__ == "__main__":

    display_banner()

    # Read command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 dorkopen.py <dorks_file> [domain]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    domain = sys.argv[2] if len(sys.argv) > 2 else None
    
    open_dorks(file_path, domain)
