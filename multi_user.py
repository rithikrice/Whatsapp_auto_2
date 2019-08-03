from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

all_names = ['Sachin Yadav']
msg = input('Enter the message')
count = int(input('no.of times to send message'))

input('click any random key after qr scanning')

for name in all_names:
    user = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
    user.click()

    msgbox = driver.find_element_by_class_name('_3u328')

    for i in range (count):
        msgbox.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()