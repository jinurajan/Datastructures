"""
Given a string s consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments within the substring between the two indices, inclusive.

An item is represented as an asterisk *
A compartment is represented as a pair of pipes | that may or may not have items between them.
Example:
s = '|**|*|*'
startIndices = [1,1]
endIndices = [5,6]

The String has a total 2 closed compartments, one with 2 items and one with 1 item. For the first par of indices, (1,5), the substring is '|**|*'. There are 2 items in a compartment.
For the second pair of indices, (1,6), the substring is '|**|*|' and there 2+1=3 items in compartments.
Both of the answers are returned in an array. [2,3].


"""

def numberOfItems(s, startIndices, endIndices):
    sum_map = {}
    cumulative_sum = 0
    sum_val = 0
    started = False
    for i, char in enumerate(s):
        if char == '|':
            if started:
                # left or right boundary
                cumulative_sum += sum_val
                sum_map[i + 1] = cumulative_sum
            else:
                sum_map[i + 1] = 0
            started = True
            sum_val = 0
        else:
            # these are items
            sum_val += 1
    print(sum_map)
    left_boundary = []
    right_boundary = []
    left = -1
    for i, char in enumerate(s):
        if char == '|':
            left = i
        left_boundary.append(i)

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '|':
            right = i
        right_boundary.append(i)
    print(left_boundary)
    print(right_boundary)
    result = []
    # assuming the length of the startIndices and endIndices are equal
    n = len(startIndices)
    for i in range(n):
        start_idx, end_idx = left_boundary[startIndices[i]-1], right_boundary[endIndices[i]-1]
        if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
            result.append(sum_map[end_idx] - sum_map[start_idx])
        else:
            result.append(0)
    return result

def numberOfItems1(s, startIndices, endIndices):
    # Write your code here
    # preprocess the items to have the sum of items and boundaries to reduce computation
    # keep count on left and right boundaries
    count = 0
    total = 0
    left_bound = []
    right_bound = []
    n = len(s)
    for i, char in enumerate(s):
        if char == '|':
            count = total
        else:
            total += 1
        right_bound.append(count)
    count = 0
    total = 0
    for i in range(n - 1, -1, -1):
        if s[i] == "|":
            count = total
        else:
            total += 1
        left_bound.append(count)
    result = []
    for i in range(len(startIndices)):
        start, end = startIndices[i] - 1, endIndices[i] - 1
        count = left_bound[start] + right_bound[end] - total
        if start >= 0 and end <= n - 1 and start < end and count > 0:
            result.append(count)
        else:
            result.append(0)
    return result


s = '|**|*|*'
startIndices = [1,1]
endIndices = [5,6]
