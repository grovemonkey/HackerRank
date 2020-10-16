if __name__ == '__main__':
    mylist = []
    for _ in range(0, int(input())):
        mylist.append([input(), float(input())])
    num_two = sorted(list(set([list for name, list in mylist])))[1]
    print('\n'.join([a for a, b in sorted(mylist) if b == num_two]))

