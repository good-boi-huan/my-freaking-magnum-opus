# # Print Hello Arda
# print("hello")

# name = input("What is your name? ")
# age = input("How old are you? ")
# fav_activity = input("What is your favorite activity? ")
# book = input("What is your favorite book? ")

# # Concatination
# print("Your name is " + name)
# print("Your age is " + age)
# print("You favorite activity is " + fav_activity)
# print("Your favorite book is " + book)

# # Data Type Conversion
# var_1 = 1
# var_string = str(var_1)
# print(var_1)
# print(var_string)
# # int()
# # float()
# # str()

# Arithmetic Operators
# addition + 
# subtraction - 
# multiplication *
# division /

# Get perimeter of rectangle
# User inputs length and width
# Console outputs perimeter
# length = input("Give me a length ")
# width = input("Give me a width ")
# length2 = float(length)
# width2 = float(width)
# perimeter = (2.0*length2)+(2.0*width2)

# print("The perimeter of a",length,"by",width,"rectangle is",perimeter)

# String manip
# Concatination: "hello" + "world" -> "hello world"
# length: gives how many characters a string is, "hello" -> len("hello") = 5
# upper: convert all characters in a string to uppercase, "hello" -> "HELLO"
# lower: convert all characters in a string to lowercase, "HELLO" -> "hello"

# string1 = "can you hear me?"
# string2 = "CAN YOU HEAR ME?"

# print(string1.upper())
# print(string2.lower())
# print(len(string1))
# print(string1,string2)

# string formatting
# name = input("What is your name? ")
# number = float(input("Give me a number "))
# print(f"Your name is {name} and you will die in {number} days.")
# new line print("\n")

# name = "Feanor"
# number = "20"
# print("My name is {0} and I will die in {1} days.".format(name,number))

# Madlibs
name = input("Give me your name ")
print(f"Hello {name}. Are you ready for this? Zimzalabim...")
supervillain = input("Give me a supervillain ")
superhero = input("Give me a superhero ")
adj_1 = input("Give me an adjective ")
adj_2 = input("Give me another adjective ")
animal_1 = input("Give me an animal ")
animal_2 = input("Give me another animal ")
person_1 = input("Give me a person's name ")
person_2 = input("Give me another person's name ")
person_3 = input("Give me another person's name ")
country = input("Give me a country ")
noun_1 = input("Give me a noun ")
noun_2 = input("Give me another noun ")
weapon = input("Give me a weapon ")
noun_3 = input("Give me another noun ")
noun_4 = input("Give me another noun ")
noun_5 = input("Give me another noun ")
verb_1 = input("Give me a verb (no 'to' before it) ")
verb_2 = input("Give me a verb (no 'to' before it) ")
verb_3 = input("Give me a verb (no 'to' before it) ")
verb_4 = input("Give me a verb (no 'to' before it) ")
verb_5 = input("Give me a verb (no 'to' before it) ")
celebrity_1 = input("Give me a celebrity ")
place = input("Give me a place ")
celebrity_2 = input("Give me another celebrity ")
celebrity_3= input("Give me another celebrity ")
 
print(f"Be he {supervillain} or {superhero}, be he {adj_1} or {adj_2},\nbrood of {animal_1} or bright {animal_2},\n{person_1} or {person_2} or {person_3},\n{person_3} yet unborn upon {country},\nneither {noun_1}, nor {noun_2}, nor league of {weapon},\n{noun_3} nor {noun_4}, not {noun_5} itself,\nshall defend him from {name}, and "+name+"'s kin,\nwhoso "+verb_1+"eth or "+verb_2+"eth, or in hand "+verb_3+"eth,\nfinding "+verb_4+"eth or afar "+verb_5+f"eth\na Silmaril. This swear we all:\ndeath we will deal him ere Day's ending,\nwoe unto world's end! Our word hear thou,\n{celebrity_1}! To the everlasting\n{place} doom us if our deed faileth.\nOn the holy mountain hear in witness\nand our vow remember, {celebrity_2} and {celebrity_3}!")