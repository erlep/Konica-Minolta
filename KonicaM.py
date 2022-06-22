#
# Konica Minolta bizhub 552 - REST Api - Selenium automation
# KonicaM.py - stáhne Pdf z boxu číslo 8 - https://10.0.8.54  http://10.0.8.54/wcd/system.xml
#
#  Zmeny:
# + delete pdf
# + close chrome window
#
#  ChromeDriver - WebDriver for Chrome - https://sites.google.com/chromium.org/driver/downloads
#
# Selenium with Python - https://selenium-python.readthedocs.io/
# Selenium Webdriver with Python: Tutorial with Example - https://www.guru99.com/selenium-python.html
# ChromeDriver - WebDriver for Chrome - https://sites.google.com/a/chromium.org/chromedriver/getting-started
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from bs4 import BeautifulSoup
import time
from inspect import currentframe, getframeinfo

# # Pro Ladeni zobrazovani cisla radku
# frameinfo = getframeinfo(currentframe())
# print('#:', frameinfo.filename, frameinfo.lineno)

print('KonicaM - PDF downloader v1.2')

# selenium - How to bypass the message-“your connection is not private” on non-secure page using Selenium? - https://is.gd/7NDpuF
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# inkognito - https://bit.ly/388qqwa
options.add_argument("--incognito")
service = Service(r'd:/Utils/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# napred hl. stranka a pak /wcd/box.xml
# driver.get('https://10.0.8.54')
# driver.get('http://10.0.8.54/wcd/box.xml')  # SSL issue  # http://10.0.8.54/wcd/top.xml
driver.get('http://10.0.8.54/wcd/system.xml')  # SSL issue  # http://10.0.8.54/wcd/top.xml

# class By:                       Old syntax: find_element_by_xxx
#     ID: str                     - driver.find_element_by_id('8_LNK').click()
#     XPATH: str                  - driver.find_element_by_xpath(
#     LINK_TEXT: str
#     PARTIAL_LINK_TEXT: str
#     NAME: str
#     TAG_NAME: str
#     CLASS_NAME: str
#     CSS_SELECTOR: str           - driver.find_element_by_css_selector
# time.sleep(1)  # Let the user actually see something!

# New klik - click OK
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/input').click()
time.sleep(3)
# Klik na Box
driver.find_element_by_xpath('//*[@id="FileIconImg"]').click()
time.sleep(3)

# Python Selenium: Click a href=“javascript:()” - https://is.gd/Adawdj
driver.execute_script("html_f.execBoxLogin('F_UOU','User','8','','_NotRelayAuthOn');")
time.sleep(1)
# How to select a drop-down menu option value using Selenium - Python - https://is.gd/7bX67l
select = Select(driver.find_element(By.ID, 'F_UOU_OPE'))
time.sleep(1)
# Now we have many different alternatives to select an option.
# select.select_by_index(4)
# select.select_by_visible_text("Download to PC")
select.select_by_value('FileDownload')  # Pass value as string
# Klik na "Changes the display"
driver.find_element(By.XPATH, '//*[@id="F_UOU_FD"]/div[2]/table[3]/tbody/tr/td[2]/input').click()
time.sleep(2)
# Klik na vyber dokumentu
driver.find_element(By.ID, 'F_UOU_CHK1').click()
time.sleep(1)
driver.execute_script("html_f.SetDocumentNumber('F_UOU','1','1'); html_f.ClearErr();html_f.SetDocSelect('F_UOU','1','1','User','FileDownload')")
time.sleep(2)
# DownLoad
driver.find_element(By.ID, 'F_UOU_Next0').click()
time.sleep(4)
# OK
driver.find_element(By.CSS_SELECTOR, '#F_UOU_DOFileDownload > div.buttonarea-layout > input[type=submit]:nth-child(1)').click()
time.sleep(12)
# Download
driver.find_element(By.ID, 'btnEXE').click()

# ---------------------------------------------
# Delete Pdf - back + select Delete +
time.sleep(9)
# Back
driver.find_element(By.ID, 'btnOK').click()
time.sleep(2)
# Select Delete
select = Select(driver.find_element(By.ID, 'F_UOU_OPE'))
time.sleep(1)
select.select_by_value('FileDeletion')  # Pass value as string
# Klik na "Changes the display"
driver.find_element(By.XPATH, '//*[@id="F_UOU_FD"]/div[2]/table[3]/tbody/tr/td[2]/input').click()
time.sleep(2)
# Klik na vyber dokumentu
driver.find_element(By.ID, 'F_UOU_CHK1').click()
time.sleep(1)
driver.execute_script("html_f.SetDocumentNumber('F_UOU','1','1'); html_f.ClearErr();html_f.SetDocSelect('F_UOU','1','1','User','FileDownload')")
time.sleep(2)
# Delete
driver.find_element(By.ID, 'F_UOU_Next0').click()
time.sleep(2)
print('back 5')
# OK to delete
driver.find_element(By.XPATH, '//*[@id="F_UOU_DOFileDeletion"]/div[2]/input[1]').click()
time.sleep(2)
# OK
driver.find_element(By.ID, 'btnOK').click()
time.sleep(2)
print('back 9')

# quit - schchvalne vypnute
driver.quit()
print('OkDone.')
