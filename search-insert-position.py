class Solution(object):
    def searchInsert(self, nums, target):
        expected_index = 0 
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if target > nums[i]:
                expected_index = i + 1
        return expected_index
