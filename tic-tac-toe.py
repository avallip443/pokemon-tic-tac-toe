import pygame 
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

# style variables
dark_blue = (51, 58, 115)
beige = (238, 237, 235)
line_width = 4
font = pygame.font.SysFont(None, 40)
again_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50) # create play again rectangle

# define game variables
markers = [[0 for _ in range(3)] for _ in range(3)]
clicked = False
pos = []
player = 1
winner = 0
game_over = False
run = True


def initialize_game():
    global markers, clicked, pos, player, winner, game_over
    
    markers = [[0 for _ in range(3)] for _ in range(3)]
    clicked = False
    pos = []
    player = 1
    winner = 0
    game_over = False


def draw_grid():
    background_img = pygame.image.load("resources/bg.jpg").convert()
    background_img = pygame.transform.scale(background_img, (screen_width, screen_height))
    grid = (50, 50, 50)
    screen.blit(background_img, (0, 0))

    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 200), (screen_width, x * 200), line_width)
        pygame.draw.line(screen, grid, (x * 200, 0), (x * 200, screen_height), line_width)
    

def draw_markers():
    player1_img = pygame.image.load("resources/snorlax.png").convert_alpha()
    player1_img = pygame.transform.scale(player1_img, (200, 200)) 
    player2_img = pygame.image.load("resources/psyduck.png").convert_alpha()
    player2_img = pygame.transform.scale(player2_img, (200, 200))
        
    for x_pos, row in enumerate(markers):
        for y_pos, cell in enumerate(row):
            if cell == 1:
                screen.blit(player1_img, (x_pos * 200, y_pos * 200))
            elif cell == -1:
                screen.blit(player2_img, (x_pos * 200, y_pos * 200))
        

def check_winner():
    global winner, game_over
    
    # check rows and columns
    for i in range(3):
        if sum(markers[i]) == 3 or sum(markers[j][i] for j in range(3)) == 3:
            winner = 1
            game_over = True
        elif sum(markers[i]) == -3 or sum(markers[j][i] for j in range(3)) == -3:
            winner = 2
            game_over = True
    
    # check diagonals
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == 3:
        winner = 1
        game_over = True
    elif markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[0][2] + markers[1][1] + markers[2][0] == -3:
        winner = 2
        game_over = True
 

def draw_winner(winner):
    win_text = 'Player ' + str(winner) + ' wins !'
    win_img = font.render(win_text, True, beige)
    pygame.draw.rect(screen, dark_blue, (screen_width // 2 - 120, screen_height // 2 - 60, 240, 50))

    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))
    
    again_text = "Play again?"
    again_img = font.render(again_text, True, beige)
    pygame.draw.rect(screen, dark_blue, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))
      
    
while run:
    draw_grid()
    draw_markers()
    
    # add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x, cell_y = pos[0] // 200, pos[1] // 200

                if markers[cell_x][cell_y] == 0:
                    markers[cell_x][cell_y] = player
                    player *= -1
                    check_winner()
    
    if game_over:
        draw_winner(winner)
        
        # check for mouselick to see if user has clicked on play again
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            
            if again_rect.collidepoint(pos):  
                initialize_game()
                
    pygame.display.update()
    
pygame.quit()
            