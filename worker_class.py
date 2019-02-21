# main class of this file
class Worker:

    def __init__(self, cmd, worker_id):  # probably hash path
        self._cmd = cmd
        self._id = worker_id
        self._status = None
        self.check_for_new_cmd()

    def check_for_new_cmd(self):
        import Command

        if self._cmd != Command.get_cmd():
            self._cmd = Command.get_cmd()
