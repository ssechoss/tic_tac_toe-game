# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:48:58 2018

@author: cen
"""

score_win = 1;
score_lose =-1;
score_draw = 0
import random
import sys
board = []
for i in range (9):
    board.append("*")
result = []
winner = ""
def play():
    global winner
    solution = []
    solution.append(tuple(board))
    

    for i in range(9):
        
        if i%2==0:
            if i == 0:
                move_position = random.randint(0,8)
                
                board[move_position] = "X"
                solution.append(tuple(board))
            else:    
                score,position = maximum_move(board)
                board[position] ="X"
                solution.append(tuple(board))
      
            if  game_finished(get_position("X")):
                winner = "X wins!"
                result.append(solution)
                
                return 
        else:
            score,position = minimum_move(board)
            board[position] = "O"
            solution.append(tuple(board))
          
            if  game_finished(get_position("O")):
                winner = "O wins!"
                result.append(solution)
              
                return 
    result.append(solution)
    winner = "Draw Game! "
def maximum_move(board):
    
    best_score = -sys.maxsize-1;
    best_position = -1;
    for each in get_position("*"):
        board[each] = "X";
       
        if game_finished(get_position("X")):         
            score = score_win
        elif len(get_position("*")) == 0:
            score = score_draw
        else: 
            score,position = minimum_move(board)
        board[each] = "*"
        if best_score == best_score < score:
            best_score = score
            best_position = each
        
    return best_score,best_position
 
def minimum_move(board):
    best_score = sys.maxsize;
    best_position = -1;
    for each in get_position("*"):
        board[each] = "O";       
        if game_finished(get_position("O")):         
            score = score_lose
       
        else:              
            score,positon = maximum_move(board)
        board[each] = "*"
        if  best_score > score:
            best_score = score
            best_position = each 
    return best_score,best_position
       
    

def get_position(a): 
    position = []
    for i in range(9):
        if board[i]==a:
            position.append(i)
    return position
    
def game_finished(position):
    goal_position = [[0,1,2],[3,4,5],[6,7,8],
                     [0,3,6],[1,4,7],[2,5,8],
                     [0,4,8],[2,4,6]]
    for goal in goal_position:
        count = 0
        for each in goal:           
            if each in position:
                count +=1
        if count == 3:
            return True
    return False

def print_result(result):
    play()
    for each in result[0]:
        for i in range(3):
            print(each[i * 3 + 0], each[i * 3 + 1], each[i * 3 + 2])
        print()
    print("Result:",winner)
print_result(result)