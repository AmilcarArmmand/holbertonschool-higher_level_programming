#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) is 1:
        print("0 arguments.")
    elif len(argv) is 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
