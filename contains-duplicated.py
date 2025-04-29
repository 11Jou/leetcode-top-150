class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numbers = {}
        n = len(nums)
        for i in range(0,n):
            if nums[i] in numbers and abs(i-numbers[nums[i]]) <= k:
                return True
            numbers[nums[i]] = i
        return False