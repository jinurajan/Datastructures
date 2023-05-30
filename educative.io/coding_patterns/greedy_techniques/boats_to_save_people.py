"""
Youre given an array, people, where people[i] is the weight of the ith person, and an infinite number of boats, where each boat can carry a maximum weight, limit. Each boat carries, at most, two people at the same time. This is provided that the sum of the weight of those people is under or equal to the weight limit.

You need to return the minimum number of boats to carry every person in the array.

1. each boat has maximum weight called limit
2. each index has passengers weight
3. boat carries atmost two people at the same time
"""

def rescue_boats(people, limit):
    # Replace the placeholder return statement below with your code
    # Tip: You may use the code template provided
    # in the two_pointers.py file
    people.sort()
    light = 0
    heavy = len(people)-1
    count = 0
    while light <= heavy:
        count += 1
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
    return count

def main():
    people = [[1, 2], [3, 2, 2, 1], [3, 5, 3, 4], [
        5, 5, 5, 5], [1, 2, 3, 4], [1, 2, 3, 4, 5], [3, 4, 5]]
    limit = [3, 3, 5, 5, 5, 3, 1]
    for i in range(len(people)):
        print(i + 1, "\tWeights = ", people[i], sep="")
        print("\tWeight Limit = ", limit[i], sep="")
        print("\tThe minimum number of boats required to save people are ",
              rescue_boats(people[i], limit[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()