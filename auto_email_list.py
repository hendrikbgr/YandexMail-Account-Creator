# 🚀 This Project is in it's early stages of Development.
# 📌 Working on new features and main menu.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 1.0.2

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
import os
import twocaptcha as captcha
import warnings
import zipfile
import time
import random
from random import choice
import string
import requests
import csv
from proxyscrape import create_collector
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException, InvalidSessionIdException, TimeoutException
import undetected_chromedriver as uc
from faker import Faker
import captcha_config
import proxy_config
clear = lambda: os.system('clear')
clear()
i = 0
collector = create_collector('my-collector', 'https')

print ('\033[31m' + """\
    __  ___      _ __
   /  |/  /___ _(_) /
  / /|_/ / __ `/ / / 
 / /  / / /_/ / / /  
/_/  /_/\__,_/_/_/   
                                                      
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
proxynum = 0
for proxy in proxy_config.proxy:
    # Pick an email for Verification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    verifymail = "x"

    # Pick an email for Notification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
    notifymail = ""
    proxy = proxy_config.proxy[proxynum].split(":")
    PROXY_HOST = proxy[0]
    PROXY_PORT = proxy[1]
    PROXY_USER = proxy[2]
    PROXY_PASS = proxy[3]

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
    
    uc.install(
        executable_path='driver/chromedriver.exe',
    )
    options = uc.ChromeOptions()
    pluginfile = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    options.add_extension(pluginfile)
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile': {
            'password_manager_enabled': False
        }
    })
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-web-security")
    viewport = ['2560,1440', '1920,1080', '1440,900']
    options.add_argument(f"--window-size={choice(viewport)}")
    options.add_argument("--log-level=3")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = uc.Chrome(options=options)
    print('\033[92m' + 'Proxy: ' + '\033[92m', proxylist[proxynum])

    warnings.filterwarnings("ignore", category=DeprecationWarning) 

    # Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)

    url = 'https://passport.yandex.com/registration'

    fake = Faker()
    rngusername = f'{fake.unique.first_name()}{random.randint(100000,999999)}'
    rngpassword = f'{random.randint(10000,99999)}{fake.unique.first_name()}{random.randint(10000,99999)}'
    fakeFirstName = f'{fake.unique.first_name()}'
    fakeLastName = f'{fake.unique.last_name()}'
    birthMonth = f'{random.randint(1,12)}'
    birthDay = f'{random.randint(1,28)}'
    birthYear = f'{random.randint(1960,2000)}'

    def randomStringDigits(stringLength=6):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

    is_site_loading = True
    site_loaded = 'success'

    while(is_site_loading):
        try:
            driver.get(url)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            time.sleep(5)
            loading_yes = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/div/h1')
            is_site_loading = False

        except (NoSuchElementException, WebDriverException, InvalidSessionIdException) as e:
            proxynum += 1
            site_loaded = 'false'
            is_site_loading = False
    if site_loaded == 'success':
        
        # Username pick
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[3]/span/input').send_keys(rngusername)

        time.sleep(1)
        
        time.sleep(1)
        # First and Last name pick
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[1]/span/input').send_keys(fakeFirstName)
        
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[2]/span[1]/input').send_keys(fakeLastName)

        time.sleep(1)

        # Password pick
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[2]/div[1]/span/input').send_keys(rngpassword)

        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[2]/div[2]/span/input').send_keys(rngpassword)

        time.sleep(1)
        
        # Password recovery pick
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[1]/span').click()

        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div[2]/span/input').send_keys(rngusername)


        time.sleep(1)

        time.sleep(6)

        print('Using ' + captcha.__name__ + ' version: ' + str(captcha.__version__) + ' loaded from ' + str(captcha.__path__))
        solver = captcha.TwoCaptcha(captcha_config.key)
        
        print('Solver has attribute normal: ' + str(hasattr(solver,'normal')))
        print('Attribute normal is callbable: ' + str(callable(getattr(solver, 'normal'))))
        img = driver.find_element_by_class_name("captcha__image")
        src = img.get_attribute('src')
        img = requests.get(src)
        with open('captcha.jpg', 'wb') as f:
            f.write(img.content)
        
        try:
            result = solver.normal('captcha.jpg') # change to your image path
        
        except Exception as e:
            print(e)
        
        else:
            print('solved: ' + str(result))
        finalResult = str(result['code'])
        os.remove('captcha.jpg')
        print('\033[92m' + 'ReCapchta Success! Now signing up...' + '\033[92m')
        time.sleep(1)
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button').click()
        except (NoSuchElementException, WebDriverException, InvalidSessionIdException) as e:
            pass

        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div[1]/span/input').send_keys(finalResult)

        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/span/button').click()

        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/div/div[2]/div/button').click()

        print ('\033[31m' + "Your New Email Adress is: ", rngusername,"@yandex.com", sep='' + '\033[0m')
        print ('\033[31m' + "Your New Email Password is: "  + '\033[0m' , rngpassword)
        print ('\033[31m' + "Your New First Name is: "  + '\033[0m' , fakeFirstName)
        print ('\033[31m' + "Your New Last Name is: "  + '\033[0m' , fakeLastName)

        csvData = [[rngusername + '@yandex.com', rngpassword, fakeFirstName, fakeLastName]]
        with open('list.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csvData)
        csvFile.close()
        print ('\033[31m' + 'Great! We added you account details to the table.' + '\033[0m')
        proxynum += 1
        time.sleep(8)
        driver.close()
        '''except (NoSuchElementException, WebDriverException) as e:
            proxynum += 1
            driver.close()
            print ('\033[31m' + 'No Recapchta possible...' + '\033[0m')
            print ('\033[31m' + 'Trying next proxy...' + '\033[0m')
            time.sleep(5)
        '''
    else:
        print ('\033[31m' + 'Trying next proxy...' + '\033[0m')
