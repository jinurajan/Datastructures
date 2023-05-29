"""
For a given number, n, generate all combinations of balanced parentheses.
1≤ n ≤14
"""

def generate_combinations(n):
    result = []

    def backtrack(combination, open_count, close_count):
        if open_count == n and close_count == n:
            result.append("".join(combination[:]))
            return
        if open_count < n:
            combination.append("(")
            backtrack(combination, open_count+1, close_count)
            combination.pop()
        if close_count < open_count:
            combination.append(")")
            backtrack(combination, open_count, close_count+1)
            combination.pop()

    backtrack([], 0, 0)
    return result


def print_result(result):
    for rs in result:
        print("\t\t ", rs)

# Driver code
def main():
    n = [1, 2, 3, 4, 5]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t All combinations of valid balanced parentheses: ")

        result = generate_combinations(n[i])
        print_result(result)

        print("-" * 100)


if __name__ == '__main__':
    main()
