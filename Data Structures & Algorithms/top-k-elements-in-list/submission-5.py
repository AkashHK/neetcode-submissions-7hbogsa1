class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        freq_cnt = [[] for i in range(len(nums) + 1)]
        for num, value in freq_map.items():
            freq_cnt[value].append(num)
        res = []
        i = len(freq_cnt) - 1
        while i >= 0:
            for num in freq_cnt[i]:
                res.append(num)
                if len(res) == k:
                    return res
            i -= 1
        