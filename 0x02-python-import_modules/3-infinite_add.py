#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_num = 0

    for arg in sys.argv[1:]:
        arg_num += int(arg)

    print("{}".format(arg_num))
