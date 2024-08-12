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

def siteipsorgu():
    site = input("Site URL'si Giriniz: ")
    url = "https://www.ipsorgu.com/site_ip_adresi_sorgulama.php?site="+site+"#sorgu"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2000)