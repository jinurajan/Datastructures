def totalScore(num, blocks):
    # WRITE YOUR CODE HERE
    # keep a stack for tracking last and second last score
    stack = []
    score = 0
    for hit in blocks:
        if type(hit) == int:
            score += hit
            stack.append(hit)
        elif hit == 'X':
            if stack:
                s = stack[-1] * 2
                score += s
                stack.append(s)
        elif hit == 'Z':
            if stack:
                s = stack.pop(-1)
                score -= s
        elif hit == '+':
            s = 0
            if len(stack) >= 2:
                s = stack[-1] + stack[-2]
            elif len(stack) == 1:
                s = stack[-1]
            stack.append(s)
            score += s
    return score
                
            
            
print totalScore(8, [5, -2, 4, 'Z', 'X', 9, '+', '+'])

