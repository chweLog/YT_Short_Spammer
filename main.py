from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import string
import random

email = "" #Your email
password = "" #Your password
url = "" #Shorts url

def pick(_LENGTH):

    string_pool = string.ascii_letters + string.digits

    result = "" 
    for i in range(_LENGTH) :
        result += random.choice(string_pool)

    return result

if  __name__  ==  "__main__" :
    #settings
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = uc.Chrome(chrome_options=chrome_options)

    #Login
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="buttons"]/ytd-button-renderer'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierId"]'))
    ).send_keys(email)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    ).send_keys(password)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="passwordNext"]/div/button'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="comments-button"]/ytd-button-renderer/a'))
    ).click()
    while True:
        driver.delete_all_cookies()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="placeholder-area"]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="contenteditable-root"]'))
        ).send_keys(pick(5))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="submit-button"]/a'))
        ).click()    