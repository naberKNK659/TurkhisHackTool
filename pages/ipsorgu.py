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

def ipsorgu():
    ip = input("İP Adresi Giriniz: ")
    url = "https://www.ipsorgu.com/?ip="+ip+"#sorgu"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2000)