class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        prefix = []
        self.premCalc(nums, prefix, result)
        return result

    def premCalc(self, nums, prefix, result):
        if len(nums) == 0:
            result.append(prefix[:])
            return 
        copyNum = set(nums)
        for i in copyNum:
            copyNum.remove(i)
            prefix.append(i)
            self.premCalc(copyNum, prefix, result)
            copyNum.add(i)
            prefix.remove(prefix[-1])