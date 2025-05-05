class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        array_words = s.split(' ')
        ans = []
        for word in array_words:
            if len(word) > 0:
                ans.append(word)

        return " ".join(ans[len(ans) - 1::-1])
        