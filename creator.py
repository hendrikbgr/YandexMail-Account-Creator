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
import undetected_chromedriver.v2 as uc
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

import config
import proxy_config


def clear():
    # clearing the screen
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


clear()
i = 0
if __name__ == '__main__':
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


    def type_me(element, text):
        """
        Type like a human
        """
        for letter in text:
            element.send_keys(letter)
            sleep(uniform(.1, .3))


    for proxy in proxy_config.proxy:

        header = Headers(
            browser="chrome",
            os=OSNAME,
            headers=False
        ).generate()
        agent = header['User-Agent']

        options = uc.ChromeOptions()
        options.add_argument('--proxy-server=%s' % proxy)
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        prefs = {"credentials_enable_service": False,
                "profile.password_manager_enabled": False
                }
        options.add_experimental_option("prefs", prefs)
        driver = uc.Chrome(options=options)

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
            print(f'Loading: {url}')
            try:
                driver.get(url)
                driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                sleep(5)
                wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/span/button')))
                is_site_loading = False

            except (NoSuchElementException, WebDriverException, InvalidSessionIdException) as e:
                site_loaded = 'false'
                is_site_loading = False

        if site_loaded == 'success':
            print(f'{url} loaded Successfully')
            try:
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[2]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button'))).click()
            except (NoSuchElementException, WebDriverException, InvalidSessionIdException) as e:
                pass

            # Username pick
            print(f'Picking Username: {rngusername}')
            user = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="login"]')))
            type_me(user, rngusername)

            # First and Last name pick
            print(f'Picking First & Last Name: {fakeFirstName} {fakeLastName}')
            first = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="firstname"]')))
            type_me(first, fakeFirstName)

            last = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="lastname"]')))
            type_me(last, fakeLastName)

            # Password pick
            print(f'Picking Password: {rngpassword}')
            password = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="password"]')))
            type_me(password, rngpassword)

            confirm = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="password_confirm"]')))
            type_me(confirm, rngpassword)

            # Adding Phone number
            token = config.phonekey
            country = 'russia'
            operator = 'any'
            product = 'yandex'

            headers = {
                'Authorization': 'Bearer ' + token,
                'Accept': 'application/json',
            }
            response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers)
            activation_number = response.json()['phone']
            phone_id = response.json()['id']
            print(f'Picking Phone Number: {activation_number}')
            print(f'Phone Number ID: {phone_id}')
            

            phone = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/span/input')))
            type_me(phone, activation_number)
            sleep(5)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div/button'))).click()

            try:
                print('Waiting for Activation Code...')
                sleep(25)
                headers = {
                    'Authorization': 'Bearer ' + token,
                    'Accept': 'application/json',
                }

                response = requests.get('https://5sim.net/v1/user/check/' + str(phone_id), headers=headers)
                activation_code = response.json()['sms'][0]['code']
                print(f'Entering Activation Code: {activation_code}')

                code_input = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[2]/div[1]/span/input')))
                type_me(code_input, activation_code)

                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[4]/span/button'))).click()

                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[4]/div/div[2]/div/button'))).click()

                
                sleep(2)

            except Exception as e:
                print(str(e))
                print('\033[31m' + 'No Recapchta possible...' + '\033[0m')
                print('\033[31m' + 'Trying next proxy...' + '\033[0m')
                sleep(5)
                driver.close()
                pass

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[3]/span/a'))).click()

            # Open Passwords accordion
            print('Adding IMAP and POP3...')
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/main/div/div/div/div/div/div/div/div[4]/div[2]'))).click()

            sleep(5)

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div[2]/div[3]/main/div/div/div/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div/div[1]/div/span/span'))).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div/button'))).click()
            
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[1]/button'))).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/div[2]/div[2]/ul/li[1]/span[1]/span'))).click()

            appName = 'App for Imap'
            print(f'Picking Name for App: {appName}')
            final = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/div[2]/div[3]/div[1]/span/input')))
            type_me(final, appName)
            
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/div[2]/div[4]/div/div[1]/button'))).click()
            sleep(4)

            appPassword = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/div[2]/div[1]/div[1]/span'))).text
            
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/button'))).click()

            print('Going to Email Client Settings...')
            driver.get('https://mail.yandex.com/?dpda=yes#setup/client')

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[2]/div[7]/div/div[3]/div/div[2]/div/main/div[7]/div/div/div/div[2]/form/div/div[2]/div[1]/span/span/label/span[1]'))).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[2]/div[7]/div/div[3]/div/div[2]/div/main/div[7]/div/div/div/div[2]/form/div/div[3]/div[1]/span/span/label/span[1]'))).click() 

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[2]/div[7]/div/div[3]/div/div[2]/div/main/div[7]/div/div/div/div[2]/form/button/span/span'))).click()                   
            print('Finishing up...')
            sleep(1)
            print(f'Your New Email Address: {rngusername}@yandex.com')
            print(f'Your New Password: {rngpassword}')
            print(f'Your First & Last Name: {fakeFirstName} {fakeLastName}')
            print(f'Your Proxy used: {proxy}')
            print(f'Your Phone Number used: {activation_number}')
            print(f'Your Activation Code used: {activation_code}')
            csvData = [[rngusername + '@yandex.com', rngpassword, fakeFirstName, fakeLastName, recoveryname, proxy, appPassword, activation_number, phone_id]]
            with open('list.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(csvData)
            csvFile.close()

            sleep(5)

            driver.close()

        else:
            print('\033[31m' + 'Trying next proxy...' + '\033[0m')
            os.remove('proxy_auth_plugin.zip')
