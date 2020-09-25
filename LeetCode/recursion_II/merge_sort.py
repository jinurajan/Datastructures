"""
1. Top down
    1. keep dividing array into 2 until we have 1 element in each list
    2. merge the sublists
    3. after recursion we should have sorted list
2. bottom up
    1. divide array into single elements
    2.merge sublists two at a time until the single list remains
"""


class Solution1(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        return self.merge_sort(nums, 0, len(nums)-1)


    def merge_sort(self, array, l, r):

        def merge(array1, array2):
            result = []
            i = 0
            j = 0
            while i < len(array1) and j < len(array2):
                if array1[i] <= array2[j]:
                    result.append(array1[i])
                    i += 1
                else:
                    result.append(array2[j])
                    j += 1

            result.extend(array1[i:])
            result.extend(array2[j:])
            return result

        if l < r:
            mid = (l + r) / 2
            left = merge_sort_top_down(array, l, mid)
            right = merge_sort_top_down(array, mid+1, r)
            return merge(left, right)
        return array[l:r+1]




def merge(array1, array2):
    result = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    result.extend(array1[i:])
    result.extend(array2[j:])
    return result



def merge_sort_top_down(array, l, r):
    if l < r:
        mid = (l + r) / 2
        left = merge_sort_top_down(array, l, mid)
        right = merge_sort_top_down(array, mid+1, r)
        return merge(left, right)
    return array[l:r+1]



def merge_1(a, l, m, r):
    n1 = m-l + 1
    n2 = r - m
    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = a[l+i]

    for i in range(n2):
        R[i] = a[m+i+1]
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1
    while i < n1:
        a[k] = L[i]
        k += 1
        i += 1

    while j < n2:
        a[k] = R[j]
        k += 1
        j += 1
        

def merge_sort_bottom_up(array):
    """
    array = [5, 4, 3, 2, 1]
    n = 4
    current_size = 1
    while loop1
        left = 0
        loop1.1
            mid = min(0+1-1, 4) = 0
            right = ((1,4)[2-1 > 4] = ((1,4)[False]) = 1 (False as 0)
            merge(array, 0,0, 1) -> array = [4,5,3,2,1]
            left = 0 + 2 = 2
        loop 1.2
            mid = min(2+1-1, 4) = 2
            right = ((2+2-1, 4))[3 > 4] -> ((3,4)[False]) = 3
            merge(array, 2, 2, 3) -> array = [4, 5, 2, 3, 1]
            left = 2 + 2 = 4
        loop 1.3
            mid = min(4+2, 4) = 4
            right = ((2+4-1, 4)[5 > 4]) = 4
            merge(array, 4, 4, 4) -> array = [4, 5, 2, 3,1]
    current_size = 2
    while loop 2
        left = 0
        loop 2.1
            mid = 0+2-1, 4 = 1
            right = 4+0-1, 4 = 3
            merge(array, 0, 1, 3) -> array = [2, 3, 4, 5, 1]
            left = 4
        loop 2.2
            mid = 4+2-1, 4 = 4
            right = 4+2-1, 4 [True] = 4
            merge(array, 4, 4, 4) -> array = [2, 3, 4, 5, 1]
    current_size = 4
    while loop 3
        left = 0
        loop 3.1
            mid = min(0+4-1, 4) = 3
            right = 2*4+0-1, 4 = 4
            merge(array, 0, 3, 4) -> array = [1, 2, 3, 4, 5]
            left = 0 + 8
            exit
    while loop exits as current size = 8 > 4
    """
    current_size = 1
    n = len(array) - 1
    while current_size <= n:
        left = 0
        while left <= n:
            mid = min((left + current_size - 1),n)
            right = ((2 * current_size + left - 1,  n)[2 * current_size  
                        + left - 1 > n])
            print left, mid, right,
            merge_1(array, left, mid, right)
            print array
            left = left + (2 * current_size)
        current_size *= 2
    return array

        


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        current_size = 1
        n = len(nums) - 1
        
        def merge(a, l, m, r):
            n1 = m-l + 1
            n2 = r - m
            L = [0]*n1
            R = [0]*n2
            for i in range(n1):
                L[i] = a[l+i]

            for i in range(n2):
                R[i] = a[m+i+1]
            i, j, k = 0, 0, l
            while i < n1 and j < n2:
                if L[i] > R[j]:
                    a[k] = R[j]
                    j += 1
                else:
                    a[k] = L[i]
                    i += 1
                k += 1
            while i < n1:
                a[k] = L[i]
                k += 1
                i += 1

            while j < n2:
                a[k] = R[j]
                k += 1
                j += 1
        while current_size <= n:
            left = 0
            while left <= n:
                mid = min((left + current_size - 1),n)
                right = ((2 * current_size + left - 1,  n)[2 * current_size  
                            + left - 1 > n])
                merge(nums, left, mid, right)
                left = left + (2 * current_size)
            current_size *= 2
        return nums
    




print merge_sort_top_down([5,4,3,2,1], 0, 4)
print merge_sort_top_down([6, 5,4,3,2,1], 0, 5)
print merge_sort_top_down([6], 0, 5)

print merge_sort_bottom_up([5,4,3,2,1])
print merge_sort_bottom_up([6, 5,4,3,2,1])
print merge_sort_bottom_up([6])


print Solution().sortArray([5,4,3,2,1])
print Solution1().sortArray([5,4,3,2,1])


