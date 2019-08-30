

def Sum(matrix1, matrix2):
    # assuming both are same dimension
    result = []
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix1[0])):
            row_result.append(
                matrix1[i][j] + matrix2[i][j])
        result.append(row_result)

    return result


def DisplayMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print matrix[i][j],
        print "\n"


def SumOfNMatrices(matrices):
    result = reduce(Sum, matrices)
    DisplayMatrix(result)

if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix4 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    matrices = [matrix1, matrix2, matrix3, matrix4]
    SumOfNMatrices(matrices)