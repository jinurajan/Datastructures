"""
A company is planning to interview 2n people. you are given the array costs where costs[i] = [acosti, bcosti.The cost of flying the ith person to city A is acosti and the cost of flying the ith
person to city B is bcosti

return the minimum cost to fly every person to a city such that exactly n people arrive in each city


costs.length = 2n
2 <= costs.length <= 100

costs.length is always even
1 <= acosti, bcosti<=1000
"""
import math
def two_city_scheduling(costs):
  # Write your code
  min_cost = 0
  difference = sorted(
    [(a-b, a, b) for a, b in costs])
  total_diff = len(difference)
  for i in range(total_diff):
    if i < math.floor(total_diff/2):
      min_cost += difference[i][1]
    else:
      min_cost += difference[i][2]
  
  return min_cost



def main():
    input_costs = [
            [[10, 20], 
            [30, 200], 
            [400, 50], 
            [30, 20]],

            [[259, 770], 
            [448, 54], 
            [926, 667], 
            [184, 139], 
            [840, 118], 
            [577, 469]],

            [[515, 563], 
            [451, 713], 
            [537, 709], 
            [343, 819], 
            [855, 779], 
            [457, 60], 
            [650, 359], 
            [631, 42]],

            [[1, 2], 
            [3, 4], 
            [5, 6], 
            [7, 8]],

            [[1, 2], 
            [1, 2], 
            [1, 2], 
            [1, 2]]]
            
    for i in range(len(input_costs)):
        print("Test Case #", i + 1)
        print(
            "\nThe minimum cost to send people equally into City A and B when the costs are ", input_costs[i], " is:", two_city_scheduling(input_costs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
