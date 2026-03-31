import requests
from datetime import datetime

URLS = [
    "https://google.com",
    "https://github.com",
    "https://python.org",
    "https://nieistniejaca-strona-xyz.pl"
]

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def loguj(wiadomosc):
    czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "OK" in wiadomosc:
        kolor = GREEN
    elif "ERROR" in wiadomosc:
        kolor = YELLOW
    elif "FAIL" in wiadomosc:
        kolor = RED
    else:
        kolor = RESET
    print(f"{kolor}[{czas}] {wiadomosc}{RESET}")
    with open("monitoring.log", "a") as f:
        f.write(f"[{czas}] {wiadomosc}\n")

def alert(wiadomosc):
    print("\n + ""!"*50)
    print("ALERT:", wiadomosc)
    print("!"*50 + "\n")



def sprawdz_uslugi():
    for url in URLS:
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                loguj(f"OK     {url}  {r.status_code}")
            else:
                loguj(f"ERROR  {url}  {r.status_code}")
        except Exception as e:
            loguj(f"FAIL   {url}  {e}")
            alert(f"Uwaga! Usługa padła: {url}")


sprawdz_uslugi()