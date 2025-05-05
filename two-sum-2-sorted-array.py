class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0 ; j = len(numbers) - 1

        while i < j:
            test_target = numbers[i] + numbers[j]
            if test_target == target:
                return [i+1, j+1]

            elif test_target > target:
                j -= 1

            else:
                i += 1
                