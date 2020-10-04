import random

matrix_dimension=4

#Eπιστρέφει την i-οστή στήλη σε μορφή list
def column(matrix,i):
    return [row[i] for row in matrix]

#Επιστρέφει την κύρια διαγώνιο επάνω στην οποία βρίσκεται το σημείο (i,j) σε μορφή list
def main_diagonal(matrix,i,j):
    diag=[]
    starting_point=j-i
    if (starting_point>=0):
        j=starting_point
        i=0
        for x in range(j,matrix_dimension-1):
            diag.append(matrix[i][x])
            i+=1
    else:
        i=abs(starting_point)
        j=0
        for x in range(i,matrix_dimension-1):
            diag.append(matrix[x][j])
            j+=1
    return diag

#Επιστρέφει την δευτερεύουσα διαγώνιο επάνω στην οποία βρίσκεται το σημείο (i,j) σε μορφή list
def secondary_diagonal(matrix,i,j):
    diag=[]
    starting_point=i+j
    if (starting_point<=matrix_dimension-1):
        j=starting_point
        i=0
        for x in range(j,-1,-1):
            diag.append(matrix[i][x])
            i+=1
    else:
        j=matrix_dimension-1
        i=starting_point-j
        for x in range(j,starting_point-matrix_dimension,-1):
            diag.append(matrix[i][x])
            i+=1
    return diag


        




    

#Eπιστρέφει true εάν η λίστα l1 είναι κομμάτι της λίστας l2
#sublist([1,1,1,1],[1,0,1,0,1,0,1,0])=false
#sublist([1,1,1],[0,0,0,1,1,1,0,0])=true
def sublist(l1,l2):
    s1="".join(str(i) for i in l1)
    s2="".join(str(i) for i in l2)
    return s1 in s2

#Ελέγχει εάν υπάρχει τετράδα
def Four_Consecutives_Found(mult_array):
 return sublist([1,1,1,1],mult_array[i]) or sublist([0,0,0,0],mult_array[i]) or sublist([1,1,1,1],column(mult_array,j)) or sublist([0,0,0,0],column(mult_array,j)) or sublist([0,0,0,0],main_diagonal(mult_array,i,j)) or sublist([1,1,1,1],main_diagonal(mult_array,i,j)) or sublist([0,0,0,0],secondary_diagonal(mult_array,i,j)) or sublist([1,1,1,1],secondary_diagonal(mult_array,i,j))


numbers_created=0
consecutives_not_found=True
while (consecutives_not_found):
 multi_array=[['-' for i in range(matrix_dimension)]for j in range(matrix_dimension)]
 for i in range(matrix_dimension):
    for j in range(matrix_dimension):
        multi_array[i][j]=random.randrange(0,2)
        numbers_created+=1
        if Four_Consecutives_Found(multi_array):
            consecutives_not_found=False
            break
    else:
        continue
    break

        



for i in multi_array:
    print(i)

print("Numbers created:",numbers_created)



 


