"""
Gas Station (Medium)

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""
class Solution1(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int_
        """
        n = len(gas)

        def get_cost(gas, cost, start_index, n):
            T = gas[start_index]
            gas_no = start_index+1 if start_index != n-1 else 0
            while gas_no < n:
                if gas_no == 0:
                    cost_val = cost[-1]
                else:
                    cost_val = cost[gas_no-1]
                gas_val = T - cost_val
                if gas_val >= 0:
                    if gas_no == start_index:
                        print "completed one round"
                        return start_index
                    T = gas_val + gas[gas_no]
                    gas_no += 1
                else:
                    T = 0
                    return -1
                if gas_no == n:
                    gas_no = 0
                
        for i in range(n):
            start_index = get_cost(gas, cost, i, n)
            if start_index >= 0:
                return start_index
        return -1



class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int_
        
        [1, 2, 3, 4, 5]
        [3, 4, 5, 1, 2]

        sum(gas) = 15 sum(cost) = 15
        
        loop 1
        ------

        gas_tank = 0 start_index = 0
        i = 0
        gas_tank = 1-3 = -2
        start_index = 1
        gas_tank = 0

        loop 2
        ------
        i = 1
        gas_tank = -2
        start_index = 2
        gas_tank = 0

        loop 3
        ------
        i = 2
        gas_tank = -2
        start_index = 3
        gas_tank = 0

        loop 4
        ------
        i = 3
        gas_tank = 3
        
        loop 5
        ------
        i = 4
        gas_tank = 
        

        """
        if sum(gas) < sum(cost):
            return -1
        T, start_index = 0, 0
        for i in range(len(gas)):
            T += gas[i] - cost[i]
            if T < 0:
                start_index = i+1
                T = 0
        return start_index



print Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
print Solution().canCompleteCircuit([2,3,4], [3, 4, 3])



 
                
        



