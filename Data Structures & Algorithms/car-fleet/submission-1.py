class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in pair:
            arrival = (target - p) / s
            stack.append(arrival)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)