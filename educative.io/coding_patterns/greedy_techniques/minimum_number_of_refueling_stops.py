"""
You need to find the minimum number of refueling stops that a car needs to make to cover a distance, target. For simplicity, assume that the car has to travel from west to east in a straight line. There are various fuel stations on the way that are represented as a 2-D array of stations, i.e., stations[i] 
= [di, fi] where di is the distance (in miles) of the ith gas station from the starting position, and fi is the amount of fuel (in liters) that it stores. 
Initially, the car starts with k liters of fuel. The car consumes one liter of fuel for every mile traveled. Upon reaching a gas station, the car can stop and refuel using all the petrol stored at the station. In case it cannot reach the target, the program simply returns 
-1.
1 <= target, k <= pow(10, 9)
0 <= stations.length <= 900
1 <= di < di+1 < target
1 <= fi < pow(10, 9)
"""

from heapq import *
def min_refuel_stops(target, start_fuel, stations): 
    max_heap = [] # store highest fuel
    if start_fuel >= target:
        return 0
    min_stops = 0
    max_distance = start_fuel
    i, n = 0, len(stations)
    while max_distance < target:
        if i < n and stations[i][0] <= max_distance:
            heappush(max_heap, -stations[i][1])
            i += 1
        elif not max_heap:
            return -1
        else:
            max_distance += -heappop(max_heap)
            min_stops += 1
    return min_stops

def main():
    input = (
              (3, 3, []),
              (59, 14, [[9, 12], [11, 7], [13, 16], [21, 18], [47, 6]]),
              (15, 3, [[2, 5], [3, 1], [6, 3], [12, 6]]),
              (570, 140, [[140, 200], [160, 130], [310, 200], [330, 250]]),
              (1360, 380, [[310, 160], [380, 620], [700, 89], [850, 190],
               [990, 360]])
    )
    num = 1
    for i in input:
        print(num, ".\tStations : ", i[2], sep="")
        print("\tTarget : ", i[0])
        print("\tStarting fuel : ", i[1])
        print("\n\tMinimum number of refueling stops :",
              min_refuel_stops(i[0], i[1], i[2]))
        num += 1
        print("-" * 100, "\n")


if __name__ == "__main__":
    main()
