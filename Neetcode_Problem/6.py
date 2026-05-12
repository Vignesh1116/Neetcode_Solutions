from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        op=""
        for i in strs:
            op+=str(len(i))+i
        return op



    def decode(self, s: str) -> List[str]:
        op = []
        
        while s:
            # find position of '#'
            i = s.find("#")
            
            # extract number
            num = int(s[:i])
            
            # extract string
            item = s[i+1:i+1+num]
            op.append(item)
            
            # move forward
            s = s[i+1+num:]
        
        return op


sol=Solution()
print(sol.encode(["h2i","i","am","gokul"]))

# why do we need #
# why not just the numbers