from itertools import chain
    
def convertList(numbers):
    """
    Input: list[str]
    Output: list
    """
    return list(filter(lambda x: x != ".", numbers))

def checkValidity(numbers):
    """
    Input: list[list[str]]
    Output: bool
    """
    for i in numbers:
        convertedList = [int(i) for i in convertList(i)]
        if sum(convertedList) != sum(set(convertedList)):
            return False
    return True

class Solution:
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = board
        columns = [list(i) for i in list(zip(*board))]
        squares = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = list(chain(*(row[j:j+3] for row in columns[i:i+3])))
                squares.append(square)
        if checkValidity(rows) and checkValidity(columns) and checkValidity(squares):
            return True
        else:
            return False