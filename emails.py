# 🚀 This Project is in it's early stages of Development.
# 📌 Working on new features and main menu.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 1.0.2

from selenium import webdriver
import warnings
import time
import random
import string
import requests
import csv
import sys
from proxyscrape import create_collector
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException
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
while (True):
    # Pick an email for Verification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    verifymail = input('\033[31m' + "Enter Email Adress for Verification(x for Automatic Mode): " + '\033[0m')

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
                requests.get("http://protonmail.com/", proxies=proxies, timeout=3.5)

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
            first_char = data.read(1)
            if not first_char:
                print("You do not have any proxies in the proxy.txt file")
                exit(1)
            proxy_lines = [line.strip() for line in data]
        proxy_from_file = "false"
        i = 0
        while (proxy_from_file == "false"):
            print('\033[31m' + proxy_lines[i] + '\033[0m')
            try:
                proxies_file = {'http':'http://:@{}/'.format(proxy_lines[i])}
                requests.get("http://protonmail.com/", proxies=proxies_file, timeout=3.5)
            except OSError:
                print ('\033[31m' + "Proxy Connection error!" + '\033[0m')
                proxy_from_file = "false"
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K") 
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                i += 1
            else:
                print ('\033[31m' + "Proxy is working..." + '\033[0m')
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
    username_used = True
    while(username_used):
        headers = {"x-pm-apiversion" : "3", "x-pm-appversion" : "Web_3.16.33"}
        if proxy_option == "3":
            response = requests.get(f"https://mail.protonmail.com/api/users/available?Name={rngusername}", timeout=3.5, headers=headers)
        else:
            response = requests.get(f"https://mail.protonmail.com/api/users/available?Name={rngusername}", proxies=proxies_file, timeout=3.5, headers=headers)
        if "1000" in response.text:
            username_used = False
        else:
            rngusername = randomStringDigits(13)
    is_site_loading = True
    while(is_site_loading):
        try:
            driver.set_page_load_timeout(10)
            driver.get(url)
            if "Select Your ProtonMail Account Type" in driver.page_source:
                is_site_loading = False

        except (WebDriverException, TimeoutException) as e:
            driver.close()
            proxy_from_file = "false"
            while (proxy_from_file == "false"):
                if i is len(proxy_lines):
                    print("You reached the end of the proxy list")
                    time.sleep(5)
                    exit(0)
                i += 1
                print('\033[31m' + proxy_lines[i] + '\033[0m')
                try:
                    proxies_file = {'http': 'http://:@{}/'.format(proxy_lines[i])}
                    requests.get("http://protonmail.com/", proxies=proxies_file, timeout=10.5)
                except OSError:
                    print('\033[31m' + "Proxy Connection error!" + '\033[0m')
                    proxy_from_file = "false"
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                else:
                    print('\033[31m' + "Proxy is working..." + '\033[0m')
                    options = Options()
                    options.add_argument('--proxy-server={}'.format(proxy_lines[i]))
                    driver = webdriver.Chrome(executable_path='./driver/chromedriver', chrome_options=options)
                    proxy_from_file = "true"
                    proxy_option


    time.sleep(4)

    driver.find_element_by_class_name('panel-heading').click()

    time.sleep(1)

    driver.find_element_by_id('freePlan').click()

    time.sleep(4)

    driver.switch_to.frame(0)

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
    print('\033[31m' + "(1) Automatic Email verification" + '\033[0m')
    print('\033[31m' + "(2) Manual Email verification" + '\033[0m')
    print('\033[31m' + "(3) Captcha verification" + '\033[0m')
    verifymethod = input('\033[31m' + "Pick an verification option: " + '\033[0m')
    if verifymethod == "1":
        get_response = requests.get("https://lazy-mail.com/mailbox/create/random")
        csrf_token = get_response.text.split("input type=\"hidden\" name=\"_token\" value=\"")[1].split("\"")[0]
        post_data = {"_token": csrf_token}
        post_response = requests.post("https://lazy-mail.com/mailbox/create/random", data=post_data,cookies=get_response.cookies)
        generated_email = post_response.url.split("mailbox/")[1]

        driver.find_element_by_id('id-signup-radio-email').click()

        time.sleep(1)

        driver.find_element_by_id('emailVerification').send_keys(generated_email)

        time.sleep(1)

        driver.find_element_by_class_name('codeVerificator-btn-send').click()

        time.sleep(3)
        while (True):
            get_emails = requests.get("https://lazy-mail.com/mail/fetch?new=true", cookies=post_response.cookies)
            get_emails = requests.get("https://lazy-mail.com/mail/fetch", cookies=post_response.cookies)
            if "ProtonMail" not in get_emails.text:
                time.sleep(10)
            else:
                get_code = get_emails.text.split("ext\":\"Your Proton verification code is:<br\/>")[1].split("\"")[0]
                break
        driver.find_element_by_id('codeValue').send_keys(get_code)
        driver.find_element_by_css_selector(".humanVerification-completeSetup-create").click()
        time.sleep(5)

    if verifymethod == "2":
        driver.find_element_by_id('id-signup-radio-email').click()

        time.sleep(1)

        driver.find_element_by_id('emailVerification').send_keys(verifymail)

        time.sleep(1)

        driver.find_element_by_class_name('codeVerificator-btn-send').click()

        time.sleep(3)
    elif verifymethod == "3":
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
            csvData = [[rngusername + '@protonmail.com', rngpassword, generated_email]]
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

        else:
            print ('\033[31m' + "Ok! The script is exiting now." + '\033[0m')
            time.sleep(1)
            exit()
