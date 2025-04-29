class Solution(object):
    def isHappy(self, n,visited=None):
        if visited is None:
            visited = set()
        if n == 1:
            return True
        if n in visited:
            return False

        visited.add(n)

        new_num = sum(int(i)**2 for i in str(n))

        return self.isHappy(new_num,visited)
            