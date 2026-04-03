class Solution:
    def isValidGroup(self, nums: List[str]) -> bool:
        cnt = {}
        for num in nums:
            if num.isdigit():
                if num in cnt:
                    return False
                else:
                    cnt[num] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        res = True
        sqrt_n = int(math.sqrt(len(board)))
        for length in range(len(board)):
            res = res and self.isValidGroup(board[length])
        for breadth in range(len(board[0])):
            temp_group = []
            for length in range(len(board)):
                temp_group.append(board[length][breadth])
            res = res and self.isValidGroup(temp_group)
        starter_points = []
        length, breadth = 0, 0
        while(length < len(board)):
            while(breadth < len(board)):
                starter_points.append((length, breadth))
                breadth += sqrt_n
            length += sqrt_n
        for start in starter_points:
            temp_group = []
            length, breadth = start[0], start[1]
            for i in range(sqrt_n):
                for j in range(sqrt_n):
                    temp_group.append(board[length + i][breadth + j])
            res = res and self.isValidGroup(temp_group)
        return res
                


        