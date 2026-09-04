class Solution:
    def countBits(self, n: int) -> List[int]:
        count_list = [0]
        res = 1
        for i in range(1, n+1):
            count_list.append(res + count_list[i//2])
            res = 1 - res 
        return count_list
        