from selenium import webdriver
import time
brow=webdriver.Chrome(executable_path='chromedriver.exe')

brow.get('http://web.whatsapp.com')

time.sleep(5)
print('all correct!')
user='Elnur'
num=237


X=brow.find_element_by_xpath('//span[@title="{}"]'.format(user))
X.click()



msg_box=brow.find_element_by_xpath('//div[@spellcheck="true"]')
for x in range(1,num+1):
    msg_box.click()
    msg_box.send_keys(str(x)+') Машка')
    brow.find_element_by_xpath('//button[@class="_35EW6"]').click()




