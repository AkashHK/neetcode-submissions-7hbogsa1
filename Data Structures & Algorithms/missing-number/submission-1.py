class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += num
        total_sum = (len(nums) * (len(nums) + 1)) // 2
        return total_sum - res
        