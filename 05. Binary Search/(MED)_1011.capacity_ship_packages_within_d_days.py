import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Try different values of capacities

        # Min: max(weights)
        # Max: sum(weights)

        def calculateNumberOfDays(weights, capacity):
            days = 1
            day_total = 0

            for weight in weights:
                if day_total + weight <= capacity:
                    day_total += weight
                else:
                    days += 1
                    day_total = weight

            return days

        l = max(weights)
        r = sum(weights)

        while l <= r:
            # try the middle value, to see how many days it takes to ship all
            mid = (l + r) // 2

            # if there are too many days, try higher values of capacities
            if calculateNumberOfDays(weights, mid) > days:
                l = mid + 1

            else: # if calcDays <= days, try smaller values of capacities
                min_capacity = mid
                r = mid - 1

        return min_capacity
            # we return the min valid capacity