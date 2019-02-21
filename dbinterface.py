import sqlite3


class DBI:
    def __init__(self):
        conn = sqlite3.connect('pcreeps.db')
        self._c = conn.cursor()

    def createuser(self, nick, pwh):
        #TODO create new user in db
        pass

    def getuserid(self, nick):
        #TODO return user id
        pass

    def getusermap(self, nick):
        #TODO return map id
        pass

    def changeuserpw(self, nick, pwh, pwhnew):
        #TODO password change
        pass

    def checknickavail(self, nick):
        #TODO return True if nick is available
        pass

    def checklogoninfo(self, nick, pwh):
        #TODO return 0 if pwh = db pwh
        pass