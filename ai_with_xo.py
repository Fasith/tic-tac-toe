import pygame
import time
import random

pygame.init()


#board
board = [['_']*3 for i in range(0,3)]


#determine player
player = 1

#colours
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

#display
display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()


# creating the game ui
gameDisplay.fill(white)
pygame.draw.line(gameDisplay,green,(0,200),(600,200),4)
pygame.draw.line(gameDisplay,green,(0,400),(600,400),4)
pygame.draw.line(gameDisplay,green,(200,0),(200,600),4)
pygame.draw.line(gameDisplay,green,(400,0),(400,600),4)

pygame.display.update()


def minimax(board,depth,isMax):
    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score
    if (isMovesLeft(board) == False):
        return 0
    if (isMax):
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = max(best,minimax(board,depth+1,False))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] =='_':
                    board[i][j] = 'X'
                    best = min(best,minimax(board,depth+1,True))
                    board[i][j] = '_'

        return best
                    


def findBestMove(board):
    bestVal = -1000
    row = -1
    column = -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                moveVal = minimax(board,0,False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestVal = moveVal
                    row = i
                    column = j
    return (row,column,bestVal)


def pressed(x,y,board):   
    

    xx = x//200
    yy = y//200

    if board[xx][yy] != '_':
        return
    else:
        board[xx][yy] = 'X'
        print(board)
        if(isMovesLeft(board) == True):
            values = findBestMove(board)
            print(values)
            board[values[0]][values[1]] = 'O'
    
        
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True

    return False
        
       
        
def current_board(board):
    
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'O':
                font = pygame.font.SysFont(None,100)
                text = font.render("O",True,red)
                gameDisplay.blit(text,(x*200,y*200))
                
            elif board[x][y] == 'X':
                font = pygame.font.SysFont(None,100)
                text = font.render("X",True,blue)
                gameDisplay.blit(text,(x*200,y*200))
                

def evaluate(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return -10
            elif board[i][0] == 'O':
                return 10

        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return -10
            elif board[0][i] == 'O':
                return 10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return -10
        elif board[0][0] =='O':
            return 10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return -10
        elif board[0][2] == 'O':
            return 10

    return 0

    
            

    


def game_loop():

    #a = random.randint(0,2)
    a = 1
    print(a)
    if a == 1:
        pos = findBestMove(board)
        board[pos[0]][pos[1]] = 'O'
        current_board(board)
        

    while True:
        
        
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:        
            pressed(mouse[0],mouse[1],board)

        current_board(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        status = evaluate(board)
        if status == 10:
            font = pygame.font.SysFont(None,100)
            text = font.render("Player 'O' wins ",True,green)
            gameDisplay.blit(text,(0,300))
            #break
        elif status == -10:            
            font = pygame.font.SysFont(None,100)
            text = font.render("Player 'X' wins ",True,green)
            gameDisplay.blit(text,(0,300))
            #break

        if(isMovesLeft(board) == False) and status == 0:
            font = pygame.font.SysFont(None,100)
            text = font.render(" Match Draw ",True,green)
            gameDisplay.blit(text,(0,300))
            

        pygame.display.update()
        clock.tick(60)





game_loop()
#wait_loop()
        
    
    





            
