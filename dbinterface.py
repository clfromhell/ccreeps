import sqlite3


class DBI:
    def __init__(self):
        conn = sqlite3.connect('pcreeps.db')
        self._c = conn.cursor()

    def create_user(self, nick, pwh):
        # TODO create new user in db
        pass

    def get_user_id(self, nick):
        # TODO return user id
        pass

    def get_user_map(self, nick):
        # TODO return map id
        pass

    def change_user_pw(self, nick, pwh, pwh_new):
        # TODO password change
        pass

    def check_nick_avail(self, nick):
        # TODO return True if nick is available
        pass

    def check_logon_info(self, nick, pwh):
        # TODO return 0 if pwh = db pwh
        pass

    def remove_user(self, nick):
        # TODO drop user from database
        pass

    def remove_map(self, map_id):
        # TODO drop map from database
        pass

    def reset_map(self, map_id):
        # TODO reset map to the default values in database
        pass
