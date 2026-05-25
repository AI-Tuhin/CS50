#try and except use to avoid errors. it test the user input before something goes wrong
# notice the code below it will occurs an error called name error. because int can't be convert to string and not defined as a variable right to left
try:
    user = int(input())
except:
    print("Input an integer")
    # using else here to avoid the name error and print the user input if there is no error 
else:
    print(f"x is {user}")

#print(user)     (name error)

def main():
    x = get_int()
    print(f"y is {x}")

def get_int():
    while True:
        try:
            x = int(input("Type Y: "))
        except:
            print("Type an integer")
        else:
            return x
main()


def print_():
    x = got_int()
    print(f"z is {x}")
def got_int():
    while True:
        try:
            x = int(input("Type Z: "))
            return x
        except ValueError:
            print("Value error ")
print_()


def abc():
    x = getting_int("Type the value of abs: ")
    print("abc is:",x)
def getting_int(a):
    while True:
        try:
            while True:
                #this "a" value is the function;s argument value
                return int(input(a))
        except ValueError:
            pass

abc()


