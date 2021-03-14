def fake_bin(number):
    res = ''
    for i in number:
        if int(i) < 5:
            res += '0'
        else:
            res += '1'
    return res

assert fake_bin("45385593107843568") == "01011110001100111"
assert fake_bin("509321967506747") == "101000111101101"
assert fake_bin("366058562030849490134388085") == "011011110000101010000011011"