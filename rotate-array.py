class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        result = [0] * len(nums) 
        j = 0

        for i in range(k, len(nums)):
            result[i] = nums[j]
            j += 1

        for i in range(0,k):
            result[i] = nums[j]
            j+=1

        nums[:] = result


        