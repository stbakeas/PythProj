import random
matrix_dimension=10

#Δημιουργία του πίνακα
basic_matrix=[[random.choice(("S","O")) for x in range(matrix_dimension)] for i in range(matrix_dimension)] 

#Καλύτερη οπτική αναπαράσταση του πίνακα
for i in basic_matrix: 
    print(i)

#Οι λίστες αυτές μας βοηθούν να εντοπίσουμε εάν υπάρχει κρυμμένο ένα SOS μέσα σε ένα άλλο.
#π.χ. [S,O,S,O,S]. Εδώ υπάρχουν 2 SOS. Η new_list της προηγούμενης λίστας θα είναι:[SOS,OSO,SOS]
new_list_horizontal=[] 
new_list_vertical=[]
new_list_diagonal=[]
new_list_reverse_diagonal=[]

#Μέτρηση SOS οριζόντια και κάθετα
horizontal_counter,vertical_counter,diagonal_counter,reverse_diagonal_counter=0,0,0,0 
for i in range(matrix_dimension):
  for j in range(matrix_dimension-2):
    new_list_horizontal.append(basic_matrix[i][j]+basic_matrix[i][j+1]+basic_matrix[i][j+2])
    new_list_vertical.append(basic_matrix[j][i]+basic_matrix[j+1][i]+basic_matrix[j+2][i])

  horizontal_counter+=new_list_horizontal.count("SOS")
  vertical_counter+=new_list_vertical.count("SOS")
  new_list_horizontal.clear()
  new_list_vertical.clear()

#Μέτρηση SOS κύριας διαγωνίου
for i in range(matrix_dimension-2):
    for j in range(matrix_dimension-2):
     new_list_diagonal.append(basic_matrix[i][j]+basic_matrix[i+1][j+1]+basic_matrix[i+2][j+2])
    diagonal_counter+=new_list_diagonal.count("SOS")
    new_list_diagonal.clear()

#Μέτρηση SOS δευτερεύουσας διαγωνίου
for i in range(matrix_dimension-2):
  for j in range(matrix_dimension-1,1,-1):
    new_list_reverse_diagonal.append(basic_matrix[i][j]+basic_matrix[i+1][j-1]+basic_matrix[i+2][j-2])
  reverse_diagonal_counter+=new_list_reverse_diagonal.count("SOS")
  new_list_reverse_diagonal.clear()


diagonal_counter+=reverse_diagonal_counter   


  
print("Horizontal SOS",horizontal_counter)
print("Vertical SOS",vertical_counter)
print("Diagonal SOS",diagonal_counter)

    



    


        


            


