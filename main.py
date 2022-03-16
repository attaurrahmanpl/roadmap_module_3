# ////////////////////////////////////////////// Conditional Statement Lecture_1 //////////////////////////////////////


#temperature  = int(input("Enter value of temperature : ")) # this line is for geric value of temrature

# let get static value for temerature
print("Conditional Statement Lecture_1\n")
temperature = 40

if temperature > 20 :
    print("temperature is greater than 20")
elif temperature == 20 :
    print("temperature is equal 20")
else:
    print("temperature i less thatn 20")

print("done\n")

# ////////////////////////////////////////////// Ternary operator Lecture_2 //////////////////////////////////////
# we can write the above code in single line that is called ternary operator
#student_age = int(input("enter age of the student : "))
print("\n")
print("Ternary operator Lecture_2\n")
student_age = 17
message = "eligible" if student_age > 18 else "not eligible"
print(message)


# ////////////////////////////////////////////// Logical operator Lecture_3 //////////////////////////////////////
print("\n")
print("Logical operator Lecture_3\n")
high_income = True
good_credit = False

# logical "and" operator
# in and operator if one condition is fulfill the result will be false
if high_income and good_credit:
    print("\nemployee is eligible")
else:
    print("\nnot eligible")

# logical "or" operator
# in or operator if one condition is fulfill the result will be true
if high_income or good_credit:
    print("\nemployee is eligible")
else:
    print("\nnot eligible")

# logical "Not" operator
# in or operator if one condition is fulfill the result will be true

student = False
if not student:
    print("\neligible for employee")
else:
    print("\nStudents are not allowed for employee")

# now apply all the conditions
if (high_income or good_credit) and not student:
    print("\ncongratulations you are eligible for employee")
else:
    print("\nStudents are not allowed for employee")
# in the above lecture we have play only with bol operators


# ////////////////////////////////////////////// Short circuits evaluation Lecture_5 //////////////////////////////////////
print("\n")
print("Short circuits evaluation Lecture_5 \n")
high_income = False
good_credit = True
student = False
if high_income and good_credit and not student:
    print("\nyou are eligible for employee")
else:
    print("\nnot eligible ")


# ////////////////////////////////////////////// changing comparison operator Lecture_6 //////////////////////////////////////

# age should be between 18 to 65 for employee
# age = input("enter your age")
print("\n")
print("changing comparison operator Lecture_6 \n")
age = 122
if age >= 18 and age < 65:
    print("\nmyou are eligible for employee")
elif age < 18 :
    print("\nyou are under age ")
else:
    print("\nyou are overage ")

# second approach for the above problem

if 18 <= age < 65:
    print("\ncongratulations you are eligible")
else:
    print("\nsorry your not eligible")


# ////////////////////////////////////////////// Quiz Lecture_7 //////////////////////////////////////

# ////////////////////////////////////////////// For loops Lecture_8 //////////////////////////////////////

# use loop to create repetition
print("\n\nLoop")
print("For loops Lecture_8 \n")
for number in range(3):
    print("hello world")

# we can print number also with the message
print("\n\nLoop")
for number in range(3):
    print("hello world" , number)

# we can print number also with the message from indexing 1
print("\n\nLoop")
for number in range(3):
    print("hello world" , number + 1 , (number + 1) * "*") # this will print stars as wel index


# the above work we can do with multiple approach
print("\n\nLoop")
for number in range(1 , 10 , 2): # tis will print every second numer start from 1
    print("hello world" , number , number * "*") # this will print stars as wel index


# ////////////////////////////////////////////// For Else Lecture_9 //////////////////////////////////////
print("\n\nLoop")
print("For Else Lecture_9 \n")
successful = True
for number in range(3):
    print("hello world")
    if successful: # if this condition is fulfil the break statement will stop the program
        print("successful")
        break


# second approach
print("\n\nLoop")
# attempts = int(input("\nHow many times you want to attempt ? :"))
attempts = 7
successful = False
for number in range(attempts):
    print("hello world")
    if successful: # if this condition is fulfil the break statement will stop the program
        print("successful")
        break
else: # this is for else
    print("you have try" , attempts , "times")


# ////////////////////////////////////////////// Nested loop Lecture_10 //////////////////////////////////////
print("\n")
print("Nested loop Lecture_10\n")
# loop in loop

for x in range(5):
    for y in range(3):
        print(f"({x} , {y} )")


# ////////////////////////////////////////////// iterables Lecture_11 //////////////////////////////////////

print("\n")
print("niterables Lecture_11\n")
# Iterables
print(type(5)) # print the type of the variable
print(type(range(5))) # change the type of the variable from int to range
for x in range(5):
    print(x) # this will print the iteration of integer


# Iteration of  string
print("\n")
for x in "python":
    print(x) # this will print the iteration of integer

# Iteration of  List
print("\n")
for x in [1 , 2 , 3 , 4 , 60 , 20 , 3]:
    # this will print the iteration of integer
    print(x)
# second method for list iteration
print("\n")
list_of_numer  = [1 , 2 , 3 , 4 , 5 , 6 , 7]

for x in list_of_numer:
    # this will print the iteration of integer
    print(x)


# ////////////////////////////////////////////// while loop Lecture_11 //////////////////////////////////////

# while loop
print("\n\n")
print("while loop Lecture_11\n")
number = 100
while number > 0:
    print("the original number is : ", number)
    print(number , "/ 2 is :" )
    number = number//2
    print(number)


# while loop
# second method of the above task
print("\n\n")
number = 100
while number > 0:
    print("the original number is : ", number)
    print(number , "/ 2 is :" )
    number //= 2
    print(number)

# create simple terminal window like cmd or ubuntu terminal

command = ""
while command != "q" and command != "Q": # this loop will running untill user input q
    command = input(">>")
    print("echo" , command)


# create simple terminal window like cmd or ubuntu terminal
command = ""
while command.lower() != "q": # this loop will running until user input q
    command = input(">>")
    print("echo" , command)

