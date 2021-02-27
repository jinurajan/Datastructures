"""
find the longest increasing subsequence in an array of n elements. This is a maximum-length sequence of array elements that goes from left to right, and each element in the sequence is larger than the previous element. For example, in the array
[6,2,5,1,7,4,8,3]

length = 4 (2, 5, 7, 8)

"""

def find_longest_subseq_1(array):
    n = len(array)
    dp =[0 for i in range(n)]
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

def find_longest_subseq(array):
    n = len(array)
    dp =[1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


print(find_longest_subseq([6,2,5,1,7,4,8,3]))