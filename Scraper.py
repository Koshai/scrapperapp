from Downloaders import Downloaders
from Parsers import Parsers

import time

url = "https://www.beatport.com/artist/eric-prydz/2863"

html = "file:///Users/koshai/PycharmProjects/scraperapp/app/html/artist.html"

class Scrape_Beatport_Tasks:

    def __init__(self, url, html):
        print "Scraping Beatport Artist"
        Downloaders(url).beatport_artist()
        time.sleep(1)

        print "Parsing and storing"
        Parsers(html).parse_beatport_artist()

if __name__ == '__main__':
    Scrape_Beatport_Tasks(url, html)