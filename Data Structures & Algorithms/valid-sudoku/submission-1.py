class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for i in range(len(board)):
        #    contains = []
        #    for j in range(len(board[0])):
        #        if board[i][j] != ".":
        #            if board[i][j] in contains:
        #                return False
        #            else:
        #                contains.append(board[i][j])
#
        #for i in range(len(board)):
        #    contains = []
        #    for j in range(len(board[0])):
        #        if board[j][i] != ".":
        #            if board[j][i] in contains:
        #                return False
        #            else:
        #                contains.append(board[j][i])
#
        #for i in range(3):
        #    for j in range(3):
        #        contains = []
        #        for k in range(3):
        #            for l in range(3):
        #                if board[i*3+k][j*3+l] != ".":
        #                    if board[i*3+k][j*3+l] in contains:
        #                        return False
        #                    else:
        #                        contains.append(board[i*3+k][j*3+l])
        square_values: dict[int, set] = {}
        # Check for row values.
        for i in range(len(board)):
            row = set()
            column = set()
            for j in range(len(board)):
                # Row
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])

                # Column
                if board[j][i] != ".":
                    if board[j][i] in column:
                        return False
                    else:
                        column.add(board[j][i])

                # Square
                idx = (i // 3) * 3 + (j // 3)
                if idx not in square_values:
                    square_values[idx] = set()
                
                if board[i][j] != ".":
                    if board[i][j] in square_values[idx]:
                        return False
                    else:
                        square_values[idx].add(board[i][j])
        return True