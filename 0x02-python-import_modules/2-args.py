#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    numArgs = len(sys.argv) - 1

    if numArgs == 0:
        print("0 arguments.")

    elif numArgs == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(numArgs))

    for n in range(numArgs):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
