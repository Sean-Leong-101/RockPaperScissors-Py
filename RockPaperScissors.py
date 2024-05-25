# This program is a coded version of Rock Paper Scissors
# It takes in an input from the user and randomly chooses the cpu's choice
# from the pool of choices.
# Coded on 25/5/2024
# Tutorial from https://thecleverprogrammer.com/2021/01/10/rock-paper-and-scissors-game-with-python/

import random
import os

pool = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0


while True:
    player = input("Rock, Paper or Scissors? ").capitalize()
    random.shuffle(pool)
    cpu = pool[0]
    print("CPU chooses", cpu)
    if player == cpu:
        print("Tie!")
    elif player == "Rock":
        if cpu == "Paper":
            print("You lose!", cpu, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", cpu)
            player_score+=1
    elif player == "Paper":
        if cpu == "Scissors":
            print("You lose!", cpu, "cuts", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", cpu)
            player_score+=1
    elif player == "Scissors":
        if cpu == "Rock":
            print("You lose...", cpu, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cuts", cpu)
            player_score+=1
    elif player=='End':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================")
        if player_score > cpu_score:
            print("Congratualtions you won!!!")
        elif player_score == cpu_score:
            print("Damm it was a tie!!!")
        else:
            print("Unlucky you lost try again!!")
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        print("========================")
        print("")
        break