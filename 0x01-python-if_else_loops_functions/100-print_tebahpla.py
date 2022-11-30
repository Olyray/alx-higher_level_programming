#!/usr/bin/python3
for i in range(26):
    if i % 2 != 0:
        print('{:s}'.format(chr(122 - i).upper()), end='')
    else:
        print('{:c}'.format(122 - i), end='')
