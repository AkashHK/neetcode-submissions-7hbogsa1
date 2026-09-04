class Solution:
    def countBits(self, n: int) -> List[int]:
        count_list = []
        for i in range(n+1):
            res = 0
            while i:
                res += 1
                i &= i-1
            count_list.append(res)
        return count_list
        