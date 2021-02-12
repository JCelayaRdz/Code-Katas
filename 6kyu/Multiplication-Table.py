def multiplication_table(size):
    mult_table = []
    for row in range(1,size+1):
        row_table = []
        for column in range(1,size+1):
            row_table.append(row*column)
        mult_table.append(row_table)
    return mult_table

assert multiplication_table(3) == [[1,2,3],[2,4,6],[3,6,9]] , "Should be [[1,2,3],[2,4,6],[3,6,9]]"
assert multiplication_table(2) == [[1, 2], [2, 4]] , "Should be [[1, 2], [2, 4]]"
