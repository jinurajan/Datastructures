"""
Write a script to create and display a matrix  
"""


def DisplayMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print matrix[i][j],
        print "\n"


if __name__ == "__main__":
    print "Enter Number of rows:"
    r = raw_input()
    print "Enter Number of columns:"
    c = raw_input()

    rows = int(r)
    columns = int(c)

    i = 0
    array = []
    while i < rows:
        print "Enter {}th Row".format(i)
        row_input = raw_input().split()
        print row_input
        if len(row_input) != columns:
            raise Exception("Invalid number of elements")
        row = []
        for row_val in row_input:
            row.append(int(row_val))
        array.append(row)
        i += 1
    print DisplayMatrix(array)
