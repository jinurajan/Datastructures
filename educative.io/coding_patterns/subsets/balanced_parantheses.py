"""
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""


def generate_valid_parentheses(num):
    result = []

    q = [("", 0, 0)]
    while q:
        s, open_count, close_count = q.pop(0)
        if open_count == num and close_count == num:
            result.append(s[:])
        else:
            if open_count < num:
                q.append((s + "(", open_count + 1, close_count))
            if open_count > close_count:
                q.append((s + ")", open_count, close_count + 1))

    return result


def generate_valid_parentheses(num):
    result = []
    parantheses_string = [0 for _ in range(2 * num)]

    def dfs(open_count, close_count, index):
        if open_count == num and close_count == num:
            result.append("".join(parantheses_string))
            return
        if open_count < num:
            parantheses_string[index] = "("
            dfs(open_count + 1, close_count, index + 1)
        if open_count > close_count:
            parantheses_string[index] = ")"
            dfs(open_count, close_count + 1, index + 1)

    dfs(0, 0, 0)
    return result



def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
