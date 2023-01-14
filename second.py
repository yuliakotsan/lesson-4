def together(*args):
    result = []
    for dictionary in args:
        result = result + dictionary

    return result

print(together([1,2],[2,3],[4,5]))
