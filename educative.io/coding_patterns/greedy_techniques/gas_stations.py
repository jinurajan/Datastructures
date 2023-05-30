"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

We have a car with an unlimited gas tank, and it costs cost[i] of gas to travel from the ith station to the next (i+1) th
station. We begin the journey with an empty tank at one of the gas stations.

Find the index of the gas station in the integer array gas such that if we start from that index we may return to the same index by traversing through all the elements, collecting gas[i] and consuming cost[i].

If it is not possible, return -1.

If there exists such index, it is guaranteed to be unique.

- gas.length == cost.length
- 1 <= gas.length, cost.length <= pow(10, 3)
- 0 <= gas[i], cost[i] <= pow(10, 3)
"""

def gas_station_journey(gas, cost):
    # Your code will replace this placeholder return statement
    total_gas = sum(gas)
    total_cost = sum(cost)
    if total_gas < total_cost:
        return -1
    start_index = 0
    curr_gas = 0
    for i in range(len(gas)):
        curr_gas = curr_gas + (gas[i]-cost[i])
        if curr_gas < 0:
            curr_gas = 0
            start_index = i + 1
    return start_index

def main():
    gas = [[1, 2, 3, 4, 5], [2, 3, 4], [1, 1, 1, 1, 1], [
        1, 1, 1, 1, 10], [1, 1, 1, 1, 1], [1, 2, 3, 4, 5]]
    cost = [[3, 4, 5, 1, 2], [3, 4, 3], [1, 2, 3, 4, 5], [
        2, 2, 1, 3, 1], [1, 0, 1, 2, 3], [1, 2, 3, 4, 5]]
    for i in range(len(gas)):
        print(i+1, ".\tGas = ", gas[i])
        print("\tCost = ", cost[i])
        print("\n \tThe index of the gas station we can start our journey from is ", gas_station_journey(
            gas[i], cost[i]), " (If it's -1, then that \n \tmeans no solution exists)", sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
