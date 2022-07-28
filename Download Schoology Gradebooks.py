
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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


driver = webdriver.Chrome('/Users/christopherrogers/Desktop/Work Programs/chromedriver 11')


driver.set_page_load_timeout(10)
driver.get('https://collierville.schoology.com/home')
driver.find_element_by_name('loginfmt').send_keys('crogers@CHSschoolsemail.org')
driver.find_element_by_name('loginfmt').send_keys(Keys.ENTER)
driver.find_element_by_name('passwd').send_keys(unchange(psw, dict_chr_to_chr))
time.sleep(2)


driver.find_element_by_name('passwd').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_id('idSIButton9').click()

list_of_courses = ['Physics', 'AP Physics 1', 'AP Physics C: E&M']

list_of_gradebook_urls = [
        'https://collierville.schoology.com/course/5145542691/grades/export',
        'https://collierville.schoology.com/course/5145542691/grades/export?csm_section_nid=5145542696',
        'https://collierville.schoology.com/course/5145542657/grades/export',
        'https://collierville.schoology.com/course/5145542657/grades/export?csm_section_nid=5145542660',
        'https://collierville.schoology.com/course/5145542657/grades/export?csm_section_nid=5145542663',
        'https://collierville.schoology.com/course/5145542665/grades/export'
        ]
for url in list_of_gradebook_urls:
    time.sleep(0.5)
    driver.get(url)
    driver.find_element_by_id('edit-export-type-gbook').click()
    driver.find_element_by_id('edit-submit').click()




time.sleep(2)

driver.quit()
print()
print('Browser closed')


