import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


email = 'yiyig64464@teasya.com'
password = 'throwaway12345'

target_url = 'https://www.hackerrank.com/auth/login'
dash_url = 'https://www.hackerrank.com/dashboard'


chrome_options = Options()

# chrome_options.add_argument('--headless')
# user_agent = 'user-agent= Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'    
# chrome_options.add_argument(user_agent)

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get(target_url)

# Needed to use Googles DevTools (Inspect) to find unique general locators (name, id, class) of the username/password fields.
# Used send_keys to input email/password into text fields.
driver.find_element(By.ID, 'input-1').send_keys(email) 
driver.find_element(By.ID, 'input-2').send_keys(password)

"""
Used XPATH due to the submit button not having any unique identifiers. 
XPATH standard syntax: 'Xpath = //tagname[@attribute='value']'
There are several ways of finding the element with XPATH. Easiest is to just right click the element and select copy fullXPATH.
Other examples: '//*[contains(text(),"Log In")]', '//span[. = "Log In"]'
"""
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[4]/button/div/span").click()
time.sleep(3) # Time for the login to redirect

driver.get('https://www.hackerrank.com/settings/account')
time.sleep(3)

# Collect some data
# topics = driver.find_elements(By.CLASS_NAME, 'topic-name')
# topic_list = []


# for t in topics:
#     topic_list.append(t.text)
# print(topic_list)

driver.close()