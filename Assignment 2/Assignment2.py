from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


web = webdriver.Chrome(ChromeDriverManager().install())
web.get('https://automationpractice.com/index.php')

FirstName = "Printed Summer Dress"
first = web.find_element_by_xpath('//*[@id="search_query_top"]')
first.send_keys(FirstName)

Submit = web.find_element_by_xpath('//*[@id="searchbox"]/button')
Submit.click()

img = web.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div/[1]/div/a[1]/img')
img.click()
