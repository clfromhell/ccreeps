import sqlite3


class DBI:
    def __init__(self):
        conn = sqlite3.connect('pcreeps.db')
        self._c = conn.cursor()

    def createuser(self, nick, pwh):
        pass

    def getuserid(self, nick):
        pass

    def getusermap(self, nick):
        pass

    def changeuserpw(self, nick, pwh, pwhnew):
        pass

    def checknickavail(self, nick):
        pass

    def checklogoninfo(self, nick, pwh):
        #return 0 if pwh = db pwh
        pass