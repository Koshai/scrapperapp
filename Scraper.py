from Downloaders import Downloaders
from Parsers import Parsers

import time

artist_url = "https://www.beatport.com/artist/eric-prydz/2863"

artist_html = "file:///Users/koshai/PycharmProjects/scraperapp/muzetrak/html/artist.html"

label_url = "https://www.beatport.com/label/mau5trap/6446"

label_html = "file:///Users/koshai/PycharmProjects/scraperapp/muzetrak/html/label.html"

track_url = "https://www.beatport.com/genre/progressive-house/15/top-100"

track_html = "file:///Users/koshai/PycharmProjects/scraperapp/muzetrak/html/tracks.html"

sc_tracks_url = "https://soundcloud.com/mau5trap"

sc_tracks_html = "file:///Users/koshai/PycharmProjects/scraperapp/muzetrak/html/sctracks.html"

to_tracks_url = "https://www.1001tracklists.com/dj/deadmau5/index.html"

to_tracks_path = "file:///Users/koshai/PycharmProjects/scraperapp/muzetrak/"

class Scrape_Tasks:

    def __init__(self, artist_url,
                 artist_html,
                 label_url,
                 label_html,
                 track_url,
                 track_html,
                 sc_tracks_url,
                 sc_tracks_html,
                 to_tracks_url,
                 to_tracks_path):
        print "Scraping Beatport Artist"
        Downloaders(artist_url).beatport_artist()
        time.sleep(5)

        print "Parsing and storing"
        Parsers(artist_html).parse_beatport_artist()

        print "Scraping Beatport Label"
        Downloaders(label_url).beatport_label()
        time.sleep(5)

        print "Parsing and storing"
        Parsers(label_html).parse_beatport_label()

        print "Scraping Beatport tracks"
        Downloaders(track_url).beatport_tracks()
        time.sleep(5)

        print "Parsing and storing"
        Parsers(track_html).parse_beatport_tracks()

        print "Scraping Soundcloud tracks"
        Downloaders(sc_tracks_url).soundcloud_tracks()
        time.sleep(5)

        print "Parsing and storing"
        Parsers(sc_tracks_html).parse_soundcloud_tracks()

        print "Scraping 1001 tracks"
        Downloaders(to_tracks_url).thousandone_tracks()
        time.sleep(5)

        print "Parsing and storing"
        Parsers(to_tracks_path).parse_thousandone_tracks()

if __name__ == '__main__':
    Scrape_Tasks(artist_url,
                 artist_html,
                 label_url,
                 label_html,
                 track_url,
                 track_html,
                 sc_tracks_url,
                 sc_tracks_html,
                 to_tracks_url,
                 to_tracks_path)