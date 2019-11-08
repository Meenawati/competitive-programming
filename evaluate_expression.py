
def evaluate(s):
    ops = ['+', '-', '*', '/']
    for i in range(len(s)):
        if s[i] in ops:
            return operate(int(s[0:i]), int(s[i+1:len(s)]), s[i])


def operate(n1, n2, o):
    if o is '+': return n1+n2
    elif o is '-': return n1-n2
    elif o is '*': return n1*n2
    elif o is '/': return n1/n2


print(evaluate("122+2"))
print(evaluate("2*122"))
print(evaluate("120/10"))
print(evaluate("1200-200"))