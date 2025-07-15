


def hundred(num):
    if num==100:
        return 100
    print(num)
    return hundred(num+1)

print(hundred(1))