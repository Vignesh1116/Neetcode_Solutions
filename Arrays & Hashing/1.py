# Input: nums = [1, 2, 3, 3]

# Output: true


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False

       
