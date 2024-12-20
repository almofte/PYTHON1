import random

# تعريف الأشكال
rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper = """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """
scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
print ("Welcometo the Rock , paper, Scissars game:\n")
user_choice = input ("Press Enter to continue or type (Help) for the rules").lower

if user_choice == "help":
     print("""
    ********* RULES *********
    1) You choose and the computer chooses.
    2) Rock smashes Scissors -> Rock wins.
    3) Scissors cut Paper -> Scissors wins.
    4) Paper covers Rock -> Paper wins.
    """)

user_choice = input(f"Enter your choice {"Rock , Paper , Scissars"}:"). lower
if user_choice not in ["rock , paper , scissare"]:
    print(f"Invalid choice. Please restart the game and choose from {"Rock , Paper , Scissars"}.") 
else:
    if user_choice == "rock":
        print (f"You chose:\n{rock}")
    elif user_choice == "paper":
        print (f"You chose:\n{paper}")
    else :
        print(f"You chose:\n{scissors}")
random_comp = random.choice(["rock , paper , scissoer"]) 
if random_comp == "rock":
    print (f"computer chose:\n{rock}")
elif random_comp == "paper":
    print (f"computer chose:\n{paper}")
else :
    print (f"computer chose:\n{scissors}")
if user_choice == random_comp :
   print("It's a draw!")
elif ( (user_choice == "rock"and random_comp == "scissoer")or
       (user_choice== "paper" and random_comp == "rock")or
       (user_choice== "scissoer" and random_comp == "paper")): 
       print (f"You Win!{user_choice} beats {random_comp}") 
else:
    print(f"Computer wins!{random_comp} beats {user_choice}")                              
        