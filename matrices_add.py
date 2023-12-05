def sum_matrices(M1,M2):
  M3 = [[0,0,0],[0,0,0],[0,0,0]]
  for i in range(0,len(M1)):
    for j in range(0,len(M2)):
      M3[i][j] = M1[i][j] + M2[i][j]
  print(M3)

M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[4,5,2],[5,7,1],[7,9,2]]
sum_matrices(M1,M2)
