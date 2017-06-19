# Exercises from The Self-Taught Programmer

# Challenge 1
# 1. Print each item in the following list: [" The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in list:
    print(show)

# Challenge 2
# 2. Print all the numbers from 25 to 50.

for num in range(25, 51):
    print(num)
    
# Challenge 3
# 3. Print each item in the list from the first challenge and their indexes.
# I'm going to come back to this one
# NOTE: I had to look at the answers for this one. :/

for index, show in enumerate(list):
    print(index)
    print(show)

# Challenge 4
# 4. Write a program with an infinite loop (with the option to type q to quit) and a list of numbers. Each time through the loop ask the user to guess a number on the list and tell them whether or not they guessed correctly.


# Need to find out how to do this without getting a Traceback if the list is full of integers but the guess is q...

# truth = True
# numbers = ["1", "2", "3", "4", "5", "6"]
numbers = [1, 2, 3, 4, 5, 6]

# while truth == True:
#     guess = input("Guess if a number is in the list: ")
#     if guess in numbers:
#         print("Correct")
#     elif guess.lower() == "q":
#         truth = False
#         print("Stopping now.")
#         break
#     else:
#         print("Incorrect. Guess again.")

# Okay, this here is the official answer (looked it up), modified a bit:
while True:
    answer = input("Guess a number, or type q to quit: ")
    if answer == "q":
        print("Okay. Stopping now.")
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Please type a number, or type q to quit.")
    if answer in numbers:
        print("Correct.")
    else:
        print("Not found. Guess again.") # I don't like that this part is included with the ValueError message
        
# Challenge 5
# 5. Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in the list [9, 1, 33, 83], and append each result to a third list.

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multiplied = []

for i in list1:
    for j in list2:
        multiplied.append(i * j)
print(multiplied)
