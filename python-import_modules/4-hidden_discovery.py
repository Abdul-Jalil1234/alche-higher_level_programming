#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    # Get all names defined in the hidden_4 module
    # dir() returns a sorted list of strings
    names = dir(hidden_4)

    for name in names:
        # Filter out names starting with '__'
        if not name.startswith("__"):
            print("{}".format(name))
