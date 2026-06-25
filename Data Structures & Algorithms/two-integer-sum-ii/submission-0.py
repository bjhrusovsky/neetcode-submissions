class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin, end = 0, len(numbers) - 1

        while begin < end:
            if numbers[begin] + numbers[end] == target:
                return [begin+1, end+1]
            elif numbers[begin] + numbers[end] > target:
                end -= 1
            else:
                begin += 1
        