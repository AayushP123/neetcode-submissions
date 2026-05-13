class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if stack[j] == 0:
                    j = n
                    break
                j += stack[j]

            if j < n:
                stack[i] = j - i
        return stack