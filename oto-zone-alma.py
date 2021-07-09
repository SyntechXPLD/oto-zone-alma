import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("#######################################################")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("            OTO ZONE ALMA ARAÇI B3ZKURT                ")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("#######################################################")
print()

username = input("Zone Alıncak İsim: ")

password = input("Siteyi Giriniz: ")
class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def singIn(self):
         self.browser.get("https://mirror-h.org/site-send")
         time.sleep(2)

         usernameInput = self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div/form/div[1]/input")
         passwordInput = self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div/form/div[2]/input")

         usernameInput.send_keys(self.username)
         passwordInput.send_keys(self.password)
         passwordInput.send_keys(Keys.ENTER)
         time.sleep(2)

    def dm(self):
        dm = self.browser.get("https://mirror-h.org/")
        dm.click()

instgrm = Instagram(username, password)
instgrm.singIn()
instgrm.dm()
