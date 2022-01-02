from sys import argv
script, user = argv
prompt = '> '
print("Welcome to Nilfgaard!", end = ' ')
print("Here are the rules! Pay attention, mortal!")
print("You have to give answers.", end = ' ')
print("""
Sometimes the possible answers are given to you, if not feel free.
Got it?
Ok!
Let's go!
""")

print(f"This is {script} and you are {user}")
print("Are you ready to play?")
dont_care = input(prompt)
print(f"I was being polite. your answer: '{dont_care}' is of no relevance here!")

print("You are in front of a door. Do you enter? yes/no")
enter = input(prompt)
if enter == "yes":
    print("Welcome to the black kingdom of Nilfgaard.")
    print ("Now that you are here, what is your plan?")
    plan = input(prompt)
    print(f"'{plan}'??Really??? Ok, whatever!")
    print("Geralt is waiting for you with a horse. Do you search for him? yes/no")
    answer1 = input(prompt)
    if answer1 == "yes":
        print("Are you blind? He is in front of you!")
    elif answer1 == "no":
        print("Oh dear. You are no good. Get out!")
    else:
        print("You don't understand a thing. Get out!")
elif enter == "no":
    print("Go back home, coward! We will come after you!")
else:
    print("I said read the instructions first!")
    print("Try again!")
    answer2 = input(prompt)
    if answer2 == "yes":
        print("Welcome to the black kingdom of Nilfgaard.")
    elif answer2 == "no":
        print("Go back home, coward! We will come after you!")
    else:
        print("You are really stupid. Game over!")
