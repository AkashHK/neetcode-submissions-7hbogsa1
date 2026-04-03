class Solution:
    def init_heap(self) -> None:
        self.heap_array = []
        self.heap_length = 0
    def add_to_heap(self, freq_map: List[int, int]) -> None:
        print(f"heap is {self.heap_array} and length is {self.heap_length}")
        self.heap_length += 1
        if len(self.heap_array) < self.heap_length:
            self.heap_array.append(freq_map)
        else:
            self.heap_array[self.heap_length - 1] = freq_map
        i = self.heap_length - 1
        while(i > 0):
            if self.heap_array[(i-1)//2][1] < self.heap_array[i][1]:
                self.heap_array[(i-1)//2], self.heap_array[i] = self.heap_array[i], self.heap_array[(i-1)//2]
            i = (i-1) // 2
    def pop_from_heap(self) -> List[int, int]:
        if self.heap_length < 0:
            return
        freq_map = self.heap_array[0]
        self.heap_length -= 1
        self.heap_array[0] = self.heap_array[self.heap_length]
        i = 0
        while(i <= (self.heap_length - 1) // 2):
            greater = i
            left = 2*i + 1
            right = 2*i +2
            if left < self.heap_length and self.heap_array[greater][1] < self.heap_array[left][1]:
                greater = left
            if right < self.heap_length and self.heap_array[greater][1] < self.heap_array[right][1]:
                greater = right
            self.heap_array[i], self.heap_array[greater] = self.heap_array[greater], self.heap_array[i]
            if i != greater:
                i = greater
            else:
                i = self.heap_length + 1
        return freq_map

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = 1 + hash_map.get(nums[i], 0)
        hash_map = [[key, value] for key, value in hash_map.items()]
        self.init_heap()

        print(hash_map)
        for i in range(len(hash_map)):
            self.add_to_heap(hash_map[i])
        # DEBUG
        print(f"HEAP is {self.heap_array}")
        output_list = []
        i = 0
        while (i < k):
            if self.heap_length > 0:
                freq_map = self.pop_from_heap() 
                output_list.append(freq_map[0])
                i += 1
                # DEBUG
                print(f"HEAP is {self.heap_array}")
        return output_list

         
        