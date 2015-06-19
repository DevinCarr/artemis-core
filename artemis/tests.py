import os
class TestFrame:
    def __init__(self, artemis_core):
        self.artemis_core = artemis_core
        self.error_code = 0
        self.tests = [
            self.test_internal_commands_1,
            self.test_internal_commands_2,
            self.test_internal_commands_3,
            self.test_directory_change,
            self.test_create_new_command
            ]

    def eq(self,obj1,obj2):
        return obj1 == obj2

    def gt(self,obj1,obj2):
        return obj1 > obj2

    def lt(self,obj1,obj2):
        return obj1 < obj2

    def run_all(self):
        """Run all of the tests

        Will return 0 for pass, 1 for a failed test
        """
        print('RUNNING ARTEMIS-CORE TESTS: ALL')
        print('===============================')
        try:
            for test in self.tests:
                if not test():
                    print('FAILED: {0}'.format(test.__name__))
                    self.error_code = 1
                    break
        except Exception:
            print('EXCEPTION CAUGHT!!')
            print('STDOUT: {}'.format(self.artemis_core.out))
            print('STDERR: {}'.format(self.artemis_core.err))
            return self.error_code
        else:
            if self.error_code == 0:
                print('===============================')
                print('{} TESTS PASSED'.format(len(self.tests)))
            return self.error_code

    def test_internal_commands_1(self):
        """Check that echo 1 returns '1'"""
        self.artemis_core.ask_question('echo 1')
        return self.eq(self.artemis_core.out, '1')

    def test_internal_commands_2(self):
        """Checks for response from invalid arty/bash commands"""
        return self.eq(self.artemis_core.ask_question('a'), False)

    def test_internal_commands_3(self):
        """Checks for the internal command lc properly returns True"""
        return self.artemis_core.ask_question('lc')

    def test_directory_change(self):
        """Checks to make sure the internal cd can change directories properly"""
        self.artemis_core.ask_question('cd ..')
        self.artemis_core.ask_question('pwd')
        return self.eq(os.getcwd(),self.artemis_core.out)

    def test_create_new_command(self):
        """Check for creating new commands"""
        before = len(self.artemis_core.commands.command_list)
        self.artemis_core.ask_question('newc pr "print(1)" "print a one"')
        self.artemis_core.ask_question('pr')
        after = len(self.artemis_core.commands.command_list)
        return self.gt(after,before)
