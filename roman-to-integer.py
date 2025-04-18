class Solution(object):
    roman = {'I':1 , 'V':5, 'X':10,'L':50 , 'C':100, 'D':500, 'M':1000}
    def romanToInt(self, s):
        ans = 0 
        for i in range(len(s)-1 , -1 , -1):
            num = self.roman[s[i]]
            if 4 * num < ans:
                ans -= num
            else:
                ans += num
        return ans       

