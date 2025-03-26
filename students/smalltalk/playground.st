"
<implies> ::= <or> '->' <implies>
            | <or>

<or> ::= <and> '|' <or>
       | <and>

<and> ::= <unary> '&' <and>
        | <unary>

<unary> ::= '!' <unary>
          | <ground>

<ground> ::= <scalar> | <ident>

<scalar> ::= '1' | '0'

<ident> ::= '[A-Za-z0-9]*'
"

|top bot scalar ident ground unary and or implies parser|

top := Parser just: '1'.
bot := Parser just: '0'.
scalar := top | bot.

ident := Parser greedy: (Identifier new).
ground := scalar | ident.

unary := Parser unary: '!' to: ground.
and := Parser binary: '&' between: unary.
or := Parser binary: '|' between: and.
implies := Parser binary: '->' between: or.

parser := implies.

parser parseString: '!!!!!1 -> 1 & 1 | 0 & chau & !!!!hola'.

