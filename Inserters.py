import sqlite3

class Inserters:

    def __init__(self, p_list):
        self.list_for_db = p_list

    def insert_beatport_artist(self):
        conn = sqlite3.connect('mainrecord.db')
        c = conn.cursor()

        for item in self.list_for_db:
            c.execute('INSERT INTO TOPTEN(TITLE, SUBTITLE, ARTIST) VALUES (?,?,?)',
                  [item['song'], item['mix'], item['artist']])

        conn.commit()

        conn.close()

    def insert_beatport_label(self):
        conn = sqlite3.connect('mainrecord.db')
        c = conn.cursor()

        for item in self.list_for_db:
            c.execute('INSERT INTO LABELTOPTEN(TITLE, SUBTITLE, ARTIST) VALUES (?,?,?)',
                      [item['song'], item['mix'], item['artist']])

        conn.commit()

        conn.close()

    def insert_beatport_track(self):
        conn = sqlite3.connect('mainrecord.db')
        c = conn.cursor()

        for item in self.list_for_db:
            c.execute('INSERT INTO TRACKTOPHUNDRED(TITLE, LABEL, ARTIST, REMIXER) VALUES (?,?,?,?)',
                      [item['song'], item['label'], item['artist'], item['remixer']])

        conn.commit()

        conn.close()

    def insert_soundcloud_track(self):
        conn = sqlite3.connect('mainrecord.db')
        c = conn.cursor()

        for item in self.list_for_db:
            c.execute('INSERT INTO SCTRACKS(TITLE, ARTIST, LIKES, PLAYS) VALUES (?,?,?,?)',
                      [item['song'], item['artist'], item['likes'], item['plays']])

        conn.commit()

        conn.close()

    def insert_thousandone_track(self):
        conn = sqlite3.connect('mainrecord.db')
        c = conn.cursor()

        for item in self.list_for_db:
            c.execute('INSERT INTO THOUSANDONETRACKS(TITLE) VALUES (?)',
                      [item['song']])

        conn.commit()

        conn.close()

if __name__ == '__main__':
    Inserters.insert_beatport_artist()