"""
Car Pooling

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
"""
from itertools import accumulate

class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        1. find the maximum destination 
        2. create an array starting from 0 to max val
        3. keep adding the total number of passengers in start
        4. remove dropping passengers using end values
        5. accumulate the list to see if there is any time it exceeds the capacity
        return False if so return True otherwise
        """
        m = max([i for _,_,i in trips]) #find the maximum endpoint
        times = [0]*(m+1)   # using m+1 from 0 to max value 
        for pass_count, start, end in trips:
            times[start] += pass_count
            times[end] -= pass_count
        return max(accumulate(times)) <= capacity

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        1. create an array with start end values with passenger count
        2. sort the array
        3. iterate through array and reduce from capacity if capacity ever goes below 0 means 
        exceeded capacity at some point return False 
        4. return True otherwise
        """
        stops = []
        for pass_count, start, end in trips:
            stops.append((start, pass_count))
            stops.append((end, -pass_count))
        print(stops)
        stops.sort()
        print(stops)

        for _, pass_count in stops:
            capacity -= pass_count
            if capacity < 0:
                return False
        return True





        


        

print(Solution().carPooling([[2,1,5],[3,3,7]], 4) == False)
print(Solution().carPooling([[2,1,5],[3,3,7]], 5) == True)
print(Solution().carPooling([[2,1,5],[3,5,7]], 3) == True)
print(Solution().carPooling([[3,2,7],[3,7,9],[8,3,9]], 11) == True)
print(Solution().carPooling([[2,2,6],[2,4,7],[8,6,7]], 11) == True)
print(Solution().carPooling([[7,5,6],[6,7,8],[10,1,6]], 16) == False)





