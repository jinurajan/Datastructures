"""

"""

def binarysearch(nums, k):
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = l+(r-l)/2
        if k > mid:
            l = mid+1
        elif k < mid:
            r = mid-1
        else:
            return mid
    return -1