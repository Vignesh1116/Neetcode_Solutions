# Input: s = "racecar", t = "carrace"

# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)