"""
You’re given two sorted integer arrays, nums1 and nums2, of size mand n, respectively. Your task is to return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n))
"""

def get_median(a, b, idx):
    if not a:
        return b[idx]
    if not b:
        return a[idx]
    ai = len(a) // 2
    bi = len(b) // 2

    ma = a[ai]
    mb = b[bi]

    if ma > mb:
        # get the longest list
        ma, mb = mb, ma
        ai, bi = bi, ai
        a, b = b, a
    max_idx_ma = len(a)// 2 + len(b) // 2

    if max_idx_ma < idx:
        med = get_median(a[ai+1:], b, idx - (len(a)//2+1))
    else:
        med = get_median(a, b[:bi], idx)
    return med
    


def find_median(nums1, nums2):
    l =  len(nums1) + len(nums2)
    if l % 2:
        return get_median(nums1, nums2, l//2)/1.0
    else:
        return get_median(nums1, nums2, l//2)/2.0 + get_median(nums1, nums2, l//2-1)/2.0

def find_median(nums1, nums2):
    # the return type of this function should be float
    # your code will replace the placeholder statement below
    m = len(nums1)
    n = len(nums2)
    mid = ((m+n) // 2) + 1
    prev2 = prev1 = None
    i, j = 0,0
    for _ in range(mid):
        prev2 = prev1
        if j == n or (i != m and nums1[i] <= nums2[j]):
            prev1 = nums1[i]
            i += 1
        else:
            prev1 = nums2[j]
            j += 1

    return prev1/1.0 if (m+n) % 2 else (prev1+prev2) / 2.0 



