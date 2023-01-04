import math


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.block_len = int(math.sqrt(self.n))

    def is_valid(self):
        h = len(self.data)
        dt = math.sqrt(h)
        if h % dt != 0:
            return False
        for i, row in enumerate(self.data):
            if len(row) != h:
                return False
            if all(list(map(lambda x: type(x) == int and 0 < x <= h, row))):
                pass
            else:
                return False
            if int(dt) <= 3:
                if not len(set(row)) == len(row):
                    return False
            if not self._is_valid_block(i):
                return False
        return True

    def _is_valid_block(self, block_num):
        block_row_num, block_column_num = divmod(block_num, self.block_len)
        block_row, block_column = block_row_num * self.block_len, block_column_num * self.block_len
        block_set = set()
        for r in range(block_row, block_row + self.block_len):
            for c in range(block_column, block_column + self.block_len):
                block_set.add(self.data[r][c])
        return self._is_valid_set(block_set)

    def _is_valid_set(self, num_set):
        return len(num_set) == self.n \
               and max(num_set) == self.n \
               and min(num_set) == 1 \
               and all(type(i) is int for i in num_set)


# Valid Sudoku
goodSudoku1 = Sudoku([
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]
])
print(goodSudoku1.is_valid())