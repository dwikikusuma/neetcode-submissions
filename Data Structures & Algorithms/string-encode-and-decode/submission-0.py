class Solution:

    def encode(self, strs: List[str]) -> str:
        dec = ""
        for i in strs:
            dec += f"{len(i)}#{i}"
        
        return dec
            
    def decode(self, s: str) -> List[str]:
        res = []
        slow_p = 0
        fast_p = 0

        while fast_p < len(s):
            if s[fast_p] != "#":
                fast_p += 1
                continue
            
            digit = int(s[slow_p:fast_p])
            res.append(s[fast_p+1:fast_p+digit+1])
            
            slow_p = fast_p+digit+1
            fast_p = fast_p+digit+2
        
        return res
