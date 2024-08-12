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

def wimuseragent():
    opt = Options()
    opt.add_argument('--headless')
    driver = webdriver.Chrome(options=opt)
    driver.get('https://www.whatismyuseragent.com')

    textarea = driver.find_element(By.ID, 'text-box')
    user_agent = textarea.get_attribute('value')

    print("User-Agent'iniz:", Fore.GREEN, user_agent)
    driver.quit()