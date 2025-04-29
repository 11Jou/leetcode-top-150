class Solution(object):
    def plusOne(self, digits):
        num = ''
        ans = []
        for i in digits:
            num += str(i)
        num = int(num) + 1
        num = str(num)
        for i in num:
            ans.append(int(i))
        return ans

