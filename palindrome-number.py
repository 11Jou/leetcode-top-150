class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False
        string = str(x)
        start = 0
        end = len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1

        return True