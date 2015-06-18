class Command:
    def __init__(self,prompt,function,definition):
        self.prompt = prompt
        self.function = function
        self.definition = definition

    def execute(self,args):
        result = None
        passing = args
        if type(args) is list and len(args) > 1:
            passing = args[1:]
        if type(self.function) == str:
            result = exec(self.function)
        else:
            result = self.function(passing)
        return result

    def help(self):
        print('{:s}\t - {:s}'.format(self.prompt,self.definition))
