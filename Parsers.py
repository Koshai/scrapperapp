from bs4 import BeautifulSoup

import urllib2

from Inserters import Inserters

import glob

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

    def parse_beatport_label(self):

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

        Inserters(parsed_list).insert_beatport_label()

    def parse_beatport_tracks(self):

        html_file = urllib2.urlopen(self.html)
        parsed_html = BeautifulSoup(html_file, "lxml")

        containers = parsed_html.findAll("li", {"class": "ec-item"})

        parsed_list = list()

        for container in containers:
            title = container.find("p", {"class": "buk-track-title"})
            title_display = title.text.strip()

            label = container.find("p", {"class": "buk-track-labels"})
            label_display = label.text

            artist = container.find("p", {"class": "buk-track-artists"})
            artist_display = artist.text

            remixer = container.find("p", {"class": "buk-track-remixers"})
            remixer_display = remixer.text

            output = {'song': title_display, 'label': label_display, 'artist': artist_display, 'remixer': remixer_display}

            parsed_list.append(output)

        Inserters(parsed_list).insert_beatport_track()

    def parse_soundcloud_tracks(self):

        html_file = urllib2.urlopen(self.html)
        parsed_html = BeautifulSoup(html_file, "lxml")

        containers = parsed_html.findAll("li", {"class": "soundList__item"})

        parsed_list = list()

        for container in containers:
            title = container.find("a", {"class": "soundTitle__title"})
            title_display = title.text.strip()

            artist = container.find("span", {"class": "soundTitle__usernameText"})
            artist_display = artist.text

            like = container.find("button", {"class": "sc-button-like"})
            like_number = like.text

            try:
                plays = container.find("li", {"class": "sc-ministats-item"})['title']
                play_count = plays.decode('unicode-escape')
            except TypeError:
                print "Playdata not found"

            output = {'song': title_display, 'artist': artist_display, 'likes': like_number, 'plays': play_count}

            parsed_list.append(output)

        Inserters(parsed_list).insert_soundcloud_track()

    def parse_thousandone_tracks(self):

        path = self.html

        print path

        for infile in glob.glob('html/thousandone/*'):
            full_file = path + infile

            html_file = urllib2.urlopen(full_file)
            parsed_html = BeautifulSoup(html_file, "lxml")

            containers = parsed_html.findAll("div", {"class": "tlLink"})

            parsed_list = list()

            for container in containers:
                title = container.find("a")
                title_display = title.text

                output = {'song': title_display}
                parsed_list.append(output)

            Inserters(parsed_list).insert_thousandone_track()



if __name__ == '__main__':
    Parsers.parse_thousandone_tracks()