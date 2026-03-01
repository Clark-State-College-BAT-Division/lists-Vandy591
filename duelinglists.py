#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Again, your lists should be random numbers
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = 5,7,2,9,1,1,3,8,6,9
#Player Two = 3,8,5,5,8,1,4,7,4,7
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random
player1 = []
player2 = []
for i in range(10):
    player1.append(random.randint(1, 50)) 
    player2.append(random.randint(1, 50))
player1_wins = 0
player2_wins = 0
for i in range(10):
    if player1[i] > player2[i]:
        player1_wins += 1
    elif player2[i] > player1[i]:
        player2_wins += 1
p1highest = player1[0]
p1highest_index = 0
for i in range(10):
    if player1[i] > p1highest:
        p1highest = player1[i]
        p1highest_index = i
p2highest = player2[0]
p2highest_index = 0
for i in range(10):
    if player2[i] > p2highest:
        p2highest = player2[i]
        p2highest_index = i
p1lowest = player1[0]
p1lowest_index = 0
for i in range(10):
    if player1[i] < p1lowest:
        p1lowest = player1[i]
        p1lowest_index = i
p2lowest = player2[0]
p2lowest_index = 0
for i in range(10):
    if player2[i] < p2lowest:
        p2lowest = player2[i]
        p2lowest_index = i
print("Player one's lowest number is", p1lowest, "at index", p1lowest_index)
print("Player two's lowest number is", p2lowest, "at index", p2lowest_index)