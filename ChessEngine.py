'''
responsible for storing game data. It is also responsible for determining the valid moves at the current state. It will also keep a move log.
'''

class GameState():
    def __init__(self):
        #This array is the game data, which shows the 8*8 board. 
        #The color of the piece is symbolized by the first letter of the element (either b or w representing the black or white color).
        #The type of the piece is symbolized by the second letter.
        #Empty space is represented by '--'
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove


class Move():
    ranksToRows = {'1': 7,'2': 6,'3': 5,'4': 4,
                   '5': 3,'6': 2,'7': 1,'8': 0}
    rowsToRanks = {v:k for k, v in ranksToRows.items()}
    filesToCol = {'a': 0,'b': 1,'c': 2,'d': 3,
                  'e': 4,'f': 5,'g': 6,'h': 7}
    colToFiles = {v:k for k, v in filesToCol.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
    
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    

    def getRankFile(self, r, c):
        return self.colToFiles[c] + self.rowsToRanks[r]