grammar TommyWiC;


//Parser's rules
program
    : main_func
    ;

main_func
    : BEGINMAIN statements ENDMAIN
    | BEGINMAIN ENDMAIN
    ;

statements
    : statement*
    ;

statement
    : var_assign
    | operations
    | print_stmt
    | condition_stmt
    | while_stmt
    | try_except
    ;

print_stmt
    : print_str
    | print_expression
    ;

print_str
    : PRINT STRING
    ;

print_expression
    : PRINT expression
    ;

condition_stmt
    : IF expression statements (ELIF expression statements)* (ELSE statements)? ENDIF
    ;

while_stmt
    : WHILE expression statements END
    ;

try_except
    : TRY1 operations TRY2 EXCEPT (operations | statements)
    ;

var_assign
    : ID ASSIGN1 expression ASSIGN2
    ;


expression
    : ID                                      #varexpr
    | INT                                     #numberexpr
    | TRUE                                    #trueexpr
    | FALSE                                   #falseexpr
    | expression LESS1 expression LESS2       #less
    | AND1 expression AND2 expression AND3    #and
    | OR1 expression OR2 expression           #or
    | NOT expression                          #not
    | expression NOTEQ1 expression NOTEQ2     #noteq
    ;

operations
    : operation | operations operation
    ;

operation
    : ID ADDOP expression                     #plusop
    | SUBOP1 ID SUBOP2 expression             #minusop
    | ID MULOP expression                     #mulop
    | DIVOP1 ID DIVOP2 expression             #divop
    | ID DECREMENT                            #decrement
    | INCREMENT ID                            #increment
    ;


//Lexer's rules
TRUE
    : 'Anything for my princes'
    ;

FALSE
    : 'I did not hit her. It\'s not true! It\'s bullshit, I DID NOT!'
    ;

NOTEQ1
    : 'is a quack,'
    ;

NOTEQ2
    : 'is a duck'
    ;

ASSIGN1
    : 'is just a'
    ;

ASSIGN2
    : 'CHEEP CHEEP CHEEP!'
    ;

WHILE
    : 'This is a great party, you invited all my friends'
    ;

END
    : 'Everybody betray me. I\'m fed up with this world!'
    ;

IF
    : 'I have an announcement to make. We are expecting'
    ;

ELIF
    : 'Alright, let\'s toss the ball around'
    ;

ELSE
    : 'Anyway, how is your sex life?'
    ;

ENDIF
    : 'I\'m tired. I\'m wasted. I love you, darling'
    ;

PRINT
    : 'Yeah, you can say that again'
    ;

AND1
    : 'I\'m so happy I have'
    ;

AND2
    : 'as my best friend, and I love'
    ;

AND3
    : 'so much'
    ;

OR1
    : 'Look, this is not right. You are living with a'
    ;

OR2
    : 'and doing sex with a'
    ;

NOT
    : 'It\'s bullshit!'
    ;

LESS1
    : 'is great but'
    ;

LESS2
    : 'is a crowd'
    ;

DECREMENT
    : 'is as good in bed as he is at getting promotions... Awful!'
    ;

INCREMENT
    : 'You\'re acting like a kid. Just grow up,'
    ;

ID
    : [a-zA-Z_][a-zA-Z0-9_-]*
    ;

INT
    : '-'? [0-9]+
    ;

STRING
    : ( SHORT_STRING | LONG_STRING )
    ;

BEGINMAIN
    : 'Oh hi Mark'
    ;

ENDMAIN
    : 'What a story, Mark'
    ;

SUBOP1
    : 'Get out! Get out! Get out of'
    ;

DIVOP1
    : 'You are taking'
    ;

ADDOP
    : 'and your stupid mother'
    ;


MULOP
    : 'let\'s go inside and eat some'
    ;

SUBOP2
    : 'life,'
    ;

DIVOP2
    : 'apart,'
    ;

TRY1
    : 'Just what sort of perverted filth are you planning to use'
    ;

TRY2
    : 'for!?'
    ;

EXCEPT
    : 'Come on, stop. It was a mistake'
    ;

WS
    : ( SPACES | COMMENT) -> skip
    ;

//Fragments
fragment COMMENT
    : 'Keep your stupid comments in your pocket' ~[\r\n\f]*
    ;

fragment SPACES
    : [ \t\r\n]+
    ;

fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"'
 ;

fragment LONG_STRING
 : '\'\'\'' LONG_STRING_ITEM*? '\'\'\''
 | '"""' LONG_STRING_ITEM*? '"""'
 ;

fragment LONG_STRING_ITEM
 : LONG_STRING_CHAR
 | STRING_ESCAPE_SEQ
 ;

fragment LONG_STRING_CHAR
 : ~'\\'
 ;

fragment STRING_ESCAPE_SEQ
 : '\\' .
 ;