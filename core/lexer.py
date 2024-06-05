from sly import Lexer

class MyLexer(Lexer):
    ignore = ' \t'
    ignore_comment = r'\#.*'

    tokens = {ID, NUMERO, IG, DI, FALSO, VDD, MOD, ADD, SUB}
    literals = { "=", "+", "-", "*", "/", "(", ")"}


    IG = r'=='
    DI = r'!='
    MOD = r'mod'
    ADD = r'\+\+'
    SUB = r'--'

    ID = r'[a-zA-Z_][a-zA-Z0-9]*'
    ID['falso'] = FALSO
    ID['vdd'] = VDD
    
    @_(r'\d+')
    def NUMERO(self, t):
        t.value = int(t.value)
        return t    

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Caractere ilegal {}".format(t.value[0]))
        self.index += 1