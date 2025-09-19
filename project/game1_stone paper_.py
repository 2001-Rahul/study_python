import random

def stoney(comp,you):
    if comp==you:
       return None
    elif comp=="st":
       if you=="s":
        return False
       elif you=="p":
        return True
    
    elif comp=='s':
       if you=="p":
        return False
       elif you=="st":
        return True 
    
    elif comp=='p':
       if you=="st":
        return False
       elif you=="s":
        return True      


print(" computer chooice.. ")
rom=random.randint(1,3)
if rom==1:
   comp="p"
elif rom==2:
   comp="s"
elif rom==3:
   comp="st" 

you=input('enter your choice ' ).strip().lower()    

a=stoney(comp,you)

if a==None:
    print( 'game is tie ')
elif a:
    print("you win ")
else:
    print ("you loose ")    

print("you choose",you)
print("comp choose",comp)