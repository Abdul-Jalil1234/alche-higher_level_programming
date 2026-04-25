#!/usr/bin/python3
import sys


if __name__ == "__main__":
    # Get the list of arguments excluding the script name
    args = sys.argv[1:]
    count = len(args)

    # Determine the correct word for "argument" based on count
    arg_word = "argument" if count == 1 else "arguments"
    
    # Determine the punctuation after the summary line
    punctuation = "." if count == 0 else ":"

    print("{} {}{}".format(count, arg_word, punctuation))

    # Print each argument with its 1-based index
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
