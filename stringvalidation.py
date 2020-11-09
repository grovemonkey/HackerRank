if __name__ == '__main__':
    s = input()
    print(any(word.isalnum() for word in s))
    print(any(word.isalpha() for word in s))
    print(any(word.isdigit() for word in s))
    print(any(word.islower() for word in s))
    print(any(word.isupper() for word in s)) #pretty easy
