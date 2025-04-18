class Solution(object):
    def lengthOfLongestSubstring(self,s):
        ans = ''
        maximum = 0
        if len(s) == 1:
            return 1
        for i in range(0,len(s)-1):
            ans = s[i]
            for j in range(i+1,len(s)):
                if s[j] not in ans:
                    ans += s[j]
                    if len(ans) > maximum:
                        maximum = len(ans)
                else:
                    if len(ans) > maximum:
                        maximum = len(ans)
                    break
        return maximum