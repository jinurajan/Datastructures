from math import ceil


def printzigzag(string, num_of_rows):
    array = [[] for i in range(num_of_rows)]
    middle_index = int(ceil(num_of_rows / 2))
    flag = False
    middle_count = 0
    for i in range(len(string)):
        index = (i - middle_count) % num_of_rows
        if flag and index == 0:
            array[middle_index].append(string[i])
            flag = False
            middle_count += 1
        else:
            array[index].append(string[i])
        if index == num_of_rows - 1:
            flag = True
        print array
    for i in range(len(array)):
        for j in range(len(array[i])):
            print array[i][j],


if __name__ == "__main__":
    # printzigzag("PAYPALISHIRING", 3)
    printzigzag("PAYPALISHIRING", 4)
