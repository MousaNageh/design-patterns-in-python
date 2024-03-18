'''
Parsing Phase
Following lexing, the parsing phase, also known as syntax analysis, 
takes the sequence of tokens produced by the lexer as input and attempts to determine 
its grammatical structure with respect to a given formal grammar. 
This phase builds what is known as a parse tree or an abstract syntax tree (AST), 
which is a hierarchical structure that represents the grammatical structure of the token sequence.
'''

from lexing import lex, Token, TokenType
from enum import Enum

class Integer:
    def __init__(self, value):
        self.value = int(value)


class BinaryOperation:
    class Type(Enum):
        ADDITION = 0
        SUBTRACTION = 1

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None
    
    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value



def parse(tokens):
    result = BinaryOperation()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token: Token = tokens[i]

        if token.Type == TokenType.INTEGER:
            integer = Integer(token.text)
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.Type == TokenType.PLUS:
            result.type = BinaryOperation.Type.ADDITION
        elif token.Type == TokenType.MINUS:
            result.type = BinaryOperation.Type.SUBTRACTION
        elif token.Type == TokenType.LPAREN:  # note: no if for RPAREN
            j = i
            while j < len(tokens):
                if tokens[j].Type == TokenType.RPAREN:
                    break
                j += 1
            # preprocess subexpression
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j  # advance
        i += 1
    return result


def eval(input):
    tokens = lex(input)
    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')

if __name__ == '__main__':
    eval('(13+4)-(12+1)')
    eval('1+(3-4)')

    # this won't work
    eval('1+2+(3-4)')