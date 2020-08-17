"""
Distribute Candies to People
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000
"""
from math import sqrt, ceil


class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        if not candies:
            return []
        l = int(ceil(sqrt(candies)))
        r = int(ceil(sqrt(candies*2)))
        max_distrib_count = find_n(candies, l, r, l)
        no_of_iter = max_distrib_count // num_people
        result = [0] * num_people
        if no_of_iter:
            # sum of arithmetic progression with d = num_people
            # n/2 (2a+ (n-1)*d) where a is i+1 and d is num_people
            result = [int((no_of_iter/2.0) * ((2*(i+1)) + (no_of_iter-1)* num_people)) for i in range(0, num_people)]
        # nth value in arithmetic progression starting with 1 with d = num_people
        # is 2a + (n-1)*d
        total_so_far = int((no_of_iter * num_people)*((no_of_iter*num_people)+1) / 2.0) if no_of_iter else 0
        balance = candies - total_so_far
        start_value = (no_of_iter * num_people) + 1
        # print total_so_far, balance, start_value
        i = 0
        while balance > 0:
            if i  >= num_people:
                i = 0
            if balance < start_value:
                result[i] += balance
                break
            result[i] += start_value
            balance -= start_value
            start_value += 1
            i += 1

        return result


def find_n(n, l, r, val):
    if l <= r:
        mid = (l+r) // 2
        mid_sum = (mid * (mid+1)) // 2
        val_sum = ((val* (val+1)) // 2)
        if mid_sum == val_sum:
            return val
        if mid_sum <= n and mid_sum >= val_sum:
            val = mid
        if mid_sum > n:
            # find on the left side
            return find_n(n, l, mid, val)

        else:
            # find on the left side
            return find_n(n, mid, r, val)
    return val


print(Solution().distributeCandies(7, 4))
print(Solution().distributeCandies(10, 3))
print(Solution().distributeCandies(60, 4))
print(Solution().distributeCandies(90, 4))
print(Solution().distributeCandies(130, 4))

# l = int(ceil(sqrt(60)))
# r = int(ceil(sqrt(120)))
# print(find_n(60, l, r, l))

# l = int(ceil(sqrt(90)))
# r = int(ceil(sqrt(180)))
# print(find_n(90, l, r, l))
