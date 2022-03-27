from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
search = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
search.send_keys('automation')
exe = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon')
exe.click()
