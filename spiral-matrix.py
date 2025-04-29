class Solution(object):
    def spiralOrder(self, matrix):
        answer = []
        col = len(matrix[0]) #3
        row = len(matrix) #3
        size = col * row
        xrow = 0
        xcol = 0
        while len(answer) < size:
            j = xcol
            while j <= col-1 and len(answer) < size:
                answer.append(matrix[xrow][j])
                j += 1 # 1 2 3
            i = xrow + 1 # 1
            while i <= row - 1 and len(answer) < size:
                answer.append(matrix[i][col-1])
                i += 1
            j = col - 1 - 1
            while j >= xcol and len(answer) < size:
                answer.append(matrix[row-1][j])
                j -= 1
            i = row - 1 - 1
            while i >= xrow + 1 and len(answer) < size:
                answer.append(matrix[i][xcol])
                i -= 1
            xrow += 1
            xcol += 1
            row -= 1
            col -= 1
        return answer
