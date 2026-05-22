# this project for conditionals, if and else
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
        
        
# this for others


def divide(a,b):
    print("a/b is", a/b)
def modulo(a,b):
    print("a%b is", a%b)

divide(2,4)
modulo(2,4)

divide(4,2)
modulo(4,2)

#modulo operator return the vagsesh

def odd_even(x):
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
a = int(input())
odd_even(a)

"""
instead:
def is_even(n):
    return n % 2 == 0
"""
# match is same as if elif
name = "tuhin"
if name == "tuhin" or name == "tomal":
    print(name)
match name:
    case "tuhin" | "tomal":
        print(name)
    case "tusher":
        print("name")
