import random
import sys
import time
import os


def create_matrix(n, filename):
    matrix = [[-1 for i in range(n)] for j in range(n)]
    number_elements = n * n
    # print number_elements
    count = 0
    # start_time = time.time()
    while count < number_elements:
        r = random.randint(0, n-1)
        c = random.randint(0, n-1)
        if matrix[r][c] == -1:
            # not filled
            val = random.randint(1, 1000)
            matrix[r][c] = val
            count = count + 1
    # print matrix
    # end_time = time.time()
    # return end_time - start_time, matrix
    with open(filename, 'w') as f:
        f.write(print_matrix(matrix))


def print_matrix(matrix):
    string = ""
    for each in matrix:
        string += " ".join(map(str, each))
        string += "\n"
    return string


def getmatrix(filename):
    matrix = []
    with open(filename, 'r') as f:
        content = f.readlines()
        for line in content:
            line.strip()
            line = line.split()
            row = [int(l) for l in line]
            matrix.append(row)
    return matrix


def duplicate_entry_percentage(filename, n):
    matrix = getmatrix(filename)
    duplicate_entries = set()
    duplicate_count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] in duplicate_entries:
                duplicate_count += 1
            else:
                duplicate_entries.add(matrix[i][j])

    percentage = (duplicate_count / float(n * n)) * 100

    return percentage


n = sys.argv[1]
n = int(n)
filename = sys.argv[2]
create_matrix(n, filename)
# print duplicate_entry_percentage(filename, n)
os._exit(0)

# if __name__ == "__main__":
#     n = sys.argv[1]
#     n = int(n)
#     print create_matrix(n)
