"""
You’re given an array of positive integers, w, where w[i] describes the weight of the ith index.

You need to perform weighted random selection to return an index from the w array. The larger the value of w[i], the heavier the weight is. Hence, the higher the chances of its index being picked.

Suppose the weights array contains the values [12,84,35]. In this case, the probabilities of picking the indexes will be the following:

Index 0: 12/(12+84+35)=9.2%
Index 1: 84/(12+84+35)=64.1%
Index 2: 35/(12+84+35)=26.7%

"""
import random


class RandomPickWithWeight:

    def __init__(self, w):
        # Write your code here
        # The integer's weight array is passed to the constructor
        self.sums = []
        sum = 0
        for weight in w:
            sum += weight
            self.sums.append(sum)
        self.total = sum

    def pick_index(self):
        # Write your code here
        # Currently returning the first index
        # Your function should implement the required solution to this problem
        target = random.randint(0, self.total)
        low = 0
        high = len(self.sums)-1
        while low < high:
            mid = (low + high) // 2
            if self.sums[mid] > target:
                high = mid
            else:
                low = mid + 1

        return low

# Driver code


def main():
    counter = 900
    weights1 = [1, 2, 3, 4, 5]
    weights2 = [1, 12, 23, 34, 45, 56, 67, 78, 89, 90]
    weights3 = [10, 20, 30, 40, 50]
    weights4 = [1, 10, 23, 32, 41, 56, 62, 75, 87, 90]
    weights5 = [12, 20, 35, 42, 55]
    weights6 = [10, 10, 10, 10, 10]
    weights7 = [10, 10, 20, 20, 20, 30]
    weights8 = [1, 2, 3]
    weights9 = [10, 20, 30, 40]
    weights10 = [5, 10, 15, 20, 25, 30]
    weights = [weights1, weights2, weights3, weights4, weights5,
               weights6, weights7, weights8, weights9, weights10]
    dict = {}
    for i in range(len(weights)):
        print(i + 1, ".\tInput: ", weights[i], ", pick_index() called ", counter, " times", "\n", sep="")
        [dict.setdefault(l, 0) for l in range(len(weights[i]))]
        for j in range(counter):
            sol = RandomPickWithWeight(weights[i])
            index = sol.pick_index()
            dict[index] += 1
        print("-"*95)
        print("{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<15}{:<5}{:<15}".format( \
            "Indexes", "|", "Weights", "|", "Occurences", "|", "Frequency", "|", "Expected Frequency"))
        print("-"*95)
        for key, value in dict.items():

            print("{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<15}{:<5}{:<15}".format(key, "|", weights[i][key], "|", value, "|", \
                str(round((value/counter)*100, 2)) + "%", "|", str(round(weights[i][key]/sum(weights[i])*100, 2))+"%"))
        dict = {}
        print("\n", "-"*100, "\n", sep="")


if __name__ == '__main__':
    main()
