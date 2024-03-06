from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()

options.add_experimental_option('prefs',{
    'download.prompt_for_download': False,
    'plugins.always_open_pdf_externally': True
})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
URL = "https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/"
driver.get(URL)
driver.implicitly_wait(3)

    
buttons = driver.find_elements(By.CLASS_NAME,'//*[@id="table-files"]/tbody/tr[1]/td[5]/a')
time.sleep(10)
for button in buttons:
    if button.text == 'Download sample pdf file':
        button.click()
        time.sleep(0.2)