# 🚀 This Project is in it's early stages of Development.
# 📌 Also I am working on a way to auto verfiy account via 10min mail api.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 0.3

from selenium import webdriver
from colorama import Fore, Back, Style
import warnings
import time
import random
import string
import urllib.request
import requests
from proxyscrape import create_collector

collector = create_collector('my-collector', 'http')

# Retrieve only 'us' proxies
proxygrab = collector.get_proxy({'code': 'us'})
proxy = ("{}:{}".format(proxygrab.host, proxygrab.port))
print ('\033[31m' + "Proxy:", proxy + '\033[0m')

try:
    proxy_host = proxygrab.host
    proxy_port = proxygrab.port
    proxy_auth = ":"
    proxies = {'http':'http://{}@{}:{}/'.format(proxy_auth, proxy_host, proxy_port)}
    requests.get("http://example.org", proxies=proxies, timeout=3.05)

except OSError:
    print ('\033[31m' + "Proxy Connection error!" + '\033[0m')
    print ('\033[31m' + "Please restart script..." + '\033[0m')
    exit()
else:
    print ('\033[31m' + "Proxy is working..." + '\033[0m')

from selenium.webdriver.chrome.options import Options 

warnings.filterwarnings("ignore", category=DeprecationWarning) 

options = Options()
options.add_argument('--proxy-server={}'.format(proxy)) # <-- Enter your Proxy here [Proxy:Port]

# Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)
driver = webdriver.Chrome(executable_path='/Users/hendrik/Development/ProtonMail-Account-Creator/driver/chromedriver', chrome_options=options)

print ('\033[31m' + "ProtonMail Account Creator is Starting..." + '\033[0m')

url = 'https://protonmail.com/signup'

def randomStringDigits(stringLength=13):
    # Generate a random string of letters and digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

rngusername = randomStringDigits(13)
rngpassword = randomStringDigits(15)

# Pick an email for Verification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
verifymail = "YourEmail@Mail.com"

# Pick an email for Notification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
notifymail = "YourEmail@Mail.com"

driver.get(url)

time.sleep(15)

driver.find_element_by_class_name('panel-heading').click()

time.sleep(4)

driver.find_element_by_id('freePlan').click()

time.sleep(3)

driver.switch_to_frame(0)

time.sleep(2)

driver.find_element_by_id('username').send_keys(rngusername)

print ('\033[31m' + "Used ", rngusername,"as Username" + '\033[0m')

time.sleep(1)

driver.switch_to.default_content()

time.sleep(1)

driver.find_element_by_id('password').send_keys(rngpassword)

time.sleep(1)

driver.find_element_by_id('passwordc').send_keys(rngpassword)

print ('\033[31m' + "Used ", rngpassword,"as Password" + '\033[0m')

time.sleep(1)

driver.switch_to_frame(1)

time.sleep(1)

# Pick an email for Recovery. Replace 'YourEmail@Mail.com' with your email adress.
driver.find_element_by_id('notificationEmail').send_keys(notifymail)

time.sleep(1)

driver.find_element_by_name('submitBtn').click()

time.sleep(6)

driver.find_element_by_id('id-signup-radio-email').click()

time.sleep(1)

driver.find_element_by_id('emailVerification').send_keys(verifymail)

print ('\033[31m' + "Send the Verification Code to: ", verifymail + '\033[0m')

time.sleep(1)

driver.find_element_by_class_name('codeVerificator-btn-send').click()

time.sleep(3)

print ('\033[31m' + "Your New Email Adress is: ", rngusername,"@protonmail.com", sep='' + '\033[0m')
print ('\033[31m' + "Your New Email Password is: ", rngpassword + '\033[0m')
print ('\033[31m' + "Enter Verification Code and Click 'Complete Setup'" + '\033[0m')
