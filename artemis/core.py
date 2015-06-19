import sys
import json
import shlex
from subprocess import Popen, PIPE
import os
import test
from .command import Command
from .tests import TestFrame

class Core:
    def __init__(self, version):
        # List of default commands
        default = [('lc',Command('lc',self.list_commands,'List of all Artemis\'s Current Commands.')),
                    ('help',Command('help',self.print_help,'List the help')),
                    ('newc',Command('newc',self.create_command,'Create a new command.')),
                    ('cd',Command('cd',self.change_directory,'Change directory.')),
                    ('quit',Command('quit','import sys; sys.exit(0)','Quit Artemis.'))]
        self.commands = dict(default)
        self.version = version
        self.out = ""

    def op(self,message):
        if message is not None:
            print(str(message))
            return message

    def ip(self,message=''):
        return input('Arty: {0}'.format(message))

    def check_commands(self,args):
        keys = self.commands.keys()
        check = args
        if type(args) is list:
            check = args[0]
        for command in keys:
            if args[0] == command:
                self.out = self.commands[command].execute(args)
                return True
        return False

    def check_bash(self,args):
        """Check bash for the command"""
        try:
            with Popen(args,stdout=PIPE) as process:
                out, err = process.communicate()
                self.out = out[:-1].decode('utf8')
        except OSError:
            # file/program doesn't exist
            return False
        except FileNotFoundError:
            return False
        except ValueError:
            # invalid arguements
            self.op('Invalid arguments for {0}'.format(args))
            return True
        else:
            return True

    def ask_question(self,question=None):
        """Prompts the user for input"""
        self.out = ""
        if question is None:
            question = self.ip()
        args = shlex.split(question)
        found = self.check_commands(args)
        if not found:
            if not self.check_bash(args):
                self.op('Command not found: {}'.format(args[0]))
                return False
        self.op(self.out)
        return True

    def list_commands(self,args):
        """List all of the currently loaded arty-commands"""
        self.op('Artemis\'s current command list:')
        for command in self.commands:
            self.commands[command].help()

    def create_command(self,args):
        prompt = self.ip('Name: ')
        keys = self.commands.keys()
        while prompt in keys:
            self.op('Sorry, that function name is taken, please try another.')
            prompt = self.ip('Name: ')
        function = self.ip('{:s}\'s operation: '.format(prompt))
        definition = self.ip('{:s}\'s definition: '.format(prompt))

        self.commands[prompt] = Command(prompt,function,definition)

    def print_help(self,args):
        helpMessage = '\nArtemis v{0}\n\nA simple inline configurable shell bot in python.'
        self.op(helpMessage.format(self.version))

    def change_directory(self,args):
        if type(args) is list:
            args = args[0]
        try:
            os.chdir(args)
        except FileNotFoundError:
            self.op('No such file or directory: \'{}\''.format(args))

    def run_tests(self):
        testing = TestFrame(self)
        return testing.run_all()
