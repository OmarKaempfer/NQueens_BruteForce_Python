import argparse
import sys
import time

from BoardIterator.BoardIterator import BoardIterator
from BoardUtils.BoardUtils import BoardUtils


def main(argv):
    class Args:
        def __init__(self):
            self.board_size = 0
            self.t = False
            self.ta = False
            self.tf = False

        pass

    parser = argparse.ArgumentParser(description='N-Queens Brute Force')
    parser.add_argument('board_size', type=int,
                        help='The size of one side of the board, the board would be NxN')
    parser.add_argument('-t', action='store_true', help='Prints the time it takes to find and print all solutions')
    parser.add_argument('-ta', action='store_true', help='Prints the time it takes to find all solutions')
    parser.add_argument('-tf', action='store_true', help='Prints the time it takes to find the first solution')
    args_obj = Args()
    parser.parse_args(argv, namespace=args_obj)

    board_iterator = BoardIterator(args_obj.board_size)
    board_utils = BoardUtils(args_obj.board_size)
    if not args_obj.t and not args_obj.ta and not args_obj.tf:
        board_utils.print_all_solutions(board_iterator)
        exit(0)

    output_file = open("bf_python_results.txt", "w")

    if args_obj.t:
        start_time = time.time()
        board_utils.print_all_solutions(board_iterator)
        elapsed_time = time.time() - start_time
        output_str = "Printing ALL solutions: " + str(elapsed_time) + " s" + "\n"
        print(output_str)
        output_file.write(output_str)

    if args_obj.ta:
        start_time = time.time()
        board_utils.find_all_solutions(board_iterator)
        elapsed_time = time.time() - start_time
        output_str = "Finding ALL solutions: " + str(elapsed_time) + " s" + "\n"
        print(output_str)
        output_file.write(output_str)

    if args_obj.tf:
        start_time = time.time()
        board_utils.find_first_solution(board_iterator)
        elapsed_time = time.time() - start_time
        output_str = "Finding FIRST solution: " + str(elapsed_time) + " s" + "\n"
        print(output_str)
        output_file.write(output_str)

    output_file.close()
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
