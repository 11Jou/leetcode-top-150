class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}

        for num in nums:
            if num in hash_table:
                hash_table[num] += 1

            else:
                hash_table[num] = 1

        for key, value in hash_table.items():
            if value == 1:
                return key


        