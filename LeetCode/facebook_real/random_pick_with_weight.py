



class Solution:

    def __init__(self, w: List[int]):
        self.sums = []
        sum = 0
        for weight in w:
            sum += weight
            self.sums.append(sum)
        self.total = sum
        

    def pickIndex(self) -> int:
        target = random.randint(0, self.total)
        low = 0
        high = len(self.sums) - 1
        while low < high:
            mid = (low + high) // 2
            if self.sums[mid] > target:
                high = mid
            else:
                low = mid+1
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()