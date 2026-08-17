# Einfach Funktion ohne Parameter definieren
def function_name(Parameters):
    # code block
    return value # Optional


# Example : Simple Function

def greet():
    print("Hello , Data Science Enthusiast!")

greet()


# Functions with Parameters

def greet(name):
    print(f"Hello, {name}!")

greet("Alice") 
greet("Bob")   


# Funcion wiht Multiple Parameters

def add_numbers(a , b):
    result = a + b
    print(f"The sum of  {a} and {b} is {result}.")

add_numbers(3, 5)


# Default Arguments

def greet(name="Data Scientist"):
    print(f"Welcome , {name}!")


greet()
greet("Alice")    


# Aufgabe : FUnktion mit Zwei Parametern, einer davon mit Standartwert

def introduce(name, city="Bremen"):
    print(f"Ich bin {name} und wohne in {city}.")

introduce("Musti")
introduce("Musti", "Helsinki")
introduce("Musti", city="Berlin") 

#Example : Returning a value


def square(number):
    return number * number

result = square(4)
print(f"The square of 4 is {result}") 


#CAlling FUnctions


def say_hello():
    print("Hello!")

# Function call
say_hello()    