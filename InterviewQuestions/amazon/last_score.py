"""
given is a num of hits and hits in an array

if hit is an integer add to the score
if hit is 'X' score is double of last score
if hit is 'Z' remove the last score means '-'
if hit is '+' score is the sum of last two scores

iterations:
1. 5 is integer score is 5 [5]
2. -2 is integer score is 3. [5,-2]
3. 4 is integer score 7 [5,-2,4]
4. found 'Z' remove last score 7-4 = 3 [5,-2]
5. found 'x' score is 2*-2 = -4 current score is 3+ -4 = -1 [5,-2,-4]
6. 9 is integer score is -1+9 = 8 [5,2,-4,9]
7. found 'x' score is 9+-4 = 5 current score is 8+ 5 = 13 [ 5, -2, -4, 9, 5]
8. found x score is 9+5 = 14 -> current score is 13 + 14 = 27
"""


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
