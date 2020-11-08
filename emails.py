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
from selenium.webdriver.chrome.options import Options 
import os
clear = lambda: os.system('clear')
clear()
i = 0
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

print ('\033[31m' + "Auto Account Creator Script" + '\033[0m')
print('\033[31m' + "Pick a proxy option:" + '\033[0m')
print('\033[31m' + "(1) - Crawl Free Proxies (recommended)" + '\033[0m')
print('\033[31m' + "(2) - Load from file" + '\033[0m')
print('\033[31m' + "(3) - No Proxy (experimental)" + '\033[0m')
proxy_option = input('\033[31m' + "Enter you option number: " + '\033[0m')
sys.stdout.write("\033[F") 
sys.stdout.write("\033[K") 
sys.stdout.write("\033[F")
sys.stdout.write("\033[K")
sys.stdout.write("\033[F")
sys.stdout.write("\033[K")
sys.stdout.write("\033[F")
sys.stdout.write("\033[K") 
restart2 = 2
while (restart2 > 1):
    # Pick an email for Verification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    verifymail = input('\033[31m' + "Enter Email Adress for Verification: " + '\033[0m')

    # Pick an email for Notification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    notifymail = input('\033[31m' + "(Optional) Enter Email Adress for Recovery: " + '\033[0m') 


    if proxy_option == "1":
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K") 
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")  
        proxy_status = "false"
        while (proxy_status == "false"):

            # Retrieve only 'us' proxies
            proxygrab = collector.get_proxy({'code': ('us')})
            proxy = ("{}:{}".format(proxygrab.host, proxygrab.port))
            print ('\033[31m' + "Proxy:", proxy + '\033[0m')

            try:
                proxy_host = proxygrab.host
                proxy_port = proxygrab.port
                proxy_auth = ":"
                proxies = {'http':'http://{}@{}:{}/'.format(proxy_auth, proxy_host, proxy_port)}
                requests.get("http://protonmail.com/", proxies=proxies, timeout=1.5)

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
                options = Options()
                options.add_argument('--proxy-server={}'.format(proxy))
    else:
        pass

    if proxy_option == "2":
        print('\033[31m' + "Getting Proxies from file..." + '\033[0m')
        with open('./proxy.txt', 'r') as data:
            proxy_lines = [line.strip() for line in data]
        proxy_from_file = "false"
        while (proxy_from_file == "false"):
            i += 1
            print('\033[31m' + proxy_lines[i] + '\033[0m')
            try:
                proxies_file = {'http':'http://:@{}/'.format(proxy_lines[i])}
                requests.get("http://protonmail.com/", proxies=proxies_file, timeout=1.5)
            except OSError:
                print ('\033[31m' + "Proxy Connection error!" + '\033[0m')
                proxy_from_file = "false"
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K") 
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K") 
            else:
                print ('\033[31m' + "Proxy is working..." + '\033[0m')
                i += 1
                options = Options()
                options.add_argument('--proxy-server={}'.format(proxy_lines[i]))
                proxy_from_file = "true"
                proxy_option 
    else:
        pass         
    if proxy_option == "3":
        options = Options()
        print('\033[31m' + "This is experimental! Script might not work in this mode" + '\033[0m')
    else:
        pass

    warnings.filterwarnings("ignore", category=DeprecationWarning) 

    # Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path='./driver/chromedriver', chrome_options=options)

    url = 'http://protonmail.com/signup'

    def randomStringDigits(stringLength=13):
        # Generate a random string of letters and digits
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    rngusername = randomStringDigits(13)
    rngpassword = randomStringDigits(15) 
    
    driver.get(url)

    time.sleep(4)

    driver.find_element_by_class_name('panel-heading').click()

    time.sleep(1)

    driver.find_element_by_id('freePlan').click()

    time.sleep(4)

    driver.switch_to_frame(0)

    time.sleep(3)

    driver.find_element_by_id('username').send_keys(rngusername)

    time.sleep(1)

    driver.switch_to.default_content()

    time.sleep(1)

    driver.find_element_by_id('password').send_keys(rngpassword)

    time.sleep(1)

    driver.find_element_by_id('passwordc').send_keys(rngpassword)

    time.sleep(1)

    driver.switch_to_frame(1)

    time.sleep(1)

    if notifymail == "x" or notifymail == "":
        notifymail = "mail@mail.com"
    else:
        pass
    driver.find_element_by_id('notificationEmail').send_keys(notifymail)

    time.sleep(1)

    driver.find_element_by_name('submitBtn').click()

    time.sleep(6)

    print('\033[31m' + "What type of verification do you want to use?" + '\033[0m')
    print('\033[31m' + "(1) Email verification" + '\033[0m')
    print('\033[31m' + "(2) Captcha verification" + '\033[0m')
    verifymethod = input('\033[31m' + "Enter Verification Method: " + '\033[0m')
    if verifymethod == "1":
        driver.find_element_by_id('id-signup-radio-email').click()

        time.sleep(1)

        driver.find_element_by_id('emailVerification').send_keys(verifymail)

        time.sleep(1)

        driver.find_element_by_class_name('codeVerificator-btn-send').click()

        time.sleep(3)
    elif verifymethod == "2":
        print('\033[31m' + "Please complete the captcha in your browser. " + '\033[0m')
        captchadone = input('\033[31m' + "Hit enter when captcha is complete" + '\033[0m')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div/div/p[3]/button').click()

    print ('\033[31m' + "Your New Email Adress is: ", rngusername,"@protonmail.com", sep='' + '\033[0m')
    print ('\033[31m' + "Your New Email Password is: "  + '\033[0m' , rngpassword)
    
    complete = "false"

    while (complete == "false"):
        complete_q = input('\033[31m' + "Did you complete the Verification process? y/n: " + '\033[0m')

        if complete_q == "y":
            driver.close()
            csvData = [[rngusername + '@protonmail.com', rngpassword]]
            with open('list.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(csvData)
            csvFile.close()
            print ('\033[31m' + 'Great! We added you account details to the table.' + '\033[0m')
            complete = "true"
        
        else:
            print ('\033[31m' + 'Please try verifing and try again' + '\033[0m')
            time.sleep(1)
            complete = "false"
    else:
        restart_s = input('\033[31m' + "Do you want to restart the Script and create more Accounts? y/n: " + '\033[0m')
        if restart_s == "y":
            i += 1
            clear()
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
            restart2 == 3

        else:
            print ('\033[31m' + "Ok! The script is exiting now." + '\033[0m')
            time.sleep(1)
            exit()
