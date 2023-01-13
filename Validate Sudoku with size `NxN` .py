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
        return len(block_set) == 9
