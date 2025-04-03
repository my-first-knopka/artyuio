Vars = []
Vars_names = []


class Var:
    def __init__(self, name: str, val, typ):
        self.name = name
        self.type = typ
        if typ == 'integ':
            self.val = int(eval(val))
        elif typ == 'bool':
            self.val = val
        else:
            self.val = eval(val)


class Interpreter:
    def __init__(self, code: str):
        self.code = code
        self.code_strs = self.code.split(';')
        self.code_spl_strs = []
        for k in range(len(self.code_strs)):
            self.code_spl_strs.append(self.code_strs[k].split())

    def interpret(self):
        for i in range(len(self.code_strs)):
            if self.code_spl_strs[i][0] == 'var':
                Vars.append(Var(self.code_spl_strs[i][2], self.code_spl_strs[i][4], self.code_spl_strs[i][1]))
                Vars_names.append(self.code_spl_strs[i][2])
            elif self.code_spl_strs[i][0] == 'print':
                val_to_prt = self.code_spl_strs[i][1].strip('\'')
                if val_to_prt in Vars_names:
                    print(Vars[Vars_names.index(self.code_spl_strs[i][1].strip('\''))].val)
                else:
                    print(val_to_prt.strip('\"'))
            elif self.code_spl_strs[i][0] == '///':
                pass
            elif self.code_spl_strs[i][0] == 'program_end':
                break


file = open('my.art', 'r')
cod = file.read()
interpreter = Interpreter(cod)
interpreter.interpret()
