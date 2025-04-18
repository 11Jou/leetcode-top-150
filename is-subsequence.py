class Solution(object):
    def isSubsequence(self, s, t):
        for i in s:
            index = t.find(i)
            if index == -1:
                return False
            else:
                t = t[index+1:]
        return True
                