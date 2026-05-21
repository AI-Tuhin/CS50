def signup():
    user = input()
    pwd = input()
    
    print("Welcome to MathBook!")
        
    return user,pwd
    
def login(user,pwd):
        
        user1 = input()
        pwd1 = input()
        if user == user1 and pwd == pwd1:
            print("Login succesfull.")
        else:
            print("Wrong! Try again.")
            
user, pwd = "", ""    

while True:
        select = int(input(" 1. Sign Up \n 2. Login \n 3. Exit \n "))
        
        if select == 1:
            
             user,pwd = signup()
            
            
        elif select == 2:
            login(user,pwd)
            
        elif select == 3:
            break
        else:
            print("Type 1 or 2 or 3 to select.")

print("github commit changes check from vs code")
        
        
        
    
    

