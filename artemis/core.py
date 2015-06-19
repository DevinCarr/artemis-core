import shlex
from subprocess import Popen, PIPE
# Artemis imports
from .stdcmd import io
from .command import Commands
from .tests import TestFrame

class Core:
    """The Artemis Core class"""
    def __init__(self, version):
        self.commands = Commands()
        self.version = version
        self.out = ""
        self.err = ""

    def check_commands(self,args):
        keys = self.commands.command_list.keys()
        check = args
        if type(args) is list:
            check = args[0]
        for command in keys:
            if args[0] == command:
                self.commands.command_list[command].execute(args)
                return True
        return False

    def check_bash(self,args):
        """Check bash for the command"""
        try:
            with Popen(args,stdout=PIPE) as process:
                out, err = process.communicate()
                self.out = out[:-1].decode('utf8')
                self.err = err
        except OSError as e:
            self.err = e
            return False
        except FileNotFoundError as e:
            self.err = e
            return False
        except ValueError as e:
            # invalid arguements
            self.err = e
            io.op('Invalid arguments for {0}'.format(args))
            return False
        else:
            return True

    def ask_question(self,question=None):
        """Prompts the user for input"""
        self.out = ""
        self.err = ""
        if question is None:
            question = io.ip()
        args = shlex.split(question)
        found = self.check_commands(args)
        if not found:
            self.check_bash(args)
        if self.err:
            io.op(self.err)
            return False
        else:
            io.op(self.out)
        return True

    def run_tests(self):
        testing = TestFrame(self)
        return testing.run_all()
