def solve(a,b):
    res = []
    for string in b:
        res.append(a.count(string))
    return res

assert solve(['abc', 'abc', 'xyz', 'cde', 'uvw'], ['abc', 'cde', 'uap']) == [2,1,0] , "Should be [2,1,0]"
assert solve(['abc', 'abc','abc'], ['abc', 'cde', 'uap']) == [3,0,0] , "Should be [3,0,0]"
assert solve(['abc', 'abc', 'cde', 'cde', 'uvw'], ['abc', 'cde', 'uap']) == [2,2,0] , "Should be [2,2,0]"