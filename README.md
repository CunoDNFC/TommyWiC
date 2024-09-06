# TommyWiC

An esoteric programming language (just a silly Python transpiler for now. Sorry, I'm working on it) inspired by
quotes from the cult movie [The Room](https://www.imdb.com/title/tt0368226/) by
brilliant [Tommy Wiseau](https://en.wikipedia.org/wiki/Tommy_Wiseau).

With all due respect to [ArnoldC](https://github.com/lhartikk/ArnoldC)

________________________________________________________________________________________________________________________

Based on python3, ANTLR4 grammar, interface with tkinter

## Hello, World!

    Oh hi Mark
    Yeah, you can say that again "Hello, world!"
    What a story, Mark

## Quick start

after installing the requirements:

(pip install -r /path/to/requirements.txt)

    cd main/grammar
    antlr4 -Dlanguage=Python3 -visitor -no-listener TommyWiC.g4
    cd ../

* If you want to use an interface window:`main.py`


* If for some bad reason you want to type everything by hand without saving and cleaning:
`customVisitor.py`

## Short guide

________________________________________________________________________________________________________________________

# Operations:

**PLUS OPERATOR:**  
val1 `and your stupid mother` val2

**MINUS OPERATOR:**
`Get out! Get out! Get out of` var1 `'s life,` var2

**MUL OPERATOR:**   
var1 `let's go inside and eat some` var2

**DIV OPERATOR:**   
`You are taking` var1 `apart,` var2

**INCREMENT:**      
`You're acting like a kid. Just grow up,` var

**DECREMENT:**     
var `is as good in bed as he is at getting promotions... Awful!`

________________________________________________________________________________________________________________________

# Expressions:

**ID:**
named declared variable (the name must begin with a letter of the English alphabet or the “_” character)

**INT:**
a negative, positive or zero integer

**TRUE:**
`Anything for my princes`

**FALSE:**
`I did not hit her. It's not true! It's bullshit, I DID NOT!`

**LESS:**  
expression1 `is great but` expression2 `is a crowd`

**NOT EQ, !=:**    
expression1 `is a quack,` expression2 `is a duck`

**AND:**   
`I'm so happy I have` expression1 `as my best friend, and I love` expression2 `so much`

**OR:**    
`Look, this is not right. You are living with a` expression1 `and doing sex with a` expression2

**NOT:**   
`It's bullshit!` expression
________________________________________________________________________________________________________________________

# Statements:

#### Value assignment:

var `is just a` expression `CHEEP CHEEP CHEEP! `

#### Operations:

Arithmetic operations, decrement and increment

#### Print:

`Yeah, you can say that again` expression

`Yeah, you can say that again` 'str'

#### Conditional Statements:

if:   `I have an announcement to make. We are expecting`

       expression 
       statements 

elif: `Alright, let's toss the ball around`

       expression 
       statements 

else: `Anyway, how is your sex life?`

       statements 

endif:`I'm tired. I'm wasted. I love you, darling`

#### While:

`This is a great party, you invited all my friends`

    expression

    statements

`Everybody betray me. I'm fed up with this world!`

#### Try/Except:

`Just what sort of perverted filth are you planning to use`

    operations

`for?`

`Come on, stop. It was a mistake`

    operations
________________________________________________________________________________________________________________________

## To comment the line:

`Keep your stupid comments in your pocket` any ignored stuff here
________________________________________________________________________________________________________________________

## In progress:
(but that's not certain)

0. [ ] Furious debugging
1. [ ] Methods
2. [ ] Static typing
3. [ ] Adding new types
4. [ ] Abstract Syntax Tree
5. [ ] Intermediate Representation from AST
6. [ ] Machine code generation from IR
6. [X] ??????
7. [ ] PROFIT!
