from core.lexer import MyLexer
from core.parser import MyParser

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()
    debug_token_list = False
    
    while True:
        try:
            text = input('(calc) >> ')
        except EOFError:
            break
        if text:
            token_list = lexer.tokenize(text)
            if debug_token_list:            
                for token in token_list:
                    print('type=%r, value=%r' % (token.type, token.value))
            parser.parse(token_list)