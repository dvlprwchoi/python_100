import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

unvalid = '''
xxxxxxxx
'''

user_num = input(
    "What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors.\n:")
computer_num = str(random.randint(0, 2))
# print(computer_num)

if user_num == "0":
    user = rock
elif user_num == "1":
    user = paper
elif user_num == "2":
    user = scissors
else:
    user = unvalid

if computer_num == "0":
    computer = rock
elif computer_num == "1":
    computer = paper
else:
    computer = scissors

print("You chose:\n" + user)
print("Computer chose:\n" + computer)

if user_num == computer_num:
    print("Tied...Try it again!")
else:
    if user_num == "0":
        if computer_num == "1":
            print("Computer won!")
        else:
            print("You won!")
    elif user_num == "1":
        if computer_num == "0":
            print("You won!")
        else:
            print("Computer won!")
    elif user_num == "2":
        if computer_num == "0":
            print("Computer won!")
        else:
            print("You won!")
    else:
        print("Try it again...Choose number only from 0, 1, or 2")
