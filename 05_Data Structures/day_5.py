# Datenstrukturen
#schritt 1: listen ersellten und zugreifen

numbers = [1, 2, 3, 4, 5]

# Liste mit gemischten datentypen- in Python eraubt!
mixed_list = [1, "apple", 3.14, True]

fruits = ["apple", "banana", "cherry"]

# Zugriff über den Index (zahlung gebinnt bei 0)
print(fruits[0])
print(fruits[1])
print(fruits[-1])

#print(fruits[3])


# Schritt -2 : Elmente hinzufügen und entfernen


fruit =  ["apple", "banana"]

#Element am Ende hinzufügen
fruit.append("cherry")
print(fruit)

# Element an Position 1 einfügen
fruits.insert(1, "orange")
print(fruits)

# Element nach Wert entfernen
fruits.remove("banana")
print(fruits)

# Element nach Index entfernen — pop() gibt den Wert zurück!
removed = fruits.pop(1)
print(removed)
print(fruits)

#3.Dictionaries

# Dictionary mit schlüssel wert paaren erstellen 

person = {
    "name" : "Alice",
    "age" : 25 ,
    "city" : "New York"
}

#Zugriff über den Schlüssel - nicht über den Index!
print(person["name"])
print(person["city"])


#2 — Hinzufügen, aktualisieren, entfernen:
person = {"name": "Alice", "age": 25}

# Neues Schlüssel-Wert-Paar hinzufügen
person["city"] = "Bremen"
print(person)

# Vorhandenen Schlüssel aktualisieren — gleiche Syntax!
person["age"] = 26
print(person)

# Mit del entfernen
del person["age"]
print(person)

# Mit pop() entfernen — gibt den Wert zurück
removed = person.pop("name")
print(removed)
print(person)
print(person["salary"])