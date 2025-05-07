def regredir(a):
    if a == 0:
        return 0

    print(a)

    return regredir(a - 1)

print(regredir(13))