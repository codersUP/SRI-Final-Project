import ply.lex as lex
import spacy


en = spacy.load("en_core_web_sm")

# List of token names.   This is always required
reserved = {"AND": "AND", "OR": "OR", "NOT": "NOT"}

tokens = (
    "AND",
    "OR",
    "NOT",
    "TERM",
    "LPAREN",
    "RPAREN",
)

# Regular expression rules for simple tokens

t_LPAREN = r"\["
t_RPAREN = r"\]"

# A regular expression rule with some action code
# Note addition of self parameter since we're in a class

#  digit            = r'([0-9])'
#  nondigit         = r'([_A-Za-z])'
def t_TERM(t):
    r"[a-zA-Z0-9_.,?!'/\(\)-]+"
    t.type = reserved.get(t.value, "TERM")
    t.value = en(t.value)[0].lemma_ if t.type == "TERM" else t.value
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def get_lexer():
    return lex.lex()
