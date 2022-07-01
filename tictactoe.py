#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[6]+' | '+board[7]+' | '+board[8])
    print('---------')
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('---------')
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('\n')

    pass


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[2]:


# board = [' ']*10
# test_board = [' ']*10
# display_board(board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[3]:


def player_input():
    nomarker = True
    while nomarker:
        marker = input('Please player 1 enter you desire marker (X or O):\n')
        if marker not in ['X','O']:
            print('Please enter a valid value (X or O)\n')
        else:
            nomarker =  False            
            player1 = marker
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
                
            print(f"Thanks!\nPlayer 1 will play as {player1} and Player 2 will play as {player2}\n")
            return (player1,player2)        
    pass


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[4]:


# marker1 , marker2 = player_input()


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[5]:


def place_marker(board, marker, position):
    board[position-1] = marker    
    pass


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[6]:


# place_marker(test_board,marker1,0)
# display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[7]:


def win_check(board, marker):
    
    if board[0]+board[1]+board[2] == marker*3 or board[3]+board[4]+board[5] == marker*3 or board[6]+board[7]+board[8] == marker*3 or board[0]+board[3]+board[6] == marker*3 or board[1]+board[4]+board[7] == marker*3 or board[2]+board[5]+board[8] == marker*3 or board[0]+board[4]+board[8] == marker*3 or board[2]+board[4]+board[6] == marker*3 :
        
        return True
    else:

        return False
    
    pass


# In[8]:


# test_board[0]+test_board[1]+test_board[2]


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[9]:


# win_check(test_board,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[10]:


import random

def choose_first():
    order = random.randint(0, 1)
    if order == 0:
        print('Player 1 goes first!\n')
        return 0
    else:
        print('Player 2 goes first!\n')
        return 1
    


# In[11]:


# choose_first()


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[12]:


def space_check(board, position):
    if board[position-1] == 'X' or board[position-1] == 'O':
        print('This position is already filled!\nPlease enter a new value\n')
        return False
    else:
        return True    
    pass


# In[13]:


# space_check(test_board,0)


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[14]:


def full_board_check(board):
    space = True
    for i in board:
        if i=='X' or i == 'O':
            pass
        else:
            space = False
    return space
    


# In[15]:


test_board2 = ['X','X','X','X','O','X','O','X','O','X']
full_board_check(test_board2)


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[16]:


def player_choice(board):
    position_not = True    
    while position_not:
        position = int(input('What is your next position?\n'))
        if space_check(board, position):
            return position
            position_not = False
        else:
            pass    
        pass


# In[17]:


# player_choice(test_board2)


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[18]:


def replay():
    noanswer = True
    while noanswer:
        play = input('Do you want to continue playing? (Y or N)\n')
        if play in ['Y','N']:
            noanswer = False
            if play == 'Y':
                return True
            else:
                return False
        else:
            print('Please answer Y or N\n')
     
    pass


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[19]:


print('Welcome to Tic Tac Toe!\n')
print('\n')

Game_on = True

while Game_on == True:
    
    board = [' ']*9
    
    marker1 , marker2 = player_input()
    
    turn = choose_first()
    
    Turn_on = True
    
    while Turn_on:
    
    ##Player 1 turn
    
        if turn == 0:
            print('Player1 turn!\n')
            position = player_choice(board)
            place_marker(board, marker1, position)
            display_board(board)
            
            if win_check(board, marker1):
                print('Congratulations player 1!, You have won the game!!\n')
                Turn_on = False
                    
            if full_board_check(board):
                print('The board is full! TIE GAME\n')
                Turn_on = False
                
            
            turn = 1
            

        else:         
            print('Player2 turn!\n')
            position = player_choice(board)
            place_marker(board, marker2, position)
            display_board(board)
            
            if win_check(board, marker2):
                print(f'Congratulations player 2!, You have won the game!!\n')
                Turn_on = False
                
            if full_board_check(board):
                print('The board is full! TIE GAME\n')
                Turn_on = False
                    
            turn = 0

    
    
    print('\n')
    
    if replay():
        pass
    else:
        Game_on = False
        print('Game finished!\n Thanks for playing Tic Tac Toe!\n')
    
   







