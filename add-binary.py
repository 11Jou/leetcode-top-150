class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2); b = int(b,2)
        sum_ab = a + b
        return bin(sum_ab).replace('0b','')
        