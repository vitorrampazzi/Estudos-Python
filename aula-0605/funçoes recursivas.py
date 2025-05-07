def farorial(n):
    if n < 2:
        return 1



    return n * farorial(n - 1)

print(farorial(7))