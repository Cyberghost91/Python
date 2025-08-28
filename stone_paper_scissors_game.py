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
list_1 = [rock, paper, scissors]
choice_1 = int(input("What do you choose? "
                 "Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
random_list = random.choice(list_1)
if choice_1 == 0:
    print(f"You chose: rock \n{rock}")
    if random_list == list_1[0]:
        print(f"computer chose: rock {rock}\n 'try again'")
    elif random_list == list_1[1]:
        print(f"computer chose: paper {paper}\n 'you lose'")
    else:
        print(f"computer chose: scissors {scissors}\n 'you win!'")
elif choice_1 == 1:
    print(f"You chose: paper \n{paper}")
    if random_list == list_1[0]:
        print(f"computer chose: rock {rock}\n 'you win!'")
    elif random_list == list_1[1]:
        print(f"computer chose: paper {paper}\n 'try again'")
    else:
        print(f"computer chose: scissors {scissors}\n 'you lose!'")
elif choice_1 == 2:
    print(f"You chose: scissors \n{scissors}")
    if random_list == list_1[0]:
        print(f"computer chose: rock {rock}\n 'you lose!'")
    elif random_list == list_1[1]:
        print(f"computer chose: paper {paper}\n 'you win!'")
    else:
        print(f"computer chose: scissors {scissors}\n 'try again'")
else:
    print("'you entered wrong input!'")