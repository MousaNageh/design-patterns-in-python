'''
Lexing Phase
The lexing phase, also known as lexical analysis or tokenization, 
is the process of converting a sequence of characters (such as the source code) into a sequence of tokens.
A token is a string with an assigned and thus identified meaning.
It is structured as a way of simplifying and breaking down the code into pieces that are easier to manipulate for the programming language.
'''
from enum import Enum


class TokenType(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4


class Token:    
    def __init__(self, type, text):
        self.Type = type
        self.text = text

    def __str__(self):
        return f'`{self.text}`'
          

def lex(input):
    result = []

    i = 0
    while i < len(input):
        if input[i] == '+':
            result.append(Token(TokenType.PLUS, '+'))
        elif input[i] == '-':
            result.append(Token(TokenType.MINUS, '-'))
        elif input[i] == '(':
            result.append(Token(TokenType.LPAREN, '('))
        elif input[i] == ')':
            result.append(Token(TokenType.RPAREN, ')'))
        else:  # must be a number
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(TokenType.INTEGER,
                                        ''.join(digits)))
                    break
        i += 1

    return result



if __name__ == '__main__':
    tokens = lex('(13+4)-(12+1)')
    for token in tokens:
        print(token)    