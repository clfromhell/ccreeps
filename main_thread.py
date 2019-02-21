import cmd
import multiprocessing
from worker_class import Worker


class Cmd(cmd.Cmd):

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)

    def do_test(self, *args):
        print("lol" + str(args))

    def do_exit(self, line):
        return True

    def default(self, line):
        print(line)


if __name__ == "__main__":
    cmd = Cmd()
    cmd.prompt = ">>"
    cmd.use_rawinput = False
    cmd_input = cmd.cmdloop("Welcome to pcreeps :thumbsup:")
    print(cmd_input)
