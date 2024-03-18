'''
The Interpreter design pattern is a behavioral design pattern that specifies how to evaluate sentences in a language.
The main idea is to define a language's grammar along with an interpreter that uses the grammar to interpret sentences in the language.
It is often used in specialized circumstances where the language is simple and efficiency is not a critical concern.
'''
'''
In the context of programming languages and compilers,
the process of interpreting or compiling a source code involves several phases, among which lexing and parsing are fundamental.

Lexing Phase
The lexing phase, also known as lexical analysis or tokenization, 
is the process of converting a sequence of characters (such as the source code) into a sequence of tokens.
A token is a string with an assigned and thus identified meaning.
It is structured as a way of simplifying and breaking down the code into pieces that are easier to manipulate for the programming language.

Parsing Phase
Following lexing, the parsing phase, also known as syntax analysis, 
takes the sequence of tokens produced by the lexer as input and attempts to determine 
its grammatical structure with respect to a given formal grammar. 
This phase builds what is known as a parse tree or an abstract syntax tree (AST), 
which is a hierarchical structure that represents the grammatical structure of the token sequence.
'''