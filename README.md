# Simple Two-Phase Compiler

This repository contains a simple two-phase compiler implemented in Python. The compiler includes a lexer for lexical analysis and a parser for syntax analysis. It is designed to handle basic expressions with addition, multiplication, and parentheses.

## Features

- Lexical analysis using PLY (Python Lex-Yacc)
- Syntax analysis with context-free grammar rules
- Support for addition, multiplication, and parentheses in expressions

## Usage

1. Install the required dependencies:

   ```bash
   pip install ply

2. Install the required dependencies:
   ```bash
   python main.py


# Example input
a + b * (c + d)

# Output syntax tree
('+', 'a', ('*', 'b', ('+', 'c', 'd')))
