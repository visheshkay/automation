from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/channel/UCu4zTCmg04FbPdc9_F5spfg')
subs = driver.find_element_by_xpath(
    '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[4]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string')
subs.click()
