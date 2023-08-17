'''Week:1
Task: 1 on variables

1)Create a variable called break and assign it a value 5.
See what happens and find out the reason behind the behavior that you see.'''
#break=5

#It got an Invalid Syntax because break is a key word in Python so key words can't assign as a variable.

'''
2)Create two variables. One to store your birth year and another one to store current year.
Now calculate your age using these two variables
'''
birth_year=int(input("enter Birth year:"))
current_year=int(input("Enter current year:"))
age=current_year-birth_year
print(age)

'''
3)Store your first, middle and last name in
three different variables and then print your full name using these variables
'''
first="Gundlapalli"
middle="Nashrath"
last="Tulla"
print(first+middle+last)

'''
4)Answer which of these are invalid variable
names: _nation 1record record1 record_one record-one record^one continue
'''
_nation=10
print(_nation)

#1record and record-one and record^one cannot use as variable names.

