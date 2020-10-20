from collections import Counter
word_input = input()
if len(word_input) > 3 and len(word_input) <= 10 * 4:
    cnt1 = Counter(sorted(word_input)).most_common(3)
    for st1, item in cnt1:
        print("{} {}".format(st1, item))
