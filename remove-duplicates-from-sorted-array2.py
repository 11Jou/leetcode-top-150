class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] in nums_dict:
                if nums_dict[nums[i]] == 2:
                    nums[i] = None
                else:
                    nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1

        nums[:] = [num for num in nums if num is not None]
        return len(nums)