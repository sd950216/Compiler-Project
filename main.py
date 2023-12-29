# Install PLY using: pip install ply

import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'ID',
    'PLUS',
    'TIMES',
    'LPAREN',
    'RPAREN',
)

t_PLUS = r'\+'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t


t_ignore = ' \t\n'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()


# Parser
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('+', p[1], p[3])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('*', p[1], p[3])


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_id(p):
    'factor : ID'
    p[0] = ('ID', p[1])


def p_factor_paren(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()

# Example usage
input_string = "a + b * (c + d) "
lexer.input(input_string)
for tok in lexer:
    print(tok)

result = parser.parse(input_string)
print(result)
