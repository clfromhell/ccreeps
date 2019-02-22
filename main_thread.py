import os
import cmd
import multiprocessing
from worker_class import Worker


class Cmd(cmd.Cmd):

    # helper section
    bad_cmd = None

    def filter_func(self, line):
        if "sudo" in line:
            self.bad_cmd = "sudo"
            return True
        elif "apt" in line or "apt-get" in line:
            self.bad_cmd = "apt"
            return True
        elif "python" in line or "python3" in line:
            self.bad_cmd = "py"
            return True
        elif "sed" in line:
            self.bad_cmd = "sed"
            return True
        elif "cd" in line:
            self.bad_cmd = "cd"
            return True
        return False

    # main class functions
    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.prompt = ">>"

    def do_test(self, *args):
        print("lol" + str(args))

    def do_import_new_command(self, new_cmd):
        # todo: dynamically add new commands
        pass

    def do_override_command(self, cmd_to_override):
        # todo: override old commands
        pass

    def do_clear(self, line):
        os.system("clear")

    def do_exit(self, line):
        return True

    def default(self, line):
        # enable system commands
        if "!" in line:
            sys_commands = line.replace("!", "")
            if self.filter_func(sys_commands):
                print("~{}~ We don't do that here (╯°□°)╯ ~~ ┻━┻".format(self.bad_cmd))
            else:
                os.system(sys_commands)
        else:
            print(line)


def main(intro=None):  # main method for recursive call at keyboard interrupt
    cmd_custom = Cmd()
    try:
        if intro is None:
            cmd_custom.cmdloop("Welcome to pcreeps :thumbsup:")
        else:
            print()  # newline! :D
            cmd_custom.cmdloop()
    except KeyboardInterrupt:
        main("")


if __name__ == "__main__":
    main()
