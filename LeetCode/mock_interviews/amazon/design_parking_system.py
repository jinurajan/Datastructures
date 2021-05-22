"""
Design Parking System
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.


Constraints:

0 <= big, medium, small <= 1000
carType is 1, 2, or 3
At most 1000 calls will be made to addCar
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {1:big, 2:medium, 3:small}


    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lots = {3: small, 2: medium, 1: big}

    def addCar(self, carType: int) -> bool:
        lot = self.lots[carType]
        if lot != 0:
            self.lots[carType] -= 1
            return True
        else:
            return False


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_cars = big
        self.medium_cars = medium
        self.small_cars = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_cars == 0:
                return False
            self.big_cars -= 1
        elif carType == 2:
            if self.medium_cars == 0:
                return False
            self.medium_cars -= 1
        else:
            if self.small_cars == 0:
                return False
            self.small_cars -= 1
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)