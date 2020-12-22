from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import main


def whatsapp():


    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com/')
    main.Goverbal('Enter the name of user or group : ')
    name =main.Input()                                          
    main.Goverbal('Enter your message : ') 
    msg = main.Input()
          

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(0):
       msg_box.send_keys(msg)
       button = driver.find_element_by_class_name('_3M-N-')
       button.click()