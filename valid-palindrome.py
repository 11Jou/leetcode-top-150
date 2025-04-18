class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([x for x in s if x.isalnum()])
        s = s.lower()
        if len(s) <= 1:
            return True 

        mid = len(s) // 2

        if len(s) % 2 == 0:
            return s[0:mid] == s[len(s)-1:mid-1:-1]



        return s[0:mid] == s[len(s)-1:mid:-1]
        