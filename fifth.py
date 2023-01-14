def max_frequent_letter(sentence):
    result = {}
    for symbol in sentence.lower():
        if symbol == ' ':
            continue

        if symbol in result:
            result[symbol] += 1
        else:
            result[symbol] = 1
    return max(result, key=result.get)


print(max_frequent_letter(input('Type sentence: ')))