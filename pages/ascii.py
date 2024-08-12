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

def ascii():
    yazi = input("ASCII Olacak Yazıyı Yazın: ")
    url = "https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t="+yazi+"%0A"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)
    pre_element = driver.find_element(By.ID, "taag_output_text")
    output = pre_element.get_attribute('innerText')

    system("cls||clear")
    print(output)