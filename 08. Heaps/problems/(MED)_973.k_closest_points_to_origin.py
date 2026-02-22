import heapq
from math import sqrt
            
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We basically want to sort our points by distance from origin
        # And we want to return the k elements with the shortest distance
        # So naturally we can use a heap

        # k is guaranteed to be at least 1
        # k is guaranteed to be at most points.length

        min_heap = []

        # O(n) time
        for point in points:
            x, y = point[0], point[1]
            dist_from_origin = sqrt(x**2 + y**2)
            min_heap.append([dist_from_origin, x, y])

        # O(n) time
        heapq.heapify(min_heap)

        # O(n) space
        k_closest_points = []

        # O(k log n) time
        for i in range(k):
            popped = heapq.heappop(min_heap)
            k_closest_points.append([popped[1], popped[2]])

        return k_closest_points


class AlternateSolution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        n = len(points)

        # O(k) time and O(k) space
        # Store the first k elements in a max-heap
        max_heap = []

        for i in range(k):
            point = points[i]
            dist = -(sqrt(point[0] ** 2 + point[1] ** 2))
            max_heap.append([dist, point[0], point[1]])

        heapq.heapify(max_heap)

        # For the next n - k elements, if an element is closer, push it and pop the further one
        # This takes O(n-k log k) time
        for i in range(k, n):
            point = points[i]
            dist = -(sqrt(point[0] ** 2 + point[1] ** 2))

            if abs(dist) < abs(max_heap[0][0]):
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, [dist, point[0], point[1]])
        
        k_closest_points = []

        for point in max_heap:
            k_closest_points.append([point[1], point[2]])

        return k_closest_points