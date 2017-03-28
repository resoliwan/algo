1. Create an empty stack called opstack for keeping operators. Create an empty list for output.
2. Convert the input infix stirng to a list by using the string method split.
3. Scan the token list from left to right.
    if token is an operand, append it to the end of the output list.
    if token is a left parenthesis, push it on the opstack.
    if token is a right parenthesis, pop the opstack until the corrrespoding left parenthesis is removed. Append each operator to the end of the output list.
    if token is an operator, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
4. When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and be appended to the end of the output list.
