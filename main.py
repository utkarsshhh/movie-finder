from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('/Users/utkarshpadia/Downloads/chromedriver-mac-arm64/chromedriver')

driver.get('https://www.google.co.in/')

input_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
input_box.send_keys('top 100 movies of all time')
input_box.send_keys(Keys.ENTER)
imdb_link = driver.find_element_by_xpath('/html/body/div[5]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/span/a')
imdb_link.click()
time.sleep(7)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
driver.save_screenshot("screenshot.png")

poster = driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[50]/div[1]/div/div/div[1]/div[1]/div/a/div')
poster.screenshot('screenshot2.png')
driver.quit()