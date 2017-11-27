%%token

id

%%syntax

E : E '+' A
  | E '-' A
  | A
  ;
A : A '*' B
  | A '/' B
  | B
  ;
B : '(' E ')'
  | id
  ;