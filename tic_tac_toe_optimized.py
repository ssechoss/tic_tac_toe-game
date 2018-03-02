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
    path = []
    move_position = random.randint(0,8)
    board[move_position] = "X"
    first_state = board
   
    score,path =minimum_move(board)
    path.insert(0,first_state)
   
    if score == score_draw:
        winner = "Draw Game! "
    elif score == score_win:
        winner = "X wins!"
    else:
        winner = "O wins!"
    result.append(path)
def maximum_move(board):
    
    best_score = -sys.maxsize-1;
    best_path = []
    for each in get_position("*"):
        path = []
        board[each] = "X";
       
        if game_finished(get_position("X")):         
            score = score_win
            path.append(tuple(board))
        elif len(get_position("*")) == 0:
            score = score_draw
            path.append(tuple(board))
        else: 
            score,path = minimum_move(board)
            path.insert(0,tuple(board))
        board[each] = "*"
        if best_score == best_score < score:
            best_score = score
            best_path = path
        
    return best_score,best_path
 
def minimum_move(board):
    best_score = sys.maxsize;
    best_path = []
    
    for each in get_position("*"):
        path = []
        board[each] = "O";       
        if game_finished(get_position("O")):         
            score = score_lose
            path.append(tuple(board))
       
        else:              
            score,path = maximum_move(board)
            path.insert(0, tuple(board))
        board[each] = "*"
        if  best_score > score:
            best_score = score
            best_path = path
    return best_score,best_path
       
    

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