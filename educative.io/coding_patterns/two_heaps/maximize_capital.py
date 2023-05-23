"""
A busy investor with an initial capital, c, needs an automated investment program. They can select k distinct projects from a list of n projects with corresponding capitals requirements and expected profits. The goal is to maximize their cumulative capital by selecting a maximum of k distinct projects to invest in, subject to the constraint that the investor’s current capital must be greater than or equal to the capital requirement of all selected projects.

When a selected project from the identified ones is finished, the investor will obtain its pure profit, and the amount will be added to the total capital. Now, the investor can invest in more projects with the new total capital. It is important to note that each project can only be invested once.

As a basic risk-mitigation measure, the investor wants to limit the number of projects they invest in. For example, if k is 
2
2
, the program should identify the two projects that maximize the investor’s profits while ensuring that the investor’s capital is sufficient to invest in the projects.

Overall, the program should help the investor to make informed investment decisions by picking a list of a maximum of k distinct projects to maximize the final profit while mitigating the risk.

"""

from heapq import *

def maximum_capital(c, k, capitals, profits):
  # replace the dummy return with your code
  capitals_min_heap = []
  profit_max_heap = [] 
  current_capital = c
  for idx, capital in enumerate(capitals):
    heappush(capitals_min_heap, (capital,idx))
   
  for i in range(k):
    while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
      biz_capital, idx = heappop(capitals_min_heap)
      heappush(profit_max_heap, (-profits[idx], idx))
    if not profit_max_heap:
      break
    profit, _ = heappop(profit_max_heap)
    current_capital += -profit

  return current_capital
 

def main():
    input = (
              (0, 1, [1, 1, 2], [1 ,2, 3]),
              (1, 2, [1, 2, 2, 3], [2, 4, 6, 8]),
              (2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
              (1, 3, [1, 2, 3, 4], [1, 3, 5, 7]),
              (7, 2, [6, 7, 8, 10], [4, 8, 12, 14]),
              (2, 4, [2, 3, 5, 6, 8, 12], [1, 2, 5, 6, 8, 9])
            )
    num = 1
    for i in input:
        print(f"{num}.\tProject capital requirements:  {i[2]}")
        print(f"\tProject expected profits:      {i[3]}")
        print(f"\tNumber of projects:            {i[1]}")
        print(f"\tStart-up capital:              {i[0]}")
        print("\n\tMaximum capital earned: ",
              maximum_capital(i[0], i[1], i[2], i[3]))
        print("-" * 100, "\n")
        num += 1


if __name__ == "__main__":
    main()