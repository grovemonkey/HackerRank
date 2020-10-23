import re


def lowcase(strings2):
    match1 = re.findall(regex1, strings2)
    dit1.append(match1)


def uppercase(strings2):
    match2 = re.findall(regex2, strings2)
    dit1.append(match2)


def oddnum(strings2):
    match3 = re.findall(regex3, strings2)
    dit1.append(match3)


def evennum(strings2):
    match4 = re.findall(regex4, strings2)
    dit1.append(match4)


if __name__ == '__main__':
    strings = input()
    strings2 = "".join(sorted(strings))
    dit1 = []
    regex1 = r"[a-z]+"
    regex2 = r"[A-Z]+"
    regex3 = r"[1,3,5,7,9]+"
    regex4 = r"[0,2,4,6,8]+"
    lowcase(strings2)
    uppercase(strings2)
    oddnum(strings2)
    evennum(strings2)
    x = [val for sublist in dit1 for val in sublist]
    print("".join(x))
