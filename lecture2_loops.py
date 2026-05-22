a = 0
while a <= 2 :
    print("Meow")
    a += 1

#for loop counts, how many indexes in the list
b = ["a","a"]
for i in b:
    print("bog")
    
#You can use range function instead
#_ use for when varriable doesn't needed
for _ in range(3):
    print("roar")
    
print("Meow"*3)
print("meow \n"*3, end=" ")
print("tuhin")

def main():
    meow(getnumber())
    
def getnumber():
    while True:
        n = int(input("Whats n?"))
        if n > 0:
            return n
            
def meow(n):
    for _ in range(n):
        print("Meow!")
    
main()

students = ["tuhin", "tomal", "tusher" ]
for i in students:
    print(i)
for student in range(len(students)):
    print(student + 1, students[student])

print("dictionaries")
student_houses = {
    "Tuhin" : "Netrokona",
    "Tomal" : "Dinajpur",
    "Tusher": "Rajshahi"}
print(student_houses["Tuhin"])

for houses in student_houses:
    print(houses)
    
print()

for house in student_houses:
    print(house, student_houses[house], sep=" in ")



#multiple dictionaries 
workers = [{"Harun": "Chairman", },
           {"Rashid": "Teacher"},
           {"Kamal": "Firefighter"}]

for worker in workers:
    #using if to avoid key error because second and third dic dont have Harun
    #if the dictionaries' keys are same then worker[harun] it will print all the keys' values
    if "Harun" in worker:
        print(worker["Harun"])

worker_names = [{"name": "Tuhin", "Class": "class 9"},
                {"name": "Tomal", "Class": None},
                {"name": "Tusher", "Class": "University"}]
for classes in worker_names:
    print(classes["name"], classes["Class"], sep=", ")
    

# Mario bricks
for _ in range(3):
    print("#" * 3)
print("understanding break")
for _ in range(3):
    for _ in range(3):
        print("#", end="")
    print()

print("understanding break")
def main():
    print_square(3)

def print_square(n):
    for _ in range(n):
        print_row(n)
def print_row(width):
    for _ in range(width):
        print("#", end="")
    print()
    # or just print("#" * width)
main()
