import random
from colorama import *

def generate_user_agent():
    browsers = ["Chrome", "Firefox", "Safari", "Opera", "Edge"]
    operating_systems = [
        "Windows NT 10.0; Win64; x64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "X11; Linux x86_64",
        "iPhone; CPU iPhone OS 13_5 like Mac OS X",
        "Android 10; Mobile"
    ]
    chrome_versions = [f"Chrome/{random.randint(70, 89)}.0.{random.randint(1000, 4999)}.{random.randint(100, 999)}"]
    firefox_versions = [f"Firefox/{random.randint(60, 89)}.0"]
    safari_versions = [f"Safari/{random.randint(600, 899)}.0.{random.randint(10, 99)}"]
    opera_versions = [f"OPR/{random.randint(50, 75)}.0.{random.randint(2000, 2999)}.{random.randint(100, 999)}"]
    edge_versions = [f"Edg/{random.randint(80, 90)}.0.{random.randint(600, 999)}.{random.randint(100, 999)}"]

    browser = random.choice(browsers)
    os = random.choice(operating_systems)
    
    if browser == "Chrome":
        version = random.choice(chrome_versions)
    elif browser == "Firefox":
        version = random.choice(firefox_versions)
    elif browser == "Safari":
        version = random.choice(safari_versions)
    elif browser == "Opera":
        version = random.choice(opera_versions)
    elif browser == "Edge":
        version = random.choice(edge_versions)

    user_agent = f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) {version} Safari/537.36"
    print(Fore.GREEN,user_agent)
    return user_agent