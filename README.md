# Konica-Minolta v1.1

Konica Minolta bizhub 552 - REST Api - Selenium automation

Task:

Python script saves scaned document to pdf.

Commands:

- Get Page - <https://10.0.8.54/wcd/box.xml>
- Click - Box #8
- Select from Drop Down - Specify operation: Download to PC
- Click - Changes the display
- Click - Check Box next to the 1st document
- Click - Download Setting
- Click - OK
- Click - Download

## GitHub URL - <https://github.com/erlep/Konica-Minolta>

## made by peg - <https://GitHub.com/ErleP>

## History
1.1 - fixed DeprecationWarning '.find_element(By.ID,'   instead of: '.find_element_by_id('
    - fixed DeprecationWarning istead of 'webdriver path' use selenium.webdriver.chrome.service
1.0 - 1st release