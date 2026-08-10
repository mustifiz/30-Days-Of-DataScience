# Prüft, ob eine Zahl positiv, negativ oder null ist
age = 20 
if age >= 18:
    print("Er ist volljährig.")
else:
    print("Er ist minderjährig.")  



# Example: Nested if-else statements

age = 20
if age >= 18:
    print("You can vote.")
else:
    if age >=16:
        print("You are a teenager.")
    else:
        print("You are a child.")



# Example : If-Elif-Else Statements

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")



##Loops
 # Loops allow repetitive tasks to be performed efficiently. Python has two types of loops: for loops and while loops.
 #    

numbers = [1, 2, 3, 4, 5]
for num in numbers:
   # print(num)






# Example: While Loop

count = 0
while count < 5:
    print(count)
    count += 1


for num in range(1, 6):
    if num == 3:
        break  # Exit loop when num is 3
    print(num)