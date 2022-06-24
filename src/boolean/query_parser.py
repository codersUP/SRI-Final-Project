import ply.yacc as yacc
from src.boolean.query_lexer import tokens


def p_expr_and(p):
    "expr : expr AND expr"
    p[0] = {
        "type": "EXPR",
        "func": "AND",
        "childrens": [p[1], p[3]],
        "format_str": lambda a, b: f"{a} AND {b}",
    }


def p_expr_or(p):
    "expr : expr OR expr"
    p[0] = {
        "type": "EXPR",
        "func": "OR",
        "childrens": [p[1], p[3]],
        "format_str": lambda a, b: f"{a} OR {b}",
    }


def p_expr_term(p):
    "expr : term"
    p[0] = {
        "type": "EXPR",
        "func": "TERM",
        "childrens": [p[1]],
        "format_str": lambda a: f"{a}",
    }


def p_expr_par(p):
    "expr : LPAREN expr RPAREN"
    p[0] = {
        "type": "EXPR",
        "func": "PAREN",
        "childrens": [p[2]],
        "format_str": lambda a: f"( {a} )",
    }


def p_expr_not(p):
    "expr : NOT term"
    p[0] = {
        "type": "EXPR",
        "func": "NOT",
        "childrens": [p[2]],
        "format_str": lambda a: f"NOT {a}",
    }


def p_expr_not_par(p):
    "expr : NOT LPAREN expr RPAREN"
    p[0] = {
        "type": "EXPR",
        "func": "NOTPAREN",
        "childrens": [p[3]],
        "format_str": lambda a: f"NOT ( {a} )",
    }


def p_term(p):
    "term : TERM"
    p[0] = {
        "type": "TERM",
        "word": p[1],
        "format_str": lambda a: f"{a}",
    }

    # Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")


def get_parser():
    return yacc.yacc()
