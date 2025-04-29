class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        list_dict = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in list_dict:
                list_dict[sorted_s].append(s)
            else:
                list_dict[sorted_s] = [s]

        return list(list_dict.values())

        