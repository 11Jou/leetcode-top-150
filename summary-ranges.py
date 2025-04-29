class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        j = len(nums); solution = []
        while len(nums)>0:
            sublist = nums[0:j]
            if sublist[-1] - sublist[0] == len(sublist) - 1:
                if len(sublist) == 1:
                    solution.append(str(nums[0]))
                else:
                    ranges = str(sublist[0]) + "->" + str(sublist[-1])
                    solution.append(ranges)
                nums = nums[j::]
                j = len(nums)
            else:
                j -= 1
        return solution