# 🚀 This Project is in it's early stages of Development.
# 📌 Working on new features and main menu.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 1.0.0

from selenium import webdriver
from colorama import Fore, Back, Style
import warnings
import time
import random
import string
import urllib.request
import requests
import csv
import sys
from proxyscrape import create_collector
import os
clear = lambda: os.system('clear')
clear()

collector = create_collector('my-collector', 'https')

print ('\033[31m' + """\
    ____             __              __  ___      _ __
   / __ \_________  / /_____  ____  /  |/  /___ _(_) /
  / /_/ / ___/ __ \/ __/ __ \/ __ \/ /|_/ / __ `/ / / 
 / ____/ /  / /_/ / /_/ /_/ / / / / /  / / /_/ / / /  
/_/   /_/   \____/\__/\____/_/ /_/_/  /_/\__,_/_/_/   
                                                      
    ___                               __ 
   /   | ______________  __  ______  / /_
  / /| |/ ___/ ___/ __ \/ / / / __ \/ __/
 / ___ / /__/ /__/ /_/ / /_/ / / / / /_  
/_/  |_\___/\___/\____/\__,_/_/ /_/\__/  
                                         
   ______                __            
  / ____/_______  ____ _/ /_____  _____
 / /   / ___/ _ \/ __ `/ __/ __ \/ ___/
/ /___/ /  /  __/ /_/ / /_/ /_/ / /    
\____/_/   \___/\__,_/\__/\____/_/     
""" + '\033[0m')
print ('\033[31m' + "Auto Login Script" + '\033[0m')

restart = 2
while (restart > 1):
    # Pick an email for Verification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    emailaddress = input('\033[31m' + "Enter Email Address: " + '\033[0m')

    # Pick an email for Notification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    password = input('\033[31m' + "Enter Password: " + '\033[0m')                                                    
    proxy_status = "false"
    while (proxy_status == "false"):

        # Retrieve only 'us' proxies
        proxygrab = collector.get_proxy({'code': ('us', 'uk')})
        proxy = ("{}:{}".format(proxygrab.host, proxygrab.port))
        print ('\033[31m' + "Proxy:", proxy + '\033[0m')

        try:
            proxy_host = proxygrab.host
            proxy_port = proxygrab.port
            proxy_auth = ":"
            proxies = {'http':'http://{}@{}:{}/'.format(proxy_auth, proxy_host, proxy_port)}
            requests.get("http://example.org", proxies=proxies, timeout=1.5)

        except OSError:
            print ('\033[31m' + "Proxy Connection error!" + '\033[0m')
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K") 
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K") 
            proxy_status = "false"
        else:
            print ('\033[31m' + "Proxy is working..." + '\033[0m')
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K") 
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K") 
            proxy_status = "true"


    else:
        from selenium.webdriver.chrome.options import Options 

        warnings.filterwarnings("ignore", category=DeprecationWarning) 

        options = Options()
        options.add_argument('--proxy-server={}'.format(proxy))

        # Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)
        driver = webdriver.Chrome(executable_path='/driver/chromedriver', chrome_options=options)

        url = 'http://mail.protonmail.com/login'

        driver.get(url)

        time.sleep(4)

        driver.find_element_by_id('username').send_keys(emailaddress)

        time.sleep(1)

        driver.find_element_by_id('password').send_keys(password)

        time.sleep(1)

        driver.find_element_by_id('login_btn').click()

        time.sleep(3)

        complete = "false"

        while (complete == "false"):
            complete_q = input('\033[31m' + "Are you done? y/n: " + '\033[0m')

            if complete_q == "y":
                driver.close()
                print ('\033[31m' + "Ok! The script is exiting now." + '\033[0m')
                time.sleep(1)
                clear()
                exit()
            
            else:
                print ('\033[31m' + 'Ok. Take your time.' + '\033[0m')
                time.sleep(1)
                complete = "false"
        else:
            print("something")
    