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

if __name__ == '__main__':
    Inserters.insert_beatport_artist()