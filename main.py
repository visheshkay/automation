from selenium import webdriver
import time


class main():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def inlog(self):
        self.driver.get('https://www.instagram.com/')

        time.sleep(2)

        username = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        username.click()
        username.send_keys(str(input('please  give your username:')))

        password = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password.click()
        password.send_keys(str(input('(NOTE: This will not be recorded by us) please give your password:')))

        loginbut = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
        loginbut.click()

        time.sleep(5)

        notnow = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        notnow.click()

        time.sleep(5)

        notnow2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notnow2.click()

        time.sleep(5)
        dbox = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div')
        dbox.click()
        time.sleep(8)
        sbut = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button')
        sbut.click()
        time.sleep(5)
        sbar = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')
        sbar.send_keys(str(input('name of person you want to spam:')))
        time.sleep(3)
        selr = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div')
        selr.click()
        time.sleep(3)
        nex = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div')
        nex.click()
        time.sleep(5)
        msg = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        msg.send_keys('You are being messaged through AUTOMATED BOT')
        time.sleep(1)
        send = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        send.click()


autolog = main()
autolog.inlog()
