"""
Split a String in Balanced Strings
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        self.counter = 0
        hash_set = {}
        first_elem = s[0]
        send_elem = 'L' if first_elem == 'R' else 'R'
        for i in range(len(s)):
            # already present
            if len(hash_set) == 2:
                diff = hash_set[first_elem][1] - hash_set[send_elem][1]
                if diff == 0:
                    #  RRLL case
                    self.counter += 1
                    hash_set = {}
                    first_elem = s[i]
                    send_elem = 'L' if s[i] == 'R' else 'R'
                elif diff < 0:
                    # RRLLL case
                    self.counter += 1
                    f_val = hash_set.pop(first_elem)
                    first_elem, send_elem = send_elem, first_elem
                    val = hash_set[first_elem]
                    val[0] += f_val[0]
                    val[1] -= f_val[1]
                else:
                    # diff > 0 RRRLL case
                    pass

            if s[i] not in hash_set:
                hash_set[s[i]] = [i, 1]
            else:
                val = hash_set[s[i]]
                val[1] += 1
                hash_set[s[i]] = val
        if len(hash_set) == 2:
            if hash_set[first_elem][1] >= hash_set[send_elem][1]:
                self.counter += 1
        return self.counter


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for w in s:
            if not stack:
                stack.append(w)
            else:
                if stack[-1] == w:
                    stack.append(w)
                else:
                    stack.pop()
                    if not stack:
                        count += 1
        return count


if __name__ == "__main__":
    print Solution().balancedStringSplit("RLRRLLRLRL") == 4
    print Solution().balancedStringSplit("RLLLLRRRLR") == 3
    print Solution().balancedStringSplit("LLLLRRRR") == 1
    print Solution().balancedStringSplit("RLRRRLLRLL") == 2
    print Solution().balancedStringSplit("RL") == 1
