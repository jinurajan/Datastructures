"""
Stay Positive

There is a given array of integers. Start with some value x and add each of the array elements to it consecutively. 
That is calculate a running sum of x plus each of the array elements.
Determine the minimum value of x such that the running sum is always atleast 1

Examples:

arr = [-4, 3, 2, 1]

if x == 5 running sums are

5 + -4 = 1
1 + 3 = 4
4 + 2 = 6
6 + 1 = 7
There is no smaller value for x  that satisfies the condition


arr = [3, -6, 5, 2, 1]

If the starting value is 4, running sums are [7,1,6,4,5]. This is the minimum starting value

"""

def minStart(arr):
    result = None
    for i in range(-999999, 1000001):
        x = i
        valid_for_all_array = False
        for each in arr:
            running_sum = x + each
            print "running_sum:{}".format(running_sum)
            if running_sum < 1:
                valid_for_all_array = False
                break;
            else:
                valid_for_all_array = True
                x = running_sum
        if valid_for_all_array == True:
            break;
            result = i
    return result

if __name__ == '__main__':
    arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]
    print minStart(arr)
