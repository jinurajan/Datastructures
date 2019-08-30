

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
