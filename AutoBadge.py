from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
duo_wait = 60

#Credentials - Plain Text!
username = """JoeGaucho"""
pw = """password123"""

#XPaths
LOGIN_BUTTON = """/html/body/div[4]/div/div[2]/form/div[2]/input[1]"""
NETID = """/html/body/main/div/div[1]/div/div/div[2]/form/section[1]/div/input"""
PASSWORD = """/html/body/main/div/div[1]/div/div/div[2]/form/section[2]/div/input"""
SUBMIT_BUTTON = """/html/body/main/div/div[1]/div/div/div[2]/form/input[4]"""
SHS_BRAND = """navbar-brand"""
COMPLETE_SURVEY = """/html/body/div[4]/div/div[2]/form/div[3]/div/a"""
SURVEY_CONTINUE = """/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/a"""
Q1 = """/html/body/div[2]/div/div[2]/main/form/div[2]/fieldset/div/div[2]/div"""
Q2 = """/html/body/div[2]/div/div[2]/main/form/div[3]/fieldset/div/div[2]/div"""
Q3 = """/html/body/div[2]/div/div[2]/main/form/div[4]/fieldset/div/div[2]/div"""
Q4 = """/html/body/div[2]/div/div[2]/main/form/div[5]/fieldset/div/div[2]/div"""
Q5 = """/html/body/div[2]/div/div[2]/main/form/div[6]/fieldset/div/div[2]/div"""
SUBMIT_SURVEY = """/html/body/div[2]/div/div[2]/footer/div/div[2]/input"""
SHOW_BADGE = """/html/body/div[4]/div/div[2]/form/div[2]/div/div/button"""

driver = webdriver.Chrome()
driver.get('https://studenthealthoc.sa.ucsb.edu/login_dualauthentication.aspx')

driver.find_element_by_xpath(LOGIN_BUTTON).click()

emailField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, NETID)))

#UCSB_SSO
emailField.send_keys(username)
passwordField = driver.find_element_by_xpath(PASSWORD)
passwordField.send_keys(pw)
driver.find_element_by_xpath(SUBMIT_BUTTON).click()

#jump to survey page while waiting for 2FA
WebDriverWait(driver, duo_wait).until(EC.presence_of_element_located((By.XPATH, COMPLETE_SURVEY))).click()
#driver.find_element_by_xpath(COMPLETE_SURVEY).click()
driver.find_element_by_xpath(SURVEY_CONTINUE).click()

#Find survey buttons and click
driver.find_element_by_xpath(Q1).click()
driver.find_element_by_xpath(Q2).click()
driver.find_element_by_xpath(Q3).click()
driver.find_element_by_xpath(Q4).click()
driver.find_element_by_xpath(Q5).click()
driver.find_element_by_xpath(SUBMIT_SURVEY).click()

#Verify Success and show badge
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, SHOW_BADGE))).click()

#check your email for the badge