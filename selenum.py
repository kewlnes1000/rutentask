import configparser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class SeleniumSpider():
    def __init__(self):

        # 读取 config
        self.runtime = 0
        self.config = configparser.ConfigParser()
        self.config.read('config/config.ini', encoding='UTF-8')
        chrome_path = self.config.get("option", "chrome_path")

        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1')
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-gpu')
        options.add_argument('lang=zh-tw.UTF-8')

        self.driver = webdriver.Chrome(
            executable_path=chrome_path, options=options)

    def login(self):
        start = 1
        self.driver.set_window_position(-500, 0)  # 瀏覽器位置
        self.driver.set_window_size(375, 900)  # 瀏覽器大小
        while start == 1:
            self.driver.get(
                "https://mybid.ruten.com.tw/master/mission_overview.php?utm_source=ruten&utm_medium=display&utm_campaign=20191111&utm_content=right")

            self.username = self.config.get("option", "username")
            self.password = self.config.get("option", "password")
            useridNumInput = self.driver.find_element_by_xpath(
                '//*[@id="userid"]')
            useridNumInput.send_keys(self.username)
            print('key username')
            passNumInput = self.driver.find_element_by_xpath(
                '//*[@id="pass"]')
            passNumInput.send_keys(self.password)
            print('key password')

            time.sleep(1)
            actions = ActionChains(self.driver)
            login = self.driver.find_element_by_xpath(
                '//*[@id="btn-login"]')
            actions.click(login).perform()
            print('click login')

            time.sleep(2)
            actions = ActionChains(self.driver)
            dailytask = self.driver.find_element_by_xpath(
                '//*[@id="mission-overview"]/div[2]/div[2]/div[1]/div[2]/div/a')
            actions.click(dailytask).perform()
            print('click task')

            # time.sleep(2)
            # actions = ActionChains(self.driver)
            # product = self.driver.find_element_by_xpath(
            #     '/html/body/main/div[2]/div/a[1]/div[1]/div')
            # actions.click(product).perform()
            # print('click product')

            time.sleep(11)
            self.runtime = self.runtime + 1
            print('complete ' + str(self.runtime) + ' time')

            # 清除浏览器cookies
            # cookies = self.driver.get_cookies()
            # print(f"main: cookies = {cookies}")
            # self.driver.delete_all_cookies()

            # 删除浏览器全部缓存
            self.driver.get(
                "chrome://settings/clearBrowserData")
            time.sleep(2)
            clearButton = self.driver.execute_script(
                "return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
            # click on the clear button now
            clearButton.click()
            print('clean cache & cookies')
            time.sleep(1)
            # self.driver.close()
            # SeleniumSpider().login()


if __name__ == '__main__':
    SeleniumSpider().login()
