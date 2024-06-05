from sly import Parser
from .lexer import MyLexer

class MyParser(Parser):
    debugfile = 'parser.out'
    tokens = MyLexer.tokens

    precedence = (
        ('left', 'IG', 'DI'),
        ('left', '+', '-'),        
        ('left', '*', '/', 'MOD'),        
        ('right', 'UMINUS'), 
    )

    def __init__(self):
        self.names = {}


    @_('ID "=" expr')
    def statement(self, p):
        self.names[p.ID] = p.expr
           
    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr "+" expr')  
    def expr(self, p):
        return p[0] + p[2]

    @_('expr "-" expr')  
    def expr(self, p):
        return p[0] - p[2]

    @_('expr "*" expr')  
    def expr(self, p):
        return p[0] * p[2]

    @_('expr "/" expr')  
    def expr(self, p):
        return p[0] / p[2]

    @_('expr MOD expr') 
    def expr(self, p):
        return p[0] % p[2]

    @_('expr IG expr')  
    def expr(self, p):
        return p[0] == p[2]

    @_('expr DI expr')  
    def expr(self, p):
        return p[0] != p[2]

    @_('ID ADD')  
    def statement(self, p):
        if p.ID in self.names:
            self.names[p.ID] += 1
        else:
            print(f"ID <{p.ID}> indefinido")

    @_('ID SUB')  
    def statement(self, p):
        if p.ID in self.names:
            self.names[p.ID] -= 1
        else:
            print(f"ID <{p.ID}> indefinido")

    @_('"-" expr %prec UMINUS') 
    def expr(self, p):
        return -p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NUMERO')
    def expr(self, p):
        return p.NUMBER
        
    @_('ID')
    def expr(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            print('ID <{}> indefinido'.format(p.ID))
            return 0

    @_('FALSO')
    def expr(self, p):
        return False

    @_('VDD')
    def expr(self, p):
        return True