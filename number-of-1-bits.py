class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n).replace("0b", ""); bits = 0
        for bit in n:
            if bit == '1':
                bits += 1

        return bits
        