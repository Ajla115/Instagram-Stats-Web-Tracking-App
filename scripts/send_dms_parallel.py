import mysql.connector
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

load_dotenv() # This will load env variables

# Connecting to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

mycursor = mydb.cursor()

def log_in(driver, ig_username, ig_password):
        USERNAME = ig_username
        PASSWORD = ig_password
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys(USERNAME)

        sleep(3)

        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        password_field.send_keys(PASSWORD)

        sleep(15)

        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
        login_button.click()

def get_instagram_username(recipients_id):
    query = "SELECT username FROM instagram_accounts WHERE id = %s"
    mycursor.execute(query, (recipients_id,))
    result = mycursor.fetchone()
    return result[0] if result else None

def check_username_exists(driver, username):
    insta_url = 'https://www.instagram.com/'
    driver.get(insta_url + username)
    try:
        check_title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/span'))
        )
        check_title_text = check_title_element.text
        if check_title_text == "Sorry, this page isn't available.":
            return False
        else:
             return True
    except:
        return -1

def check_if_logged_in(driver):
    try:
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        return False
    except TimeoutException:
        return True
    


def instagram_driver1(driver, username):
   
    sleep(3)

    check_login_results = check_if_logged_in(driver)
    print(check_login_results)

    if check_login_results == False:
        log_in(driver, os.environ['IGUSERNAME1'], os.environ['IGPASSWORD1'])

    sleep(7)

    #print(check_username_exists(driver, username))

    if  not (check_username_exists(driver, username)):
            return False
    #if the username does not exist, just exit
    
    #if username exists, send a DM to it
    
    driver.get('https://www.instagram.com/direct/inbox/')

    sleep(3)

    # turn_on_notifications_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div'))
    # )
    # turn_on_notifications_button.click()
    # sleep(3)


    message_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div')))
    message_button.click()

    sleep(7)

    enter_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input'))
    )
    enter_name.click()
    enter_name.send_keys(username)

    sleep(15)

    choose_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input')))
    choose_name.click()

    sleep(15)

    chat_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')))
    chat_button.click()

    sleep(7)

    message_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')))
    message_field.send_keys("Automated message.")

    sleep(7)

    send_message_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]')))
    send_message_button.click()

    sleep(5)

    driver.quit()



def instagram_driver2(driver, username):
    sleep(3)

    check_login_results = check_if_logged_in(driver)
    print(check_login_results)

    if check_login_results == False:
        log_in(driver, os.environ['IGUSERNAME2'], os.environ['IGPASSWORD2'])

    sleep(7)

    #print(check_username_exists(driver, username))

    if  not (check_username_exists(driver, username)):
            return False
    #if the username does not exist, just exit
    
    #if username exists, send a DM to it
    
    driver.get('https://www.instagram.com/direct/inbox/')

    sleep(15)

    # turn_on_notifications_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div'))
    # )
    # turn_on_notifications_button.click()
    # sleep(3)

    

    message_button = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]')))
    message_button.click()

    sleep(7)

    enter_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input'))
    )
    enter_name.click()
    enter_name.send_keys(username)

    sleep(15)

    choose_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input')))
    choose_name.click()

    sleep(15)

    chat_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')))
    chat_button.click()

    sleep(7)

    message_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')))
    message_field.send_keys("Automated message.")

    sleep(7)

    send_message_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]')))
    send_message_button.click()

    sleep(5)

    driver.quit()

def main():

    # Update paths to your local ChromeDriver binary
    service = Service(executable_path="/path/to/chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--user-data-dir=/path/to/selenium/ChromeProfile9222')

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    service2 = Service(executable_path="/path/to/chromedriver")
    options2 = webdriver.ChromeOptions()
    options2.add_argument('--remote-debugging-port=9227')
    options2.add_argument('--user-data-dir=/path/to/selenium/ChromeProfile9227')

    driver2 = webdriver.Chrome(service=service2, options=options2)
    driver2.maximize_window()

    insta_url = 'https://www.instagram.com/'
    driver.get(insta_url)
    driver2.get(insta_url)

    instagram_driver1(driver, 'target_username_1')
    instagram_driver2(driver2, 'target_username_2')

if __name__ == "__main__":

    main()
