class Solution(object):
    def twoSum(self, nums, target):
        ans = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in ans:
                return [ans[diff] , i]
            else:
                ans[nums[i]] = i