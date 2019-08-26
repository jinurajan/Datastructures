

def Sum(matrix1, matrix2):
    # assuming both are same dimension
    result = []
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix1[0])):
            row_result.append(
                matrix1[i][j] + matrix2[i][j])
        result.append(row_result)

    DisplayMatrix(result)


def DisplayMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print matrix[i][j],
        print "\n"


if __name__ == "__main__":
    matrix1 = []
    matrix2 = []
    for k in range(2):
        print "Enter Number of rows of {}th Matrix".format(k)
        r = raw_input()
        print "Enter Number of columns of {}th Matrix".format(k)
        c = raw_input()

        rows = int(r)
        columns = int(c)

        i = 0
        array = []
        while i < rows:
            print "Enter {}th Row".format(i)
            row_input = raw_input().split()
            if len(row_input) != columns:
                raise Exception("Invalid number of elements")
            row = []
            for row_val in row_input:
                row.append(int(row_val))
            array.append(row)
            i += 1

        if k == 0:
            matrix1 = array
        else:
            matrix2 = array

    Sum(matrix1, matrix2)
