#strip removes the whitespaces from left and right, title capitalize the first letter of each word
print("hello! ".title()+"      my name is tuhin".strip().title())

#by default the end value is \n. you can overwrite it
print("You are ", end="")
print("suck!")

#By default the sep value is " ", It applies middile of the print values.
print("You", "Also",sep="-")

#split convert to a list
a = "Akikul Islam"
fst= a.split()
print(fst[0])
print(a)

a,b = ["hello","Tuhin"]
print(b)

#round calculate to the nearest value of a float
fl1 = 2.3
fl2 = 2.3
print(round(fl1+fl2))

print(round(3.378, 2))
#or
print(f"{3.378: .2f}")

n = 1294748
print(f"{n: ,}")

def hello():
    print("Hello,")
name = input()
hello()
print(name)

def hello2(to):
    print("Hello,",to)

hello2(name)

def hello3(to="world"):
    print(to)
hello3()

def hello4():
    hello2(name)
hello4()

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
    
main()

def a(n):
    return n+1
print(a(1))


