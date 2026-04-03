class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums)
        res, max_res = 1, 1
        for num in nums:
            if (num - 1) not in hash_set:
                while True:
                    if (num + 1) in hash_set:
                        res += 1
                        num += 1
                    else:
                        max_res = max(max_res, res)
                        res = 1
                        break
        return max_res