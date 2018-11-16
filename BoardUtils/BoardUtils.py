class BoardUtils:

    # Creates some arrays to keep track of the positions attacked
    # So we create columns, rows and diagonals arrays.
    def __init__(self, board_size):
        self.board_size = board_size
        self.columns = [0] * self.board_size
        self.rows = [0] * self.board_size
        self.descending_diagonals = [0] * (2 * self.board_size - 1)
        self.ascending_diagonals = [0] * (2 * self.board_size - 1)

    # Initializes to 0 the aux arrays
    def initialize_aux(self):
        self.columns = [0] * self.board_size
        self.rows = [0] * self.board_size
        self.descending_diagonals = [0] * (2 * self.board_size - 1)
        self.ascending_diagonals = [0] * (2 * self.board_size - 1)

    def print_board(self, board):
        # Prints chunks of the array and insert line breaks to print a two dimensional grid
        for i in range(0, self.board_size):
            print(*board[i * self.board_size:(i + 1) * self.board_size], sep=' ')

    def is_solution(self, board):
        # Checks if the current position has a queen
        for i in range(0, len(board)):
            if board[i] == 0:
                continue

            # We are using a one dimensional array to represent the board so
            # we need to calculate the row index and column index for each
            # one dimensional position
            row_index = int(i / self.board_size)
            column_index = int(i % self.board_size)
            # Checks if the current queen positions is attacked from any
            # direction
            if (self.rows[row_index] == 1 or self.columns[column_index] == 1
                    or self.descending_diagonals[column_index - row_index + self.board_size - 1] == 1
                    or self.ascending_diagonals[row_index + column_index] == 1):
                self.initialize_aux()
                return False

            # Marks the column, row and diagonals attacked by this new
            # queen with a 1
            self.columns[column_index] += 1
            self.rows[row_index] += 1
            self.descending_diagonals[column_index - row_index + self.board_size - 1] += 1
            self.ascending_diagonals[row_index + column_index] += 1

        return True

    def find_all_solutions(self, board_iterator):
        iterator = iter(board_iterator)
        solutions = []
        for i in iterator:
            if self.is_solution(i):
                solutions.append(i.copy())

        return solutions

    def print_all_solutions(self, board_iterator):
        solutions = self.find_all_solutions(board_iterator)
        for i in solutions:
            self.print_board(i)
            print()

    def find_first_solution(self, board_iterator):
        iterator = iter(board_iterator)
        for i in iterator:
            if self.is_solution(i):
                return i

        return None
