class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maj = len(nums) // 2

        numbers = {}

        for i in nums:
            if i in numbers:
                numbers[i]+= 1
            else:
                numbers[i] = 1
            
            if numbers[i] > maj:
                return i
        