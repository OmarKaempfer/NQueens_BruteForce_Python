class BoardIterator:

    def __init__(self, board_size):
        self.board_size = board_size

    # First board is a board_size x board_size one
    # with board_size queens one next to each other
    # in the first row.
    # Queens are 1s, empty positions are 0s.
    # 'indexes' stores the position of each queen.
    def init_attributes(self):
        for i in range(0, self.board_size):
            self.board.append(1)
            self.indexes.append(i)

        for i in range(self.board_size, self.board_size**2):
            self.board.append(0)

    def __iter__(self):
        self.indexes = []
        self.board = []
        self.next_board = []
        self.init_attributes()
        self.next_board = self.board.copy()
        return self

    def __next__(self):
        # The equivalent of a has_next method
        if self.indexes[0] == len(self.board) - len(self.indexes):
            raise StopIteration

        # On the first 'next' call we just return the
        # initialized board
        if self.next_board is not None:
            tmp_board = self.next_board
            self.next_board = None
            return tmp_board

        j = 0
        for i in range(len(self.indexes) - 1, -1, -1):
            # Checks whether the current queen has reached its
            # last possible position or not. If it did, we now
            # check the next queen in line.
            if self.indexes[i] == len(self.board) - 1 - j:
                j += 1
                continue

            # Moves the queen to the next position, clearing the
            # previous one
            self.board[self.indexes[i]] = 0
            self.indexes[i] += 1
            self.board[self.indexes[i]] = 1

            # Moves each queen which was in its last position
            # to their new initial position
            for k in range(i + 1, len(self.indexes)):
                self.board[self.indexes[k]] = 0
                self.indexes[k] = self.indexes[k - 1] + 1
                self.board[self.indexes[k]] = 1
            break
        return self.board
