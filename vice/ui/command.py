from cmd import Cmd
try:
    input = raw_input
except NameError:
    # python 3
    pass

class ViceCmd(Cmd):
    prompt = 'vice> '

    def do_open(self, line):
        pass

    def do_new(self, line):
        pass

    def do_remove(self, line):
        pass

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        print('')
        return do_quit(line)

def main():
    import sys
    if len(sys.argv) > 1:
        ViceCmd().onecmd(' '.join(sys.argv[1:]))
    else:
        ViceCmd().cmdloop()


if __name__ == '__main__':
    main()
