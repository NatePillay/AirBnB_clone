import cmd


class HBNBCommand(cmd.Cmd):
    prompt: '(hbnb)'

    def emtpyline(self):
        '''if empty line is passed do nothing'''
        pass

    def do_EOF(self, line):
        '''command to exit the program'''
        return True

    def do_help(self, line):
        '''provide help for hbnb'''
        if line:
            '''user is asking for specific help commands'''
            try:
                help_func = getattr(self,f'help_{line}')
                help_func()
            except AttributeError:
                print(f"No help avaliable for '{line}'")
        else:
            '''general help required'''
            self.help.command()

    if __name__ == '__main__':
            HBNBCommand().cmdloop()
