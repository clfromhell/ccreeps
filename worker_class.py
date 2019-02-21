# main class of this file
class Worker:

    def __init__(self, command_path):  # probably hash path
        self.cmd = None
        self.status = None
        self.cmd_path = command_path

    def check_for_new_cmd(self):
        import Command
