#CPSC 231 LO1 Spring 2020
#Taimur Rizwan
#UCID: 30078941
#Assignment 2, Problem 2
#Create a program that determines average seen, most/least popular movies and hi/lowest rated movies

# Movies list contains the list of 30 moives names
#
movies = ["Wall-E (2008)",
"The Ring (2002)", 
"Minions (2015)", 
"The Mummy (1999)",
"Mean Girls (2004)",
"Million Dollar Baby (2004)",
"The Desolation of Smaug (2013)",
"Love Actually (2003)",
"Scarface (1983)",
"Oldboy (2003)", 
"Die Hard (1988)",
"The Bourne Identity (2002)",
"The Secret Life of Walter Mitty (2013)",
"The Incredibles (2004)",
"Battleship (2012)",
"The Strangers (2008)",
"Ratatouille (2007)",
"Toy Story (1995)",
"Dogville (2003)",
"Million Dollar Baby (2004)",
"The Desolation of Smaug (2013)",
"Love Actually (2003)",
"Scarface (1983)",
"Oldboy (2003)",
"Stalker (1979)",
"Up (2009)",
"Thor: Ragnarok (2017)",
"The Matrix Revolutions (2003)",
"What We Do in the Shadows (2014)",
"Deadpool (2016)"
]

#
# all_ratings contains the rating of every movie from 4 friends
#

all_ratings = [
[5,5,4,4,3,1,2,3,4,4,4,3,4,0,0,0,1,2,3,4,4,4,1,4,0,0,0,1,2,5],
[5,0,1,2,3,1,2,3,4,4,4,5,4,2,1,0,1,2,0,5,0,4,1,4,2,0,0,1,0,5],  
[5,2,3,4,4,0,0,0,4,5,0,3,0,0,0,3,4,0,1,4,4,4,0,4,0,3,0,1,2,5],  
[5,0,4,0,0,4,2,3,0,0,4,0,3,0,1,0,1,2,3,0,2,0,1,0,0,0,4,0,1,5],  
[5,4,3,2,1,1,2,3,4,3,4,3,4,0,3,0,1,2,4,4,4,4,1,4,0,0,0,1,2,5],  
]
def isMovieBest(): #4
    TOTAL_HIGHEST = 25
    TOP_AVG = 1
    numViewsList = [0] * len(movies)
    for i in range(0, len(all_ratings)):

        for j in range(0, len(all_ratings[i])):

            if all_ratings[i][j] != 0:
                
                if all_ratings[i][j] == 5:
                    numViewsList[j] = numViewsList[j] + 1

                    total_rate = sum(numViewsList)

                    average = total_rate / TOTAL_HIGHEST

                    return average

                if average == 1:

                    print(movies[i])


                                                     

                
            
def isMovieWorst(): #5
    TOTAL_HIGHEST = 25
    TOP_AVG = 1
    numViewsList = [0] * len(movies)
    for i in range(0, len(all_ratings)):

        for j in range(0, len(all_ratings[i])):

            if all_ratings[i][j] != 0:
                
                if all_ratings[i][j] == 1:
                    numViewsList[j] = numViewsList[j] + 1

                    total_rate = sum(numViewsList)

                    average = total_rate / TOTAL_HIGHEST

                    if average == 1:

                        print(movies[i])
            
def seenMovies(): #1

    

    new_ratings = [0] * len(all_ratings)
    for i in range(len(all_ratings)):
        count = 0
        for j in range(len(all_ratings[i])):

            if all_ratings[i][j] != 0:
                count = count + 1 #adds 1 to the count over and over again until it reads 0
                
        new_ratings[i] = count #stores the count into the list

    average = sum(new_ratings) / len(new_ratings) 
    return average

def mostPopular(): #2

    numViewsList = [0] * len(movies) #new list is the size of elements in all movies
    for i in range(0, len(all_ratings)): #reiterates all 5 sublists

        for j in range(0, len(all_ratings[i])): #reiterates each element of the sublist

            if all_ratings[i][j] != 0: #it loops until a zero is found under i-siblist and j-index
                numViewsList[j] = numViewsList[j] + 1 #for the values that aren't 0; the new list elements increment by 1 

    for i in range(len(numViewsList)): #now we're iterating through the new list
        if numViewsList[i] == max(numViewsList): #if i is equal to the max then you put the i index into movies
            
            print(' ',movies[i])

                

def leastPopular(): #3

    numViewsList = [0] * len(movies)
    for i in range(0, len(all_ratings)):

        for j in range(0, len(all_ratings[i])):

            if all_ratings[i][j] != 0:
                numViewsList[j] = numViewsList[j] + 1

    for i in range(len(numViewsList)):
        if numViewsList[i] == min(numViewsList):
            
            print(" ", movies[i])
    

def main():
#For seenMovies() function:
    avg_seen = seenMovies()

    print("On average, each person has seen", avg_seen, "out of the 30 movies\n")

#For mostPopular() function:
    print("The most popular movies were: \t")
    mostPopular()

    

#For leastPopular() function:
    print("\nThe least popular movies were: ")
    leastPopular()

#For isMovieBest() function:

    res_best_movies = isMovieBest()

    print("The highest rated movies were: \n", res_best_movies)

#For isMovieWorst() function:
    res_worst_movies = isMovieWorst()

    print("The lowerst rated movies were: \n", res_worst_movies)



    
    
    
main()
