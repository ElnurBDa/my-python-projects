from selenium import webdriver
from time import sleep

brow = webdriver.Chrome(executable_path='chromedriver.exe')
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x',
        'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V',
        'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for x1 in keys:
    for x2 in keys:
        for x3 in keys:
            for x4 in keys:
                try:
                    kod = '3yS8pFNp2s' + x1 + x2 + x3 + x4
                    brow.get('https://monitoring.e-kassa.gov.az/#/index')
                    X = brow.find_element_by_xpath(
                        '//*[@id="root"]/div/section/main/div/div/div[1]/form/div/div/div/input')
                    X.click()
                    X.send_keys(kod)
                    B = brow.find_element_by_xpath(
                        '//*[@id="root"]/div/section/main/div/div/div[1]/form/div/div/button/span[1]')
                    B.click()
                    X.click()
                    try:
                        sleep(0.01)
                        E = brow.find_element_by_xpath('//*[@id="root"]/div/section/main/div/div/div[2]/div[1]/button')
                        E.click()
                        print('Lucky')
                    except:
                        pass
                except:
                    print('err ' + x1 + x2)
