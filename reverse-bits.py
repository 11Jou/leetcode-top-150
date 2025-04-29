class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n).replace("0b", "")
        diff = 32 - len(n)
        if diff != 0:
            n = diff * "0" + n
        n = n[::-1]
        return int(n,2)                