#CPSC 231 LO1 Spring 2020
#Taimur Rizwan
#UCID: 30078941
#Assignment 1, Problem 7
#Create a program plays a 2 player game of pig

player1_score = 0
player2_score = 0
totalScore1 = 0
totalScore2 = 0

import random

Pig_Out = 1
WIN = 100
player1 = input("Player One, Enter your name: ") #Asks the user for their name
player2 = input("Player Two, Enter your name: ")


#Checks and reiterates the score for both inner loops (player 1 and 2 respectively)
while totalScore1 < WIN and totalScore2 < WIN:


#Player 1's loop    
    player1_score = 0
    dice = 0
    while player1_score < 20 and not dice == Pig_Out and (totalScore1 + player1_score) < WIN:

        
        dice = random.randint(1,6)
        print("Rolled a: ", dice)
   

        if dice == Pig_Out:
            print("Pigged Out!")
            player1_score = 0
            

        else:
            player1_score += dice
            

    if player1_score >= 20:
        print("Hold")

    print(player1, "Turn Score: ", player1_score)
        
    totalScore1 = player1_score + totalScore1
    
    print(player1, "Your New Total Score: ", totalScore1)

#Player 2's loop
    player2_score = 0
    dice = 0
    
    while player2_score < 20 and not dice == Pig_Out and (totalScore2 + player2_score) < WIN :

        
        dice = random.randint(1,6)
        print("Rolled a: ", dice)
   

        if dice == Pig_Out:
            player2_score = 0
            print("Pigged Out!")
            
            

        else:
            player2_score += dice
            


    if player2_score >= 20:
        print("Hold")

    print(player2, "Turn Score: ", player2_score)
        
    totalScore2 = player2_score + totalScore2
    

    print(player2, "Your New Total Score: ", totalScore2)
    
#Comparing the scores
if totalScore1 > totalScore2:
    
    print(player1, "Wins!")

elif totalScore1 < totalScore2:
    
    
    print(player2, "Wins!")

else:
    print("Tie game!")
