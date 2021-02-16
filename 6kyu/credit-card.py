def validate(number):
    digits = [int(i) for i in str(number)]
    digits = [i for i in reversed(digits)]
    for index,digit in enumerate(digits,1):
        print(index,digits)
        if index % 2 == 0:
            powed = digit * 2
            if powed < 9:
                digits[index - 1] = powed
            else:
                digits[index - 1] = sum([int(i) for i in str(powed)])
    return sum(digits) % 10 == 0


assert validate(123) == False , "Should be False"
assert validate(1) == False , "Should be False"
assert validate(2121) == True , "Should be True"
assert validate(1230) == True , "Should be True"