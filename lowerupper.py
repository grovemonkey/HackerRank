#!/usr/bin/env python3

def swap_case(s):
    x = []
    for item in s:
        if item.islower() == True:
            y = item.upper()
            x.append(y)
        elif item.isupper() == True:
            y = item.lower()
            x.append(y)
        else:
            x.append(item)
    return x


if __name__ == '__main__':
    s = "hACKERrANK.COM PRESENTS pYTHONIST 2"
    result = swap_case(s)
    print(*result)
