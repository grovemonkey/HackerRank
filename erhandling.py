for t in range(int(input())):
    try:
        a,b = map(int, input().split()) # here is the key to taking in the inputs
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)