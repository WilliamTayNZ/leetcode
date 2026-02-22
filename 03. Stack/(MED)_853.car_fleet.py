class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Change position array to an array of (position, speed) tuples
        n = len(position)
        for i in range(n):
            position[i] = (position[i], speed[i])

        # Step 2: Sort in descending order
        position.sort()
        position.reverse()
        
        # Descending order because the key to this problem is figuring out whether a car
        # that started in front of another car is expected to reach the target later than
        # this other car, meaning the car that started behind has to slow down at some point

        # You can't go in ascending order because you then won't know if a car actually slows 
        # down before you decide whether it's in a fleet.


        # Step 3: Create arrival array (creating this way is more efficient)
        arrival = [0] * n

        for i in range(n):
            car_position = position[i][0]
            car_speed = position[i][1]

            arrival_time = (target - car_position) / car_speed
            arrival[i] = arrival_time

        # position = [(8, 4), (7, 4), (6, 4), (5, 4), (4, 4), (3, 4)]

        # Step 4: Maintain monotonic stack
        stack = []
        number_of_fleets = 0 

        for i in range(n):
            while len(stack) > 0 and arrival[i] > arrival[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                number_of_fleets += 1

            stack.append(i)

        return number_of_fleets

# December 19th, 2025