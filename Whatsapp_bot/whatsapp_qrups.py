#Требует обновления

#Invalid proq


from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://web.whatsapp.com')

name = 'Купчиха'
qrup_name='Группа'
count=18
input('...')


for i in range(1,count+1):
    step_1 = driver.find_element_by_xpath('//span[@data-icon="menu"]')
    step_1.click()
    step_2 = driver.find_element_by_xpath('//div[@title="New group"]')#title="New group"
    step_2.click()
    time.sleep(0.2)
    step_3_msg = driver.find_element_by_xpath('//input[@class="_17ePo copyable-text selectable-text"]')
    step_3_msg.send_keys(name)
    time.sleep(0.2)
    step_4 = driver.find_element_by_xpath('//div[@class="_3CneP"]')
    step_4.click()
    time.sleep(0.2)
    step_3_msg.send_keys('\n')
    time.sleep(0.2)
    step_6_msg = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    step_6_msg.send_keys(qrup_name+str(i)+'ая \n')
    time.sleep(0.2)












