#!/usr/bin/env python3
import subprocess as sp

#logic for printing board
def print_board():
    sp.call('clear',shell=True)
    global fresh_game
    print("--------------")
    print('Player 1 is X')
    print('Player 2 is O')
    if fresh_game: print('Player 1 goes first')
    print("--------------")
    print_str=""
    count=0
    for i in nums:
        print_str+= " "+str(i)
        count+= 1
        if count%3 == 0:
            print(" "+print_str)
            print(line_separator)
            print_str=""
        else: print_str+=col_separator
    print("--------------")
    fresh_game = False

#logic for deciding the winner
def game_ended(player_inputs):
    #print(player_inputs)
    winning_count = 0
    #print('winning sequence');print(len(winning_sequence));
    for i in range(0,len(winning_sequence)):
        #print('first winning sequence');print(len(winning_sequence[i]));print(winning_sequence[i])
        winning_count = 0
        for j in range(len(winning_sequence[i])):
            if winning_sequence[i][j] in player_inputs:
                winning_count+=1
                #print('winning count');print(winning_count)
            if winning_count >= 3: return True
    return False

#logic for claiming a spot on the board
def claim_spot(input,replace_with):
    index = nums.index(input)
    nums[index] = replace_with

player1=[] #to store player 1's game
player2=[] #to store player 2's game
nums=[1,2,3,4,5,6,7,8,9]
allowed_nums=[1,2,3,4,5,6,7,8,9]
line_separator=" ---|---|---"
col_separator=" |"
winning_sequence=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[2,5,8],[1,4,7],[3,6,9],[3,5,7]]
fresh_game=True
still_on=True
player2_playing= False #flag to recognize who is playing
while(still_on):
    #sp.call('clear',shell=True)
    if not player2_playing:
        print_board()
        print("------------------------------------------")
        print("-- Player 1: Choose a number to place X --")
        print("------------------------------------------")
        player1_input = int(input())
        if player1_input not in allowed_nums:
            print("Please choose wisely")
            player2_playing= False
            continue
        if player1_input not in nums:
            print("Number already taken. Choose Wisely!")
            player2_playing= False
            continue
        player1.append(player1_input)
        claim_spot(player1_input,'X')
        print_board()
    if game_ended(player1):
        still_on=False
        print("------------------------------------------")
        print("Game Ended -- Winner is : Player 1")
        print(player1)
        print("------------------------------------------")
        break
    print("------------------------------------------")
    print("-- Player 2: Choose a number to place O --")
    print("------------------------------------------")
    player2_input = int(input())
    if player2_input not in allowed_nums:
        print("Please choose wisely")
        player2_playing = True
        continue
    if player2_input not in nums:
        print("Number already taken. Choose Wisely!")
        player2_playing = True
        continue
    player2.append(player2_input)
    player2_playing = False
    #player2.sort()
    claim_spot(player2_input,'O')
    print_board()
    if game_ended(player2):
        still_on=False
        print("------------------------------------------")
        print("Game Ended -- Winner is : Player 2")
        print(player2)
        print("------------------------------------------")
        break
