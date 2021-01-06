# https://leetcode.com/problems/design-parking-system/

import sys

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.storage = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        carType -= 1
        if carType > len(self.storage):
            sys.exit(0)
        if self.storage[carType] > 0:
            self.storage[carType] -= 1
            return True
        else:
            return False