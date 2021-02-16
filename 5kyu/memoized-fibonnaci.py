cache = {0:0,1:1}
def fibonacci(number):
    if number in cache:
        return cache[number]
    else:
        cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
    return cache[number]

assert fibonacci(70) == 190392490709135 , "Should be 190392490709135"
assert fibonacci(60) == 1548008755920 , "Should be 1548008755920"
assert fibonacci(50) == 12586269025 , "Should be 12586269025"