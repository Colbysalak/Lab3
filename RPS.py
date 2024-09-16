#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
computer random.choice(["Rock" , "Paper" , "Scissors" ])
 #Prompt the user for their RPS selection
player input("Choose Rock, Paper, or Scissors: ")
print()
if player == "p" or player == "paper" or play == "P"
    player = "Paper"
  
if player == "s" or player == "scissors" or player == "S"
    player = "scissors"
  
if player == "r" or player == "rock" or player == "R"
    player = "rock"

if player == "rock" and computer == "rock"
    print("Player Tie")
    ties = ties + 1

if player == "rock" and computer == "scissors"
    print("Player Win")
    wins = wins + 1

if player == "rock" and computer == "paper"
    print("Player Loss")
    losses = losses + 1

if player == "paper" and computer == "paper"
    print("Player Tie")
    ties = ties + 1

if player == "paper" and computer == "rock"
    print("Player Win")
    wins =  wins + 1

if player == "paper" and computer == "scissors"
    print("Player Loss")
    losses = losses + 1

if player == "scissors" and computer == "paper"
    print("Player Win")
    wins = wins + 1

if player == "scissors" and computer == "scissors"
    print("Player Tie")
    ties = ties + 1

if player == "scissors" and computer == "rock"
    print("Player Loss")
    losses = losses + 1
  
  #Determine winner and state what happened to the user
print()
print("Computer choose "+ computer )
print("You choose "+player )
print()

  #Ask the user if they would like to play again.
play=input("Do you want to play again?" )
print()
if play == "yes" or play == "y" or play == "Y"
  play = "yes"
if play == "no" or play == "n" or play == "N"
  play = "no"
print()
print("End of Game")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
