# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0] * n

        for i in range(n):
            pro = 1
            for j in range(n):
                if i == j:
                    continue
                pro *=nums[j]
            res[i] = pro
        return res
