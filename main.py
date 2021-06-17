from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

launcher = webdriver.Chrome()
launcher.get('https://web.whatsapp.com/')
input('Please scan the QR code on the browser. Press enter here after you\'ve successfully loggin in')

def sendDocument(name, messageBody, filepath):
    searchBox = launcher.find_element_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir = "ltr"]')
    time.sleep(2)
    searchBox.send_keys(name + Keys.ENTER)

    recipient = launcher.find_element_by_xpath(f'//span[@title = "{name}"]')
    recipient.click()

    attachmentIcon =  launcher.find_element_by_xpath(f'//span[@data-testid = "clip"][@data-icon="clip"]')
    attachmentIcon.click()

    documentIcon =  launcher.find_element_by_xpath(f'//input[@accept="*"][@type="file"]')
    documentIcon.send_keys(filepath)

    time.sleep(2)
    sendButton =  launcher.find_element_by_xpath(f'//span[@data-testid="send"]')
    sendButton.click()

def sendMessage(name, message):
    searchBox = launcher.find_element_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir = "ltr"]')
    time.sleep(2)
    searchBox.send_keys(name + Keys.ENTER)

    recipient = launcher.find_element_by_xpath(f'//span[@title = "{name}"]')
    recipient.click()
    time.sleep(2)
    inputBox = launcher.find_element_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"][@spellcheck="true"]')
    inputBox.send_keys(message + Keys.ENTER)

n = "Ting"
filepath = "C:\\CARDINAL\\NUS My Notes\\NUS Archive\\Year 1 Sem 2\\MA1101R 2019\\ma1101r-zhoufeng.pdf"
message = "Can I annoy you hehe"

for i in range(0, 20):
    sendMessage(n, message)
# sendDocument(n, "Love you lots", filepath)



