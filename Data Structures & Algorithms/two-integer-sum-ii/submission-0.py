class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)
        while left < right:
            sum = numbers[left - 1] + numbers[right - 1]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        