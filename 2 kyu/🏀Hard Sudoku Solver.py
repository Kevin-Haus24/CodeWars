# class sudoku:
#     def __int__(self, puzzle):
#         self.puzzle = puzzle
#
#     def find_x(self, ind):
#         ans = set(self[ind])
#         return ans
#
#     def find_y(self, ind):
#         ans = set()
#         for i in range(len(self)):
#             ans.add(self[i][ind])
#         return ans
#
# def sudoku_solver(puzzle):
#     # pos x
#     x1 = sudoku.find_x(puzzle, 0)
#     x2 = sudoku.find_x(puzzle, 1)
#     x3 = sudoku.find_x(puzzle, 2)
#     x4 = sudoku.find_x(puzzle, 3)
#     x5 = sudoku.find_x(puzzle, 4)
#     x6 = sudoku.find_x(puzzle, 5)
#     x7 = sudoku.find_x(puzzle, 6)
#     x8 = sudoku.find_x(puzzle, 7)
#     x9 = sudoku.find_x(puzzle, 8)
#     # pos y
#     y1 = sudoku.find_y(puzzle, 0)
#     y2 = sudoku.find_y(puzzle, 1)
#     y3 = sudoku.find_y(puzzle, 2)
#     y4 = sudoku.find_y(puzzle, 3)
#     y5 = sudoku.find_y(puzzle, 4)
#     y6 = sudoku.find_y(puzzle, 5)
#     y7 = sudoku.find_y(puzzle, 6)
#     y8 = sudoku.find_y(puzzle, 7)
#     y9 = sudoku.find_y(puzzle, 8)
#
#     ans = []
#     cal = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#     for i in range(1, len(puzzle) + 1):
#         ans.append(cal - x1 - y1)
#     return 1
import copy

def sudoku_solver( puzzle ):
    solution = copy.deepcopy( puzzle )
    if solveHelper( solution ):
        return solution
    return None

def solveHelper( solution ):
    minPossibleValueCountCell = None
    while True:
        minPossibleValueCountCell = None
        for rowIndex in range( 9 ):
            for columnIndex in range( 9 ):
                if solution[ rowIndex ][ columnIndex ] != 0:
                    continue
                possibleValues = findPossibleValues( rowIndex, columnIndex, solution )
                possibleValueCount = len( possibleValues )
                if possibleValueCount == 0:
                    return False
                if possibleValueCount == 1:
                    solution[ rowIndex ][ columnIndex ] = possibleValues.pop()
                if not minPossibleValueCountCell or \
                   possibleValueCount < len( minPossibleValueCountCell[ 1 ] ):
                    minPossibleValueCountCell = ( ( rowIndex, columnIndex ), possibleValues )
        if not minPossibleValueCountCell:
            return True
        elif 1 < len( minPossibleValueCountCell[ 1 ] ):
            break
    r, c = minPossibleValueCountCell[ 0 ]
    for v in minPossibleValueCountCell[ 1 ]:
        solutionCopy = copy.deepcopy( solution )
        solutionCopy[ r ][ c ] = v
        if solveHelper( solutionCopy ):
            for r in range( 9 ):
                for c in range( 9 ):
                    solution[ r ][ c ] = solutionCopy[ r ][ c ]
            return True
    return False

def findPossibleValues( rowIndex, columnIndex, puzzle ):
    values = { v for v in range( 1, 10 ) }
    values -= getRowValues( rowIndex, puzzle )
    values -= getColumnValues( columnIndex, puzzle )
    values -= getBlockValues( rowIndex, columnIndex, puzzle )
    return values

def getRowValues( rowIndex, puzzle ):
    return set( puzzle[ rowIndex ][ : ] )

def getColumnValues( columnIndex, puzzle ):
    return { puzzle[ r ][ columnIndex ] for r in range( 9 ) }

def getBlockValues( rowIndex, columnIndex, puzzle ):
    blockRowStart = 3 * ( rowIndex // 3 )
    blockColumnStart = 3 * ( columnIndex // 3 )
    return {
        puzzle[ blockRowStart + r ][ blockColumnStart + c ]
            for r in range( 3 )
            for c in range( 3 )
    }

def printPuzzle( puzzle ):
    for row in puzzle:
        print(row)


puzzle = [
    [0, 0, 6, 1, 0, 0, 0, 0, 8],
    [0, 8, 0, 0, 9, 0, 0, 3, 0],
    [2, 0, 0, 0, 0, 5, 4, 0, 0],
    [4, 0, 0, 0, 0, 1, 8, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 4, 0],
    [0, 0, 7, 9, 0, 0, 0, 0, 3],
    [0, 0, 8, 4, 0, 0, 0, 0, 6],
    [0, 2, 0, 0, 5, 0, 0, 8, 0],
    [1, 0, 0, 0, 0, 2, 5, 0, 0]
]

printPuzzle( puzzle )
print()

solution = sudoku_solver( puzzle )
if solution: printPuzzle( solution )
