import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Downloaders:

    def __init__(self, url):
        self.url = url

    def beatport_artist(self):
        response = requests.get(self.url)
        artist_page = response.text

        f = open('html/artist.html', 'w')
        f.write(artist_page.encode('utf-8').strip())
        f.close()

    def beatport_label(self):
        response = requests.get(self.url)
        label_page = response.text

        f = open('html/label.html', 'w')
        f.write(label_page.encode('utf-8').strip())
        f.close()

    def beatport_tracks(self):
        response = requests.get(self.url)
        label_page = response.text

        f = open('html/tracks.html', 'w')
        f.write(label_page.encode('utf-8').strip())
        f.close()

    def soundcloud_tracks(self):
        driver = webdriver.Chrome('/Users/koshai/Downloads/chromedriver')
        driver.get(self.url)
        time.sleep(5)

        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True

        with open('html/sctracks.html', 'w') as f:
            f.write(driver.page_source.encode("utf-8"))
        f.close()
        driver.quit()

    def thousandone_tracks(self):
        driver = webdriver.Chrome('/Users/koshai/Downloads/chromedriver')
        driver.get(self.url)
        time.sleep(10)

        i = 1

        while driver.find_element_by_xpath('//*[@id="middleTbl"]/tbody/tr/td/ul/li[1]').get_attribute('class') != "disabled":
            with open('html/thouonetracks'+ str(i) + '.html', 'w') as f:
                f.write(driver.page_source.encode("utf-8"))
            f.close()
            time.sleep(5)
            i += 1
            driver.find_element_by_xpath('//*[@id="middleTbl"]/tbody/tr/td/ul/li[1]/a').send_keys(Keys.RETURN)
            time.sleep(5)

        with open('html/thousandone/thouonetracks' + str(i) + '.html', 'w') as f:
            f.write(driver.page_source.encode("utf-8"))
        f.close()
        driver.quit()


if __name__ == '__main__':
    Downloaders().beatport_artist()
    Downloaders().beatport_label()
    Downloaders().beatport_tracks()
    Downloaders().soundcloud_tracks()
    Downloaders().thousandone_tracks()