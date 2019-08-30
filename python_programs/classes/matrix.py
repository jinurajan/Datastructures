import os


class Matrix(object):
    def __init__(self, filename=None, matrix=None):
        if filename and matrix:
            raise Exception("You can either supply a filename or a matrix")
        if matrix is not None:
            self.matrix = matrix
        else:
            if os.path.exists(filename):
                self.matrix = self.getmatrix(filename)
            else:
                raise Exception(
                    "File:{} does not exists".format(filename))

    def getmatrix(self, filename):
        matrix = []
        with open(filename, 'r') as f:
            content = f.readlines()
            for line in content:
                line.strip()
                line = line.split()
                row = [int(l) for l in line]
                matrix.append(row)
        return matrix

    def __str__(self):
        string = ""
        for each in self.matrix:
            string += " ".join(map(str, each))
            string += "\n"
        return string

    def write(self, file):
        with open(file, 'w') as f:
            matrix = self.__str__()
            f.write(matrix)

    def __add__(self, other):
        matrix1 = self.matrix
        matrix2 = other.matrix
        result = []
        for i in range(len(matrix1)):
            row_result = []
            for j in range(len(matrix1[0])):
                row_result.append(
                    matrix1[i][j] + matrix2[i][j])
            result.append(row_result)
        return Matrix(matrix=result)


if __name__ == "__main__":
    m1 = Matrix("matrix1.txt")
    print m1
    m2 = Matrix("matrix2.txt")
    print m2
    m3 = m1 + m2
    m3.write("matrix3.txt")
