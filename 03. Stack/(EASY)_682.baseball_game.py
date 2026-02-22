class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:
            if operation == "+":
                score1 = scores[-1]
                score2 = scores[-2]
                scores.append(score1 + score2)
            elif operation == "D":
                latest_score = scores[-1]
                scores.append(latest_score * 2)
            elif operation == "C":
                scores.pop()
            else:
                # We can assume the other token is an integer. This is better than checking String.isdigit() since it returns false for negative numbers 
                scores.append(int(operation))

        return sum(scores)