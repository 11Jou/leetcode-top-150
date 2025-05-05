import random
class RandomizedSet(object):

    def __init__(self):
        self.array = []
        self.idx = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.idx:
            return False
        self.array.append(val)
        self.idx[val] = len(self.array) - 1
        return True
        
    def remove(self, val):
        if val not in self.idx:
            return False
        last_element = self.array[-1]
        index_to_remove = self.idx[val]
        self.array[index_to_remove] = last_element
        self.idx[last_element] = index_to_remove
        self.array.pop()
        del self.idx[val]
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()