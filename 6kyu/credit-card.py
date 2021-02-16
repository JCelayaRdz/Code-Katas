def validate(number):
    digits = [int(i) for i in reversed(str(number))]
    for index,digit in enumerate(digits,1):
        if index % 2 == 0:
            new_digit = digit * 2
            if new_digit < 9:
                digits[index - 1] = new_digit
            else:
                digits[index - 1] = sum([int(i) for i in str(new_digit)])
    return sum(digits) % 10 == 0


assert validate(123) == False , "Should be False"
assert validate(1) == False , "Should be False"
assert validate(2121) == True , "Should be True"
assert validate(1230) == True , "Should be True"