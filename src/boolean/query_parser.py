import sys
import pprint
import ply.yacc as yacc

from query_lexer import tokens

documents = {1,2,3,4,5,6,7,8,9,10}
inverted_index = {
    "feo": {1,3,5,7},
    "lindo": {1,4,6,8},
    "trueno":{2,4,5,8},
    "lluvia":{1,3,4,6,8,9},
    "final":{1,2,3,4,5,6,7,8,9}

}

def p_expr_and(p):
    'expr : expr AND expr'
    p[0] = p[1].intersection(p[3])


def p_expr_or(p):
    'expr : expr OR expr'
    p[0] = p[1].union(p[3])

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

def p_expr_par(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_expr_not(p):
    'expr : NOT term'
    p[0]= documents.difference(p[2])

def p_expr_not_par(p):
    'expr : NOT LPAREN expr RPAREN'
    p[0]= documents.difference(p[3])

def p_term(p):
    'term : TERM'
    p[0] = inverted_index[p[1]]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")



parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s.lemma_)
    print(result)

