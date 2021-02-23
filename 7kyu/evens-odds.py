def evens_and_odds(n):
    if n%2 == 0:
        return bin(n)[2:]
    return hex(n)[2:]

assert evens_and_odds(2) == '10' , "Should be 10"
assert evens_and_odds(13) == 'd' , "Should be d"
assert evens_and_odds(15) == 'f' , "Should be f"
assert evens_and_odds(4) == '100' , "Should be 100"