from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

site = "https://web.whatsapp.com/"
user="SomeOne"
emo="clown"

browser = webdriver.Edge()
browser.maximize_window()
browser.get(site)

input("Waiting")
browser.find_element(By.XPATH, '//span[@title="'+user+'"]').click()

input("Waiting")
while 1:
	for e in browser.find_elements(By.XPATH, '//div[@class="_2_-To"]'):# при случае ошибки чекнуть эти элементы
		try:
			e.click()
			sleep(.3)
			browser.find_element(By.XPATH, '//span[@data-testid="react"]').click()
			sleep(.3)
			browser.find_element(By.XPATH, '//div[@aria-label="More reactions"]').click()
			sleep(.3)
			browser.find_element(By.XPATH, '//input[@data-testid="input-emoji-search"]').send_keys(emo)
			sleep(.3)
			browser.find_element(By.XPATH, '//input[@data-testid="input-emoji-search"]').send_keys(Keys.ENTER)
			sleep(.3)
		except:
			print("smth is wrong")
	again = input("again?(enter no to break the loop)")
	if again == "no": break
	emo=input("Enter the name of emodzi") or emo

input("Waiting")