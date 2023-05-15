"""
Write an algorithm to determine if a number  n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 
1
1
 (where it will stay), or it loops endlessly in a cycle which does not include 
1
1
.
Those numbers for which this process ends in 
1
1
 are happy.
Return TRUE if 
�
n
 is a happy number, and FALSE if not.

Constraints

1
≤
1≤
 
�
n
 
≤
2
31
−
1
≤2 
31
 −1
"""
def is_happy_number(n):
    #Write your code here
    if n == 2:
        return False
    def get_new_val(n):
        result = 0
        while n:
            n, mod = divmod(n, 10)
            result += pow(mod, 2)
        return result
    
    slow = n
    fast = get_new_val(n)
    while fast != 1 and fast != slow:
        slow = get_new_val(slow)
        fast = get_new_val(get_new_val(fast))
    if fast == 1:
        return True
    return False


print(is_happy_number(1))
print(is_happy_number(2))
print(is_happy_number(4))