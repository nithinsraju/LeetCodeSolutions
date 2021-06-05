def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j':9 }
    firstNum = ""
    secondNum = ""
    targetNum = ""
    for i in firstWord:
        if i in dict:
            firstNum += str(dict[i])
    print(firstNum)
    for i in secondWord:
        if i in dict:
            secondNum += str(dict[i])
    print(secondNum)
    for i in targetWord:
        if i in dict:
            targetNum+= str(dict[i])
    print(targetNum)

    x = int(firstNum)
    y = int(secondNum)
    z = int(targetNum)

    sum = x + y
    print(sum)
    if sum == z:
        return True
    else:
        return False

if __name__ == '__main__':
    firstWord = str(input())
    secondWord = str(input())
    targetWord = str(input())

isSumEqual(firstWord, secondWord, targetWord)