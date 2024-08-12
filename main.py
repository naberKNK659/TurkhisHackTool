from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, wait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.generate_user_agent import *
from pages.perform_syn_flood import *
from string import ascii_lowercase
from pages.wimuseragent import *
from pages.siteipsorgu import *
from selenium import webdriver
from pages.smsbomber import *
from bs4 import BeautifulSoup
from pages.ipsorgu import *
from os import system, sys
from pages.tarama import *
from pages.passwd import *
from pages.ascii import *
from pages.DDoS import *
from scapy.all import *
from colorama import *
import threading
import requests
import random
import time
import os

def scm():
    system('cls||clear')
    menu_options = {
        "SmsBomber": Fore.YELLOW + "1 - SmsBomber",
        "User-Agent'imNe?": Fore.CYAN + "2 - User-Agent'imNe?",
        "GenerateUser-Agent": Fore.MAGENTA + "3 - GenerateUser-Agent",
        "ASCİİ": Fore.GREEN + "4 - ASCİİ",
        "DDoS": Fore.RED + "5 - DDoS",
        "ipSorgu": Fore.BLUE + "6 - ipSorgu",
        "SiteİPSorgu": Fore.LIGHTBLUE_EX + "7 - SiteİPSorgu",
        "SYN-Flood": Fore.LIGHTRED_EX + "8 - SYN-Flood",
        "ŞifreOluşturucu": Fore.LIGHTGREEN_EX + "9 - ŞifreOluşturucu",
        "AçıkTarama": Fore.LIGHTYELLOW_EX + "0 - AçıkTarama"
    }

    print("Seçenekler:")
    for option in menu_options.values():
        print(option)

    user_choice = input(Fore.WHITE + Style.BRIGHT + "\nSeçiminizi yapınız: ")

    try:
        user_choice = int(user_choice)
    except ValueError:
        print(Fore.RED + "Hatalı giriş, lütfen sadece sayılar girin!")
        time.sleep(2)
        return

    if user_choice == 1:
        smsbomber()
    elif user_choice == 2:
        wimuseragent()
    elif user_choice == 3:
        generate_user_agent()
    elif user_choice == 4:
        ascii()
    elif user_choice == 5:
        DDoS()
    elif user_choice == 6:
        ipsorgu()
    elif user_choice == 7:
        siteipsorgu()
    elif user_choice == 8:
        perform_syn_flood()
    elif user_choice == 9:
        passwd()
    elif user_choice == 0:
        tarama()
    else:
        print(Fore.RED + "Hatalı Seçim Yaptınız!")
        time.sleep(2)
scm()