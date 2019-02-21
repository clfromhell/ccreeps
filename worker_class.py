# main class of this file
class Worker:

    def __init__(self):  # probably hash path
        self.cmd = None
        self.status = None
        self.check_for_new_cmd()

    def check_for_new_cmd(self):
        import Command
        if self.cmd != Command.get_cmd():
            self.cmd = Command.get_cmd()
