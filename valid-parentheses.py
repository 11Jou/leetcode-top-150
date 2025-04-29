class Solution(object):
    def isValid(self, s):
        my_dict = {'(':1 , ')':1, '{':2, '}':2, '[':3 ,']':3}
        stack = []           
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if stack:
                    current = stack.pop()
                    if my_dict[current] != my_dict[char]:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True