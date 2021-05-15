"""
First Unique Number
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.


Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]
Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
Example 2:

Input:
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output:
[null,-1,null,null,null,null,null,17]
Explanation:
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17
Example 3:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output:
[null,809,null,-1]
Explanation:
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
"""

from collections import OrderedDict
from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.orderedDict = OrderedDict()
        self.dups = set()
        for num in nums:
            if num not in self.dups:
                if num not in self.orderedDict:
                    self.orderedDict[num] = 1
                else:
                    del self.orderedDict[num]
                    self.dups.add(num)

    def showFirstUnique(self) -> int:
        for num in self.orderedDict:
            return num
        return -1

    def add(self, value: int) -> None:
        if value not in self.dups:
            if value in self.orderedDict:
                del self.orderedDict[value]
                self.dups.add(value)
            else:
                self.orderedDict[value] = 1

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counter = OrderedDict()
        self.uniq = 0
        for num in nums:
            if num not in self.counter:
                self.uniq += 1
                self.counter[num] = 1
            else:
                self.counter[num] += 1

    def showFirstUnique(self) -> int:
        if not self.uniq:
            return -1
        for num, count in self.counter.items():
            if count == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        if value in self.counter:
            self.counter[value] += 1
            self.counter.move_to_end(value)
        else:
            self.counter[value] = 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)