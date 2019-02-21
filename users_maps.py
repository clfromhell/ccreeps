from dbinterface import DBI as db
import hashlib


class MapPoint:
    def __init__(self, x, y, value=""):
        self._x = x
        self._y = y
        self._value = value

    def ret_value(self):
        return self._value

    def set_value(self, value=""):
        self._value = value

    def ret_coords(self):
        return self._x, self._y
    

class Map:
    def __init__(self, ):
        pass
    # TODO create Map class and check how to store its objects on harddisk

class User:
    def __init__(self):
        self._uid = ""
        self._nick = ""
        self._pwh = ""
        self._map_id = ""
        self._h = hashlib.sha256()

    def new_user(self, nick, pw):
        if not db.check_nick_avail(nick):
            self._nick = nick
            self._h.update(pw)
            self._pwh = self._h.hexdigest()

            db.create_user(self._nick, self._pwh)

            return db.get_user_id(self._nick)

        else:

            return False

    def logon(self, nick, pw):
        if db.check_nick_avail(nick):
            self._nick = nick
            self._h.update(pw)
            self._pwh = self._h.hexdigest()

            if db.check_logon_info(self._nick, self._pwh):
                return True
            else:
                return False

    def del_user(self, nick):
        self._nick = nick

        db.remove_map(db.get_user_map(self._nick))
        db.remove_user(self._nick)

        del self
