class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_xor = array_xor = 0
        for num in nums:
            array_xor ^= num
        for i in range(len(nums) + 1):
            total_xor ^= i
        return total_xor ^ array_xor
