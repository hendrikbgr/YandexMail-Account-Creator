# 🚀 This Project is in it's early stages of Development.
# 📌 Working on new features and main menu.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 0.1 Beta

import csv
import os
import platform
import random
import string
import subprocess
import sys
import warnings
import zipfile
from random import choice, uniform
from time import sleep

import requests
import undetected_chromedriver as uc
from fake_headers import Headers
from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import (InvalidSessionIdException,
                                        NoSuchElementException,
                                        WebDriverException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from twocaptcha import TwoCaptcha

import captcha_config
import proxy_config
from plugin_config import background_js, manifest_json


def clear():
    # clearing the screen
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


clear()
i = 0

print('\033[31m' + """\
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

print('\033[31m' + "Auto Account Creator Script" + '\033[0m')

print('\033[92m' + "Getting Chrome driver..." + '\033[0m')

OSNAME = platform.system()

if OSNAME == 'Linux':
    OSNAME = 'lin'
    with subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE) as proc:
        version = proc.stdout.read().decode('utf-8').replace('Google Chrome', '').strip()
elif OSNAME == 'Darwin':
    OSNAME = 'mac'
    process = subprocess.Popen(
        ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
    version = process.communicate()[0].decode(
        'UTF-8').replace('Google Chrome', '').strip()
elif OSNAME == 'Windows':
    OSNAME = 'win'
    process = subprocess.Popen(
        ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
    )
    version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
else:
    print('{} OS is not supported.'.format(OSNAME))
    sys.exit()

major_version = version.split('.')[0]

uc.TARGET_VERSION = major_version

uc.install()


def type_me(element, text):
    """
    Type like a human
    """
    for letter in text:
        element.send_keys(letter)
        sleep(uniform(.1, .3))


for proxy in proxy_config.proxy:

    proxy_split = proxy.split(":")
    PROXY_HOST = proxy_split[0]
    PROXY_PORT = proxy_split[1]
    PROXY_USER = proxy_split[2]
    PROXY_PASS = proxy_split[3]

    header = Headers(
        browser="chrome",
        os=OSNAME,
        headers=False
    ).generate()
    agent = header['User-Agent']

    options = webdriver.ChromeOptions()
    pluginfile = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js %
                    (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS))
    options.add_extension(pluginfile)
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
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
    options.add_argument(f"user-agent={agent}")
    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 40)

    print('\033[92m' + f'Proxy: {proxy}' + '\033[0m')

    warnings.filterwarnings("ignore", category=DeprecationWarning)

    url = 'https://passport.yandex.com/registration'

    fake = Faker()
    rngusername = f'{fake.unique.first_name()}{random.randint(100000,999999)}'
    recoveryname = f'{fake.unique.first_name()}{random.randint(100000,999999)}'
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
            driver.execute_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            sleep(5)
            loading_yes = driver.find_element_by_xpath(
                '/html/body/div/div/div[2]/div/main/div/div/div/div/h1')
            is_site_loading = False

        except (NoSuchElementException, WebDriverException, InvalidSessionIdException) as e:
            site_loaded = 'false'
            is_site_loading = False

    if site_loaded == 'success':

        # Username pick
        user = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="login"]')))
        type_me(user, rngusername)

        # First and Last name pick
        first = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="firstname"]')))
        type_me(first, fakeFirstName)

        last = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="lastname"]')))
        type_me(last, fakeLastName)

        # Password pick
        password = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="password"]')))
        type_me(password, rngpassword)

        confirm = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="password_confirm"]')))
        type_me(confirm, rngpassword)

        # Password recovery pick
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[1]/span'))).click()

        recovery = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div[2]/span/input')))
        type_me(recovery, recoveryname)

        solver = TwoCaptcha(captcha_config.key)

        img = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'captcha__image')))
        src = img.get_attribute('src')
        img = requests.get(src)
        with open('captcha.jpg', 'wb') as f:
            f.write(img.content)

        try:
            result = solver.normal('captcha.jpg')  # change to your image path

            finalResult = str(result['code'])
            os.remove('captcha.jpg')
            sleep(1)
            try:
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[2]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button'))).click()
            except (NoSuchElementException, WebDriverException, InvalidSessionIdException) as e:
                pass

            final = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div[1]/span/input')))
            type_me(final, finalResult)

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/span/button'))).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/div/div[2]/div/button'))).click()

            try:
                wait.until(EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'error-message')))

                print('\033[31m' + 'Wrong Recapchta ' + '\033[0m')
                print('\033[31m' + 'Trying next proxy...' + '\033[0m')
                sleep(5)
                driver.close()

            except:
                print('\033[31m' + "Your New Email Adress is: ",
                      rngusername, "@yandex.com", sep='' + '\033[0m')
                print('\033[31m' + "Your New Email Password is: " +
                      '\033[0m', rngpassword)
                print('\033[31m' + "Your New First Name is: " +
                      '\033[0m', fakeFirstName)
                print('\033[31m' + "Your New Last Name is: " +
                      '\033[0m', fakeLastName)

                csvData = [[rngusername + '@yandex.com', rngpassword,
                            fakeFirstName, fakeLastName, recoveryname]]
                with open('list.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(csvData)
                csvFile.close()
                print(
                    '\033[31m' + 'Great! We added you account details to the table.' + '\033[0m')
                sleep(8)
                driver.close()

        except Exception as e:
            print(str(e))
            print('\033[31m' + 'No Recapchta possible...' + '\033[0m')
            print('\033[31m' + 'Trying next proxy...' + '\033[0m')
            sleep(5)
            driver.close()
            pass

    else:
        print('\033[31m' + 'Trying next proxy...' + '\033[0m')
        os.remove('proxy_auth_plugin.zip')
