from platform import machine
import random
ties=0
losses=0
wins=0
print("ROCK, PAPER, SCISSORS")
print(str(wins) + " Wins, "+str(losses)+" Losses, "+str(ties)+" Ties")
print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
option=input()
while option != "q":
    random_value = random.randint(1,3)
    player_value = 0
    if str.lower(option) == "r":
        player_value = "ROCK"
    elif str.lower(option) == "p":
        player_value = "PAPER"
    elif str.lower(option) == "s":
        player_value = "SCISSORS"
    else:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        option=input()
        continue
    
    if random_value == 1:
        machine_value = "ROCK"
    elif random_value == 2:
        machine_value = "PAPER"
    else:
        machine_value = "SCISSORS"
    
    print(player_value + " versus...")
    print(machine_value)
    
    if player_value == machine_value:
        print("It is a tie!")
        ties+=1
    elif player_value == "PAPER" and machine_value == "ROCK":
        print("You win!")
        wins+=1
    elif player_value == "PAPER" and machine_value == "SCISSORS":
        print("You lose!")
        losses+=1
    elif player_value == "ROCK" and machine_value == "SCISSORS":
        print("You win!")
        wins+=1
    elif player_value == "ROCK" and machine_value == "PAPER":
        print("You lose!")
        losses+=1
    elif player_value == "SCISSORS" and machine_value == "PAPER":
        print("You win!")
        wins+=1
    elif player_value == "SCISSORS" and machine_value == "ROCK":
        print("You lose!")
        losses+=1

    print(str(wins) + " Wins, "+str(losses)+" Losses, "+str(ties)+" Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    option=input()
