class demo:
    def __init__(self,name, last_name): 
        self.name = name
        self.last_name = last_name
        
    def username(self): # funcation which display the name
        print("Hi",self.name,"Hope you are doing well, Thanks for reaching me, Have a nice day")
        print("Your full name is ",self.name,self.last_name)


input_name = input("Enter your name =") # take user name input from user 
input_last_name = input("Enter you last name =") # take user last name

obj = demo(input_name, input_last_name) # created class object 
obj.username() # classing class object 