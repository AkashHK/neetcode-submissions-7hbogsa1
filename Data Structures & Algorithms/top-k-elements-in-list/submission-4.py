class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        heap_array = [(value, num) for num, value in freq_map.items()]
        heapq.heapify_max(heap_array)
        print(f"HEAP is {heap_array}")
        i = 0
        output_list = []
        while i<k:
            output_list.append(heapq.heappop_max(heap_array)[1])
            i += 1
        return output_list
        