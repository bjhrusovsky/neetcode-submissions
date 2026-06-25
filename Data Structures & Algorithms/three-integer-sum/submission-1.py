class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        
        for index, number in enumerate(nums):

            if number > 0:
                break
            if index > 0 and number == nums[index - 1]:
                continue


            begin, end = index + 1, len(nums) - 1
            while begin < end:
                currTotal = number + nums[begin] + nums[end]
                if currTotal == 0:
                    answers.append([number, nums[begin], nums[end]])
                    end -= 1
                    begin += 1
                    while nums[begin] == nums[begin - 1] and begin < end:
                        begin += 1
                elif currTotal > 0:
                    end -= 1
                else:
                    begin += 1
        return answers
                