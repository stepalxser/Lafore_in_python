from pprint import pprint
rows = 1, 2, 3, 0, -2, -3
cols = 'a', 'b', 'abc'
data1 = [(col, row)
         for row in rows if row > 0
         for col in cols if len(col) == 1
         ]
pprint(data1)

matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]]

flattened = [elem for row in matrix for elem in row]
pprint(flattened)

w, h = 10, 5
matrix = [[0 for _ in range(w)] for _ in range(h)]
pprint(matrix)

flattened = [matrix[row_index][column_index]
             for column_index in range(m)
             for row_index in range(n)]
result_string = ''.join(flattened)
print(result_string.replace())