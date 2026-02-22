class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            values = self.time_map[key]

            if timestamp < values[0][1]:
                return ""
            elif timestamp >= values[-1][1]:
                return values[-1][0]
            
            left, right = 0, len(values) - 1
            closest_value = ""

            while left <= right:
                mid = (left + right) // 2

                if values[mid][1] == timestamp:
                    return values[mid][0]
                elif values[mid][1] < timestamp:
                    closest_value = values[mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
            
            return closest_value
                
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# December 27th, 2025
# Cool problem