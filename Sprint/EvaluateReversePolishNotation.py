class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        val = 0
        stack = []
        
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(x + y)
                elif token == '-':
                    stack.append(x - y)
                elif token == '*':
                    stack.append(x * y)
                elif token == '/':
                    if x / y < 0:
                        stack.append(math.ceil(x / y))
                    else:
                        stack.append(math.floor(x / y))
                
        return stack.pop()
