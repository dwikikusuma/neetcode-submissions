class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        res = 0
        operator = {"/", "*", "+", "-"}
        for token in tokens:
            if token not in operator :
                nums.append(int(token))
            else:
                placeholder = 1
                v1 = nums.pop()
                v2 = nums.pop()

                if token == "*":
                    val = v2 * v1
                elif token == "+":
                    val = v2 + v1
                elif token == "-":
                    val = v2 - v1
                elif token == "/":
                    val = int(v2 / v1)  
                nums.append(val)
        
        return nums[0]