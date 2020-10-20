# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re


def fun(s):
    regex = r"^[a-zA-Z0-9_-]+[@][a-zA-Z0-9]+[.]\w{2,3}$"
    match = re.match(regex, s, re.MULTILINE)
    if match != None:
        return s
    else:
        return


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
