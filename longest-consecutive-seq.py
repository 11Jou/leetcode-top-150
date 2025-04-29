class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        outputs = []; counter = 1

        for i in range(1,len(nums)):
            print(nums[i], nums[i-1])
            if abs(nums[i] - nums[i-1]) == 1:
                counter += 1
            else:
                outputs.append(counter)
                counter = 1
        outputs.append(counter)
        return max(outputs)
        