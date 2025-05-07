def multiplicacao(a, b):
    if a == 0 or b == 0:
        return 0
    if b == 1:
        return a

    return a + multiplicacao(a, b - 1)

print(multiplicacao(2, 5))

