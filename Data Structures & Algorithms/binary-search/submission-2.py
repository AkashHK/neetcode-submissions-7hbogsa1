class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1
        mid = len(nums) // 2
        if mid > 0:
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    temp = self.search(nums[mid+1:], target)
                    return mid + 1 + temp if temp > -1 else -1
                else:
                    temp = self.search(nums[0:mid], target)
                    return temp if temp > -1 else -1
        else:
            return mid if nums[mid] == target else -1
        