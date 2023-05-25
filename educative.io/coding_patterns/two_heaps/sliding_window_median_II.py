"""
"""

from heapq import heappush, heappop

# Tip: You may use some of the code templates provided
# in the support files

def find_median(max_heap, min_heap):
    if len(max_heap) == len(min_heap):
        return -max_heap[0] / 2.0 + min_heap[0] / 2.0
    else:
        return -max_heap[0] / 1.0

def rebalance_heaps(max_heap, min_heap):
    if len(max_heap) > len(min_heap) + 1:
        heappush(min_heap, -heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heappush(max_heap, -heappop(min_heap))
    return max_heap, min_heap

def median_sliding_window(nums, k):
    # Your code will replace this placeholder return statement
    print(nums, k)
    max_heap_for_small_nums = []
    min_heap_for_bigger_nums = []
    result = []
    outgoing_num = {}
    n = len(nums)
    for i in range(k):
        heappush(max_heap_for_small_nums, -nums[i])
    
    # now rebalance the k/2 to the min_heap
    for i in range(k//2):
        element = heappop(max_heap_for_small_nums)
        heappush(min_heap_for_bigger_nums, -element)
    
    # now we have equal number of elements on both heaps
    i = k
    while True:
        if (k & 1) == 1:
            # k is odd
            result.append(-max_heap_for_small_nums[0]/1.0)
        else:
            result.append(
                -max_heap_for_small_nums[0] / 2.0 +
                min_heap_for_bigger_nums[0] / 2.0
            )
        if i >= n:
            break
        # outgoing number
        out_num = nums[i-k]

        in_num = nums[i]
        i += 1

        balance = 0
        if out_num <= -max_heap_for_small_nums[0]:
            balance -= 1
        else:
            balance += 1

        if out_num in outgoing_num:
            outgoing_num[out_num] += 1
        else:
            outgoing_num[out_num] = 1
        
        if max_heap_for_small_nums and in_num <= -max_heap_for_small_nums[0]:
            balance += 1
            heappush(max_heap_for_small_nums, -in_num)
        else:
            balance -= 1
            heappush(min_heap_for_bigger_nums, in_num)
            
        if balance < 0:
            heappush(max_heap_for_small_nums, -min_heap_for_bigger_nums[0])
            heappop(min_heap_for_bigger_nums)
        elif balance > 0:
            heappush(min_heap_for_bigger_nums, -max_heap_for_small_nums[0])
            heappop(max_heap_for_small_nums)
        
        while max_heap_for_small_nums and (-max_heap_for_small_nums[0] in outgoing_num) and (outgoing_num[-max_heap_for_small_nums[0]] > 0):
            outgoing_num[-max_heap_for_small_nums[0]] -= 1
            heappop(max_heap_for_small_nums)

        while (min_heap_for_bigger_nums and min_heap_for_bigger_nums[0] in outgoing_num) and (outgoing_num[min_heap_for_bigger_nums[0]] > 0):
            outgoing_num[min_heap_for_bigger_nums[0]] -= 1
            heappop(min_heap_for_bigger_nums)
    return result            

def main():
    input = (
            ([3, 1, 2, -1, 0, 5, 8],4), 
            ([1, 2], 1), 
            ([4, 7, 2, 21], 2), 
            ([22, 23, 24, 56, 76, 43, 121, 1, 2, 0, 0, 2, 3, 5], 5), 
            ([1, 1, 1, 1, 1], 2))
    x = 1
    for i in input:
        print(x, ".\tInput array: ", i[0],  ", k = ", i[1], sep = "")
        print("\tMedians: ", median_sliding_window(i[0], i[1]), sep = "")
        print(100*"-", "\n", sep = "")
        x += 1


if __name__ == "__main__":
    main()