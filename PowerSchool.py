import os
import time
from openpyxl import Workbook
import datetime
import shutil
import datetime
from pathlib import Path
import sys
import sys
import random
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def change(word, dic):
    list_word = list(word)
    changed_word = ''
    for c in list_word:
        changed_word += dic[c] 
    return changed_word
  
def unchange(word, dic):
    list_word = list(word)
    list_for_unchanged = []
    for c in list_word:
        for key, value in dic.items():
            if value == c:      
                list_for_unchanged.append(key)
    unchanged_word = ''
    for ele in list_for_unchanged:
        unchanged_word += ele
    return unchanged_word
 
def create_dict_key():
    list_of_char = []
    for i in range(33, 127):
        print(str(i) + ': ' + chr(i))
        list_of_char.append(chr(i))
        
    random.shuffle(list_of_char)
    dict_key = {}
    for i in range(len(list_of_char)):
        dict_key[chr(i+33)] = list_of_char.pop()
    return dict_key
       

dict_chr_to_chr = {'!': '/', '"': 'n', '#': 'A', '$': 'R', '%': 'Q', '&': '=', "'": ';', '(': ',', ')': 'L', '*': 'S', '+': 'U', ',': 'C', '-': 'r', '.': 'v', '/': '<', '0': 'p', '1': '*', '2': '!', '3': '%', '4': 'Z', '5': 'x', '6': '\\', '7': 't', '8': 'b', '9': 'T', ':': 'e', ';': 'q', '<': '_', '=': 's', '>': '$', '?': '{', '@': '>', 'A': 'w', 'B': 'I', 'C': 'l', 'D': '-', 'E': 'd', 'F': 'j', 'G': 'F', 'H': 'y', 'I': '2', 'J': 'Y', 'K': 'D', 'L': 'm', 'M': 'c', 'N': '|', 'O': 'E', 'P': '8', 'Q': '?', 'R': 'M', 'S': 'O', 'T': '}', 'U': '.', 'V': '4', 'W': ':', 'X': ')', 'Y': 'a', 'Z': '7', '[': 'k', '\\': 'W', ']': '3', '^': '^', '_': '1', '`': 'h', 'a': 'H', 'b': '[', 'c': 'u', 'd': '`', 'e': '0', 'f': 'z', 'g': '"', 'h': '@', 'i': 'f', 'j': '~', 'k': 'G', 'l': 'i', 'm': '5', 'n': '&', 'o': '6', 'p': 'B', 'q': 'J', 'r': 'V', 's': '(', 't': ']', 'u': '9', 'v': '#', 'w': '+', 'x': "'", 'y': 'P', 'z': 'X', '{': 'K', '|': 'o', '}': 'N', '~': 'g'}


psw = 'password1234'                 
                   
driver = webdriver.Chrome('/Users/christopherrogers/Desktop/Work Programs/chromedriver 4')
driver.implicitly_wait(30)
driver.get('https://collierville.powerschool.com/teachers/pw.html')




driver.find_element_by_name('username').send_keys('crogers')
driver.find_element_by_name('password').send_keys(unchange(psw, dict_chr_to_chr))

driver.find_element_by_name('password').send_keys(Keys.ENTER)

time.sleep(1)
driver.get('https://collierville.powerschool.com/teachers/index.html#/reports/scoresheetReport?sectionId=33577')
          




driver.find_element_by_id('class-selector').click()


driver.find_element_by_class_name('other-header-label').click()


time.sleep(1)
driver.find_element_by_xpath('//*[@id="content-main"]/div[4]/div/div/div/div/ul/li[3]/a').click()

driver.find_element_by_id('output').click()


driver.find_element_by_xpath('/html/body/div[1]/main/div[4]/div/div/div/div/div/div[3]/div[2]/div[2]/div/div/ul/li[2]/a').click()

driver.find_element_by_id('footer-save-button').click()

time.sleep(5)
time.sleep(1)
driver.get('https://collierville.powerschool.com/teachers/index.html#/reports/report-queue')
time.sleep(1)
driver.find_element_by_tag_name('td').find_element_by_tag_name('a').click()


input('Input anything to close browser: ')
time.sleep(1)

driver.quit()
print()
print('Browser closed')


