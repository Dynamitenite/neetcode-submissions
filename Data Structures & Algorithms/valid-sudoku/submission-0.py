class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for row in range(0, 9):
            for col in range(0, 9):
                value = board[row][col]

                if value == ".":
                    continue

                box = (row // 3, col // 3)

                if row not in rows:
                    rows[row] = set()

                if col not in cols:
                    cols[col] = set()

                if box not in boxes:
                    boxes[box] = set()

                if (
                    value in rows[row] 
                    or value in cols[col]
                    or value in boxes[box]
                ):
                    return False

                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)
    
        return True