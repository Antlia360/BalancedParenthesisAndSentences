from ply.lex import lex
from ply.yacc import yacc

# Tokens are named here
tokens = ('LPAREN', 'RPAREN')

# Ignored spaces
t_ignore = ' '

# Token matching rules as regex
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Error handler for illegal characters
def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex()

# Parsing precedence
precedence = (
    ('left', 'LPAREN', 'RPAREN'),
)

def p_expression(p):
    '''
    expression : LPAREN expression RPAREN
               | empty
    '''
    #rule contents
    if len(p) == 4:
        p[0] = p[2]  
    else:
        p[0] = []

#defining empty
def p_empty(p):
    'empty :'
    pass

#define error
def p_error(p):
    #print("Invalid Matching.")
    pass

# Build the parser
parser = yacc()


#create check parenthesis for checking balanced parenthesis
def check_parenthesis(s):
    result = parser.parse(s, lexer=lexer)

# Empty result here indicates successful parsing
    if result == []:  
        print("Valid Matching.")
    else:
        print("Invalid Matching.")

# Getting input from terminal
terminal_input = input("Give an input string consisting of ‘(‘ and ‘)’: ")
check_parenthesis(terminal_input)
