import random

def gamewin(comp,you):
    if comp==you:
        return None
    
    elif comp=="s":
       if you=="w":
        return False        
       elif you=="g":
        return True
    
    elif comp=="w":
       if you=="g":
        return False        
       elif you=="s":
        return True
    
    elif comp=="g":
       if you=="s":
        return False        
       elif you=="w":
        return True
    


print(" computer chooice..snake(s),water(w),gun(g)")
choose=random.randint(1,3)
if choose==1:
    comp="s"
elif choose==2:
    comp="w"

elif choose==3:
    comp="g"
        
you=input("enter you chooice..snake(s),water(w),gun(g)").strip().lower()        
a= gamewin(comp,you) 

print(f"computer choose,{comp}")
print(f"you choose,{you}")

if a==None:
    print( 'game is tie ')
elif a:
    print("you win ")
else:
    print ("you loose ")    