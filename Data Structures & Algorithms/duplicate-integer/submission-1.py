class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return not (len(nums) == len(set(nums)) )
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            else:
                hash_map[num] = 1
        return False

        
        
        