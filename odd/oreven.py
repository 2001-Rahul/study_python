import random
class oddoreven():
    def __init__(self,your,you,comp1):
        self.your=your
        self.you=you
        self.comp1=comp1
    
       
       
        comp=""
       
        if self.you=="e":
         comp="o"
        else:
         comp="e"

        if self.comp1==self.your:
            result= None
        
        elif (self.comp1+self.your)% 2 == 0: 
                
            if self.you=="e":
             result=True
            else:
                    result=False
        else:
                
            if self.you=="o":
             result=True
            else:
             result=False 
     
        
        
        if result==None:
            print( 'game is tie ')
        elif result==True:
            print("you win ")
        else:
            print ("you loose ")    
            


        print(f"you choose {self.your}")        
        print(f"comp choose,{self.comp1}")   
       

you=input("enter your choice..odd(o),even(e)").strip().lower()
your=int(input("enter your chossen number between 1 to 10: "))
comp1=random.randint(1,10)
a=oddoreven(your,you,comp1)

