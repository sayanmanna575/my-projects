import random 
user_choice = int(input("Enter your choice : Type 0 for rock, 1 for paper, 2 for scissor : "))
if user_choice >=3 or user_choice <0:
    print ("Please enter a valid choice, You Loose !!")
else:
    computer_choice = random.randint(0, 2)
    print("Computer choice")
    print(computer_choice)
    if computer_choice == user_choice:
        print("It's a draw.")
    elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
        print("You Loose.")
    else:
        print("You Win.")
