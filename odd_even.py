import random

def odo_even(comp1,your,comp,you):
    if comp1==your:
        return None
    
    if (comp1+your)% 2 == 0: 
        
        if you=="e":
            return True
        else:
            return False
    else:
        
        if you=="o":
           return True
        else:
           return False 

       
you=input("enter your choice..odd(o),even(e)").strip().lower()
comp=""
if you=="e":
   comp="o"
else:
    comp="e"

your=int(input("enter your chossen number between 1 to 10: "))
    
comp1=random.randint(1,10)   

a=odo_even(comp1,your,comp,you)

if a==None:
    print( 'game is tie ')
elif a:
    print("you win ")
else:
    print ("you loose ")    

print("you choose",your)
print("comp choose",comp1)

