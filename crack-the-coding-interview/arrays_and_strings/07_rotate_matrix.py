

def rotate_matrix(array):
    if not len(array) or len(array) != len(array[0]):
        return False
    n = len(array)
    layer = 0
    for layer in range(n / 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = array[first][i]
            array[first][i] = array[last - offset][first]
            array[last - offset][first] = array[last][last - offset]
            array[last][last - offset] = array[i][last]
            array[i][last] = top

    return array


if __name__ == "__main__":
    array = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    print rotate_matrix(array)
