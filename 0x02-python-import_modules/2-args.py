#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    # if argc is lesser than 2, print "0 arguments."
    if argc < 2:
        print("0 arguments.")
    # elif argc is 2, print 1 argument: 1: argv[1]
    elif argc == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    # else
    else:
        # print argc -1 arguments
        print("{} arguments:".format(argc - 1))
        # Create a for loop with argc:
        for i in range(1, argc):
            # print i, and argument
            print("{}: {}".format(i, argv[i]))
