import random
matrix_dimension=10

#Matrix Creation
basic_matrix=[[random.choice(("S","O")) for x in range(matrix_dimension)] for i in range(matrix_dimension)] 

#Visual Representation of Matrix
for i in basic_matrix: 
    print(i)

new_list_horizontal=[]
new_list_vertical=[]
new_list_diagonal=[]
horizontal_counter,vertical_counter,diagonal_counter=0,0,0
for i in range(matrix_dimension):
  for j in range(matrix_dimension-2):
    new_list_horizontal.append(basic_matrix[i][j]+basic_matrix[i][j+1]+basic_matrix[i][j+2])
    new_list_vertical.append(basic_matrix[j][i]+basic_matrix[j+1][i]+basic_matrix[j+2][i])

  horizontal_counter+=new_list_horizontal.count("SOS")
  vertical_counter+=new_list_vertical.count("SOS")
  new_list_horizontal.clear()
  new_list_vertical.clear()

for i in range(matrix_dimension-2):
    for j in range(matrix_dimension-2):
     new_list_diagonal.append(basic_matrix[i][j]+basic_matrix[i+1][j+1]+basic_matrix[i+2][j+2])
    diagonal_counter+=new_list_diagonal.count("SOS")
    new_list_diagonal.clear()


  
print("Horizontal SOS",horizontal_counter)
print("Vertical SOS",vertical_counter)
print("Diagonal SOS",diagonal_counter)

    
