# Lexer Documentation

The lexer is basically composed of two parts:
1.  Token declaration or list
2.  Token specification

The token declaration is a tuple named `tokens` that contains all the labels that the lexer will use to _tokenize_ the input string. This list is also used by the grammar module to identify terminals.

- ```python
    tokens = ('identifier', 'equals', …)

The token specification part is where the regular expressions are defined. Each token is specified by writing a regular expression rule compatible with Python's `re` module. Each of these rules are defined by making declarations with a special prefix `t_` to indicate that it defines a token.

- ```python
    t_EQUALS = r"="

There are also more complex specifications of tokens, for example the newline specification.
- ```python
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

This is because some action needs to be performed.

The last part of the lexer is where it is built. Here, the function `lex.lex()` is used. Then, input data is passed through the function.