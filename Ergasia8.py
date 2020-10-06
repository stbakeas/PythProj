import random

boundarie=10 #Ανώτατο όριο ετσι ώστε το πιονι να γυρίσει κάποια στιγμή, οπωσδήποτε στο [0,0]
total_number=0 #Συνόλο αριθμών που δημιουργήθηκαν από όλους τους γύρους
for i in range(0,100):
 amount_of_numbers=0 #Σύνολο αριθμών που δημιουργήθηκαν για έναν γύρο
 pawns_x_y=[0,0] #Αρχικοποίηση συντεταγμένων του πιονιού 
 direction=random.randint(1,4)
 

 if (direction==1):
    if (pawns_x_y[0]<boundarie):
     pawns_x_y[0]+=1
 elif (direction==2):
    if (pawns_x_y[0]>-boundarie):
     pawns_x_y[0]-=1
 elif (direction==3):
     if (pawns_x_y[1]<boundarie):
      pawns_x_y[1]+=1
 else:
    if (pawns_x_y[1]>-boundarie):
     pawns_x_y[1]-=1

 while (pawns_x_y!=[0,0]):


   direction=random.randint(1,4)

   if (direction==1):
    if (pawns_x_y[0]<boundarie):
     pawns_x_y[0]+=1
     amount_of_numbers+=1
   elif (direction==2):
    if (pawns_x_y[0]>-boundarie):
     pawns_x_y[0]-=1
     amount_of_numbers+=1
   elif (direction==3):
     if (pawns_x_y[1]<boundarie):
      pawns_x_y[1]+=1
      amount_of_numbers+=1
   else:
    if (pawns_x_y[1]>-boundarie):
     pawns_x_y[1]-=1
     amount_of_numbers+=1

 total_number+=amount_of_numbers
 print(i+1,"Round Completed with:",amount_of_numbers,"numbers created")
  

print(total_number/100) #Mέσος όρος αριθμών που δημιουργήθηκαν για 100 γύρους
