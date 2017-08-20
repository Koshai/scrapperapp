import urllib2

class Downloaders:

    def __init__(self, url):
        self.url = url

    def beatport_artist(self):
        req = urllib2.Request(self.url)
        response = urllib2.urlopen(req)
        artist_page = response.read()

        f = open('html/artist.html', 'w')
        f.write(str(artist_page))
        f.close()

if __name__ == '__main__':
    Downloaders().beatport_artist()