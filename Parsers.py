from bs4 import BeautifulSoup

import urllib2

from Inserters import Inserters

class Parsers:

    def __init__(self, html):
        self.html = html

    def parse_beatport_artist(self):

        html_file = urllib2.urlopen(self.html)
        parsed_html = BeautifulSoup(html_file, "lxml")

        containers = parsed_html.findAll("div", {"class": "top-ten-track-meta"})

        parsed_list = list()

        for container in containers:
            title = container.find("span", {"class": "top-ten-track-primary-title"})
            title_display = title.text

            subtitle = container.find("span", {"class": "top-ten-track-remixed"})
            subtitle_display = subtitle.text

            artist = container.find("span", {"class": "top-ten-track-artists"})
            artist_display = artist.text.strip()

            output = {'song': title_display, 'mix': subtitle_display, 'artist': artist_display}

            parsed_list.append(output)

        Inserters(parsed_list).insert_beatport_artist()

if __name__ == '__main__':
    Parsers.parse_beatport_artist()