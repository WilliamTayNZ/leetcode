class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack: indices of decreasing temperatures
        stack = []

        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                day = stack[-1]
                answer[day] = i-day
                stack.pop()
            stack.append(i)

        return answer