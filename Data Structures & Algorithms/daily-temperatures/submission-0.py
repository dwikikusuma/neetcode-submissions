class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        stack = []

        for idx, temp in enumerate(temperatures):
            if not stack or temp <= temperatures[stack[-1]]:
                stack.append(idx)
                continue
            
            while stack and temperatures[stack[-1]] < temp:
                out = stack.pop()
                ans[out] = idx - out
            
            stack.append(idx)
            
        return ans


            
