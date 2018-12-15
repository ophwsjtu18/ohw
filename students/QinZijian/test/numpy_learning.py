import numpy as np


'''
M = np.zeros((3, 2, 4)) #row 行 
print(M)
[[[0. 0. 0. 1.]      (0,0)
  [0. 0. 0. 0.]]     (0,1)

 [[0. 0. 0. 0.]      (1,0)
  [0. 0. 0. 0.]]     (1,1)

 [[0. 0. 0. 0.]      (2,0)
  [0. 0. 0. 0.]]]    (2,1)
'''

num_rows = int(input("Rows: "))
num_cols = int(input("Columns: "))
M = np.zeros((num_rows, num_cols, 5), dtype=np.uint8)
#row行 col列 每个单元5个元素

r = 0
c = 0
M[r, c, 4] = 1
print(M)
