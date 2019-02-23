import os
import cmd


class Cmd(cmd.Cmd):
    # helper section
    bad_cmd = None

    def filter_func(self, line):
        if "ls" in line\
                or "mkdir" in line\
                or "touch" in line\
                or "rm" in line\
                or "pwd" in line:
            return 0
        elif "cd" in line:  # cd is special :(
            return 1
        else:  # filter all other sys commands
            self.bad_cmd = line.split()[0]
            return -1

    # main class functions
    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.prompt = ">>"

    def do_create_new_worker(self, new_cmd):
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
            filter_res = self.filter_func(sys_commands)
            if filter_res == -1:  # filter sys commands
                print("~{}~ We don't do that here (╯°□°)╯ ~~ ┻━┻".format(self.bad_cmd))
            elif filter_res == 1:
                if os.getcwd() == "/home/{}/safe_space".format(os.getlogin()) and ".." in sys_commands:
                    print("Nana you sassy sasquatch :3\n"
                          "Don't try breaking out of the safe space ノ┬─┬ノ ~~ ( \o°o)\ ")
                else:
                    os.chdir(sys_commands.split()[1])
            else:
                os.system(sys_commands)
        else:
            print(line)

    # help descriptions
    @staticmethod
    def help_create_new_worker():
        print("Create a new worker and infuse a new command set to it.\n"
              "Asks for worker id and import file.")

    @staticmethod
    def help_override_command():
        print("Override an old command set of a worker.\n"
              "Asks for worker id and import file")

    @staticmethod
    def help_clear():
        print("Default cli clear command.")

    @staticmethod
    def help_general():
        print("Write '!' first to use some sys commands!\nThough we filter some out ;)")


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
    safe_space = "/home/{}/safe_space".format(os.getlogin())
    if not os.path.exists(safe_space):
        os.mkdir(safe_space)
    os.chdir(safe_space)
    main()
