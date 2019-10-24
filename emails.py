# 🚀 This Project is in it's early stages of Development. I am planning on adding a random username and password script which prints out username and password into a text file
# 📌 Also I am working on a way to auto verfiy account via 10min mail api.
# ⚠️ Any Questions or Suggestions please Mail to: hendriksdevmail@gmail.com
# 🖥 Version: 0.1

from selenium import webdriver
from colorama import Fore, Back, Style
import time
import random
import string

from selenium.webdriver.chrome.options import Options 

options = Options()
options.add_argument('--proxy-server=51.79.140.77:8080') # <-- Enter your Proxy here [Proxy:Port]
driver = webdriver.Chrome(executable_path='/Users/hendrik/Development/protonMailGenerator/chromedriver', chrome_options=options)

url = 'https://protonmail.com/signup'

def randomStringDigits(stringLength=13):
    # Generate a random string of letters and digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

rngusername = randomStringDigits(13)
rngpassword = randomStringDigits(15)

# Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)
driver.get(url)

time.sleep(4)

driver.find_element_by_class_name('panel-heading').click()

time.sleep(3)

driver.find_element_by_id('freePlan').click()

time.sleep(3)

driver.switch_to_frame(0)

time.sleep(2)

# Pick your username and replace it with 'YourUsername'
driver.find_element_by_id('username').send_keys(rngusername)

time.sleep(1)

driver.switch_to.default_content()

time.sleep(1)

# Pick your password and replace it with 'YourPassword'
driver.find_element_by_id('password').send_keys(rngpassword)

time.sleep(1)

# Pick your password and replace it with 'YourPassword' (Make sure to use the same password)
driver.find_element_by_id('passwordc').send_keys(rngpassword)

time.sleep(1)

driver.switch_to_frame(1)

time.sleep(1)

# Pick an email for Recovery. Replace 'YourEmail@Mail.com' with your email adress.
driver.find_element_by_id('notificationEmail').send_keys('YourEmail@Mail.com')

time.sleep(1)

driver.find_element_by_name('submitBtn').click()

time.sleep(3)

driver.find_element_by_id('id-signup-radio-email').click()

time.sleep(1)

# Pick an email for Verification. Replace 'YourEmail@Mail.com' with an email adress. (You can use 10min mail for this)
driver.find_element_by_id('emailVerification').send_keys('YourEmail@Mail.com')

time.sleep(1)

driver.find_element_by_class_name('codeVerificator-btn-send').click()

time.sleep(3)

print ('\033[31m' + "Your New Email Adress is: ", rngusername,"@protonmail.com", sep='' + '\033[0m')
print ('\033[31m' + "Your New Email Password is: ", rngpassword + '\033[0m')

