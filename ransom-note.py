class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        while magazine:
            if not ransomNote:
                return True
            stackM = magazine.pop()
            if stackM in ransomNote:
                ransomNote.remove(stackM)
        if ransomNote:
            return False
        else: 
            return True