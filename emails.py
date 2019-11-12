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
print ('\033[31m' + "Auto Account Creator Script" + '\033[0m')

restart = 2
while (restart > 1):
    # Pick an email for Verification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    verifymail = input('\033[31m' + "Enter Email Adress for Verification: " + '\033[0m')

    # Pick an email for Notification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    notifymail = input('\033[31m' + "Enter Email Adress for Recovery: " + '\033[0m')                                                    
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

        driver.find_element_by_id('notificationEmail').send_keys(notifymail)

        time.sleep(1)

        driver.find_element_by_name('submitBtn').click()

        time.sleep(6)

        driver.find_element_by_id('id-signup-radio-email').click()

        time.sleep(1)

        driver.find_element_by_id('emailVerification').send_keys(verifymail)

        time.sleep(1)

        driver.find_element_by_class_name('codeVerificator-btn-send').click()

        time.sleep(3)

        print ('\033[31m' + "Your New Email Adress is: ", rngusername,"@protonmail.com", sep='' + '\033[0m')
        print ('\033[31m' + "Your New Email Password is: "  + '\033[0m' , rngpassword)

        complete = "false"

        while (complete == "false"):
            complete_q = input("Did you complete the Verification process? y/n: ")

            if complete_q == "y":
                driver.close()
                csvData = [[rngusername + '@protonmail.com', rngpassword]]
                with open('list.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(csvData)
                csvFile.close()
                print ('Great! We added you account details to the table.')
                complete = "true"
            
            else:
                print ('Please try verifing and try again')
                time.sleep(1)
                complete = "false"
        else:
            restart_s = input("Do you want to restart the Script and create more Accounts? y/n: ")
            if restart_s == "y":
                restart ++ 1
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

            else:
                print ("Ok! The script is exiting now.")
                time.sleep(1)
                exit()
else:
    print("something")