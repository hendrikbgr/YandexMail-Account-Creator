# 🚀 This Project is in it's early stages of Development.
# 📌 Working on new features and main menu.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 0.1 Beta

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys,os,warnings,zipfile,time,random,string,requests,csv,captcha_config,proxy_config
import twocaptcha as captcha
from random import choice
from proxyscrape import create_collector
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException, InvalidSessionIdException, TimeoutException
import undetected_chromedriver as uc
from faker import Faker
import captcha_config
import proxy_config
from plugin_config import manifest_json, background_js


def clear():
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c') #clearing the screen

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

for proxy in proxy_config.proxy:

    proxy_split = proxy.split(":")
    PROXY_HOST = proxy_split[0]
    PROXY_PORT = proxy_split[1]
    PROXY_USER = proxy_split[2]
    PROXY_PASS = proxy_split[3]

    uc.install(
        executable_path='chromedriver.exe',
    )
    options = uc.ChromeOptions()
    pluginfile = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS))
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
    print('\033[92m' + 'Proxy: ' + '\033[92m', proxy)

    warnings.filterwarnings("ignore", category=DeprecationWarning)

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
            site_loaded = 'false'
            is_site_loading = False
    if site_loaded == 'success':

        # Username pick
        driver.find_element_by_xpath('//*[@id="login"]').send_keys(rngusername)

        time.sleep(1)

        time.sleep(1)
        # First and Last name pick
        driver.find_element_by_xpath('//*[@id="firstname"]').send_keys(fakeFirstName)

        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="lastname"]').send_keys(fakeLastName)

        time.sleep(1)

        # Password pick
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(rngpassword)

        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="password_confirm"]').send_keys(rngpassword)

        time.sleep(1)

        # Password recovery pick
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[1]/span').click()

        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div[2]/span/input').send_keys(rngusername)


        time.sleep(1)

        time.sleep(6)
        solver = captcha.TwoCaptcha(captcha_config.key)

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
            pass
        finalResult = str(result['code'])
        os.remove('captcha.jpg')
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
        time.sleep(8)
        driver.close()
        '''except (NoSuchElementException, WebDriverException) as e:
            driver.close()
            print ('\033[31m' + 'No Recapchta possible...' + '\033[0m')
            print ('\033[31m' + 'Trying next proxy...' + '\033[0m')
            time.sleep(5)
        '''
    else:
        print ('\033[31m' + 'Trying next proxy...' + '\033[0m')
