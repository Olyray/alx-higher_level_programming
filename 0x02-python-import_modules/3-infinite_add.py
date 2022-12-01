#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum_total = 0
    argc = len(argv)
    # if argc < 2, print 0
    if argc < 2:
        print("0")
    # else:
    else:
        # for loop with argc:
        for i in range(1, argc):
            # sum += int(argv[i])
            sum_total += int(argv[i])
        # print sum
        print(sum_total)
