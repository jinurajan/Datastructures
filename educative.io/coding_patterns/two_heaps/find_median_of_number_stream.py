"""
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
"""


import heapq
class MedianOfAStream:

  min_heap = []
  max_heap = []
  def insert_num(self, num):
    if not self.max_heap or -self.max_heap[0] >= num:
      heapq.heappush(self.max_heap,-num)
    else:
      heapq.heappush(self.min_heap, num)
    if len(self.max_heap) > len(self.min_heap) + 1:
      heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    elif len(self.min_heap) > len(self.max_heap):
      heapq.heappush(self.max_heap, heapq.heappop(self.min_heap))

  def find_median(self):
    # TODO: Write your code here
    if len(self.min_heap) == len(self.max_heap):
      return self.min_heap[0] / 2.0 + - self.max_heap[0] / 2.0
    else:
      return -self.max_heap[0] / 1.0

    return 0.0


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()
