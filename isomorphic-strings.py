class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s = {}; hash_t = {}

        for charS , charT in zip(s,t):
            if charS in hash_s and hash_s[charS] != charT :
                return False

            if charT in hash_t and hash_t[charT] !=charS:
                return False

            hash_s[charS] = charT
            hash_t[charT] = charS

        return True


        