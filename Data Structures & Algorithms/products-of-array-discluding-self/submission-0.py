class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return []
        cur = 0
        output_arr = [num for num in nums]
        prod = 1
        while cur < len(nums):
            output_arr[cur] = prod
            prod *= nums[cur]
            cur += 1
        cur = len(nums) - 1
        prod = nums[cur]
        while cur > 0:
            output_arr[cur - 1] *= prod
            prod *= nums[cur -1]
            cur -= 1
        return output_arr
            
        