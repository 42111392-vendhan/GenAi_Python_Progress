def pattern(n):
    for x in range(1,n+1):
        for y in range(x):
            print(x, end="")
        print()
pattern(8)
