def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number,end_number+1,step))

assert sequence_sum(2,6,2) == 12 , "Should be 12"
assert sequence_sum(1,5,1) == 15 , "Should be 15"
assert sequence_sum(1,5,3) == 5 , "Should be 5"
assert sequence_sum(0,15,3) == 45 , "Should be 45"
assert sequence_sum(16,15,3) == 0 , "Should be 0"
assert sequence_sum(2,24,22) == 26 , "Should be 26"