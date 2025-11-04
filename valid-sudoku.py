class Solution:
    def isValidSudoku(self, board) -> bool:

        for row in range(9):
            if(not self.isValidRow(row, board)):
                return False

        
        for col in range(9):
            if(not self.isValidCol(col, board)):
                return False

        boxes = self.getAllBox(board)
        for box in range(9):
            if(not self.isValidBox(boxes[box])):
                return False
        return True

    def isValidRow(self, row, board):
        freq = {}
        for col in range(9):
            i = board[row][col]
            if i != ".":
                if i in freq:
                    return False
                else:
                    freq[i] = 1
        return True

    def isValidCol(self, col, board):
        freq = {}
        for row in range(9):
            i = board[row][col]
            if i != ".":
                if i in freq:
                    return False
                else:
                    freq[i] = 1
        return True

    def isValidBox(self, box):
        freq = {}
        for row in range(9):
            i = box[row]
            if i != ".":
                if i in freq:
                    return False
                else:
                    freq[i] = 1
        return True


    def getAllBox(self, board):
        allBoxes = []

        for boxRow in range(3):
            for boxCol in range(3):
                rowStart = boxRow * 3
                colStart = boxCol * 3
                box = []
                for row in range(rowStart ,rowStart + 3):
                    for col in range(colStart ,colStart + 3):
                        box.append(board[row][col])
                allBoxes.append(box)
        return allBoxes

        