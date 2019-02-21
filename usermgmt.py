from dbinterface import DBI as db
import hashlib


class User:
    def __init__(self):
        self._uid = ""
        self._nick = ""
        self._pwh = ""
        self._h = hashlib.sha256()

    def newuser(self, nick, pw):
        if not db.checknickavail(nick):
            self._nick = nick
            self._h.update(pw)
            self._pwh = self._h.hexdigest()

            db.createuser(self._nick, self._pwh)

            return db.getuserid(self._nick)

        else:

            return 0

    def logon(self, nick, pw):
        if db.checknickavail(nick):
            self._nick = nick
            self._h.update(pw)
            self._pwh = self._h.hexdigest()

            if db.checklogoninfo(self._nick, self._pwh):
                return True
            else:
                return False
            