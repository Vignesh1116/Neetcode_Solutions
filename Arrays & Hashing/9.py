# Longest Consecutive Sequence

# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res