import random

num_Of_rounds = int(input("Tell the number of rounds you want to play :=> "))

choices = ['rock', 'paper','scissors']

comp_points = 0
user_points = 0

# rules:
# rock beats scissors, scissor beats paper and paper beats rock
i = 0
for i in range(num_Of_rounds):
    user =  None
    while user not in choices:
        user = input("Choose rock, Paper or Scissors ? ").lower()
    computer = random.choice(choices)
    print("My Choice is : ", computer)

    print("Round Number = ", i+1)

    if user == computer:
        print("It's a Tie !")
    elif user == 'scissors' and computer == 'rock':
        print("I Win !")
        comp_points += 1
    elif user == 'rock' and computer == 'scissors':
        print("You Win !")
        user_points += 1
    elif user == 'rock' and computer == 'paper':
        print("I Win !")
        comp_points += 1
    elif user == 'paper' and computer == 'rock':
        print("You Win !")
        user_points += 1
    elif user == 'paper' and computer == 'scissors':
        print("I Win !")
        comp_points += 1
    elif user == 'scissors' and computer == 'paper':
        print("You Win !")
        user_points += 1

print("It's the end of the match ! \n")
print("Computer Score : ", comp_points)
print('Your Score : ', user_points)

