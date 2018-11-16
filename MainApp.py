import argparse
import sys
import time

from BoardIterator.BoardIterator import BoardIterator
from BoardUtils.BoardUtils import BoardUtils


def main(argv):
    parse_args(argv)
    exit(0)


def parse_args(argv):

    # I declare an Args class to store the arguments parsed by the argparse library
    class Args:
        def __init__(self):
            self.board_size = 0
            self.t = False
            self.ta = False
            self.tf = False

    parser = argparse.ArgumentParser(description='N-Queens Brute Force')
    parser.add_argument('board_size', type=int,
                        help='The size of one side of the board, the board would be NxN')
    parser.add_argument('-t', action='store_true', help='Prints the time it takes to find and print all solutions')
    parser.add_argument('-ta', action='store_true', help='Prints the time it takes to find all solutions')
    parser.add_argument('-tf', action='store_true', help='Prints the time it takes to find the first solution')

    args_obj = Args()

    # The args_obj will store the values of the different flags
    parser.parse_args(argv, namespace=args_obj)
    board_iterator = BoardIterator(args_obj.board_size)
    board_utils = BoardUtils(args_obj.board_size)

    # No option arguments passed -> Just print the solutions
    if not args_obj.t and not args_obj.ta and not args_obj.tf:
        board_utils.print_all_solutions(board_iterator)
        exit(0)

    output_file = open("bf_python_results.txt", "w")

    # I check the state of every single flag and act accordingly
    if args_obj.t:
        output_str = get_all_results_printing_time_str(board_utils, board_iterator)
        handle_output(output_file, output_str)

    if args_obj.ta:
        output_str = get_all_results_time_str(board_utils, board_iterator)
        handle_output(output_file, output_str)

    if args_obj.tf:
        output_str = get_first_result_time_str(board_utils, board_iterator)
        handle_output(output_file, output_str)

    output_file.close()


def get_first_result_time_str(board_utils, board_iterator):
    start_time = time.time()
    board_utils.find_first_solution(board_iterator)
    elapsed_time = time.time() - start_time
    return "Finding FIRST solution: " + str(elapsed_time) + " s" + "\n"


def get_all_results_time_str(board_utils, board_iterator):
    start_time = time.time()
    board_utils.find_all_solutions(board_iterator)
    elapsed_time = time.time() - start_time
    return "Finding ALL solutions: " + str(elapsed_time) + " s" + "\n"


def get_all_results_printing_time_str(board_utils, board_iterator):
    start_time = time.time()
    board_utils.print_all_solutions(board_iterator)
    elapsed_time = time.time() - start_time
    return "Printing ALL solutions: " + str(elapsed_time) + " s" + "\n"


def handle_output(output_file, output_str):
    print(output_str)
    output_file.write(output_str)


if __name__ == "__main__":
    main(sys.argv[1:])
