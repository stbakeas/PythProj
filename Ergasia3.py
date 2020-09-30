def swap(array_word,i,j):
    temp=array_word[i]
    array_word[i]=array_word[j]
    array_word[j]=temp

def combinations(lst,list_index=0):
   if (list_index==len(lst)-1):
       print("".join(lst))
   for i in range(list_index,len(lst)):
       swap(lst,list_index,i)
       combinations(lst,list_index+1)
       swap(lst,i,list_index)

#Start
word=list(input("Enter a word:"))
combinations(word)


