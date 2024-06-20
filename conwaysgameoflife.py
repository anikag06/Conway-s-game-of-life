#Running pygame
import pygame
pygame.init()
# making the screen
cell_size=10
grid_height = int(input("Set the height of the grid: ")) 
grid_width = int(input("Set the width of the grid: ")) 
screen_height=grid_height*cell_size
screen_width=grid_width*cell_size
screen = pygame.display.set_mode((screen_width,screen_height))
# Making the grid
import random
def make_grid(width,height,randomize=True):
    grid=[[0 for _ in range(width)] for _ in range(height)]
    if randomize:
        grid=[[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]
    else:
        grid=[[0 for _ in range(width)] for _ in range(height)]
    return grid

# colours for cells
grid_colour=(128,128,128)
alive_colour=(255,255,0)
dead_colour=(0,0,0)
fps=3 #frame rate

#drawing the grid
def draw_grid(screen,grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])): #setting the colour
            if grid[y][x]==1:
                colour=alive_colour
            else:
                colour=dead_colour
            pygame.draw.rect(screen,colour,(x*cell_size,y*cell_size,cell_size,cell_size)) #making appropriate rectangles
            pygame.draw.rect(screen,grid_colour,(x*cell_size,y*cell_size,cell_size,cell_size), 1)
#implementing the rules of the game
def grid_change(grid):
    #initializing line with 0s
    new_grid=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    for y in range(len(grid)):
        for x in range(len(grid[0])):
             #counting the alive neighbours
            alive_neighbours=sum([grid[(y+1)%len(grid)][(x+1)%len(grid[0])],
                             grid[(y+1)%len(grid)][(x-1)%len(grid[0])],
                             grid[(y+1)%len(grid)][x],
                             grid[(y-1)%len(grid)][(x+1)%len(grid[0])],
                             grid[(y-1)%len(grid)][(x-1)%len(grid[0])],
                             grid[(y-1)%len(grid)][x],
                             grid[y][(x+1)%len(grid[0])],
                             grid[y][(x-1)%len(grid[0])]])
            if grid[y][x]==1 and (alive_neighbours==2 or alive_neighbours==3):
                new_grid[y][x]=1
            elif grid[y][x]==0 and alive_neighbours==3:
                new_grid[y][x]=1
    return new_grid
def main():
    grid=make_grid(grid_width,grid_height)
    clock = pygame.time.Clock()
    running=False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quit game
                pygame.quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE: #toggle start stop using space
                    running=not running
                elif event.key==pygame.K_r: #reset grid using R
                    grid=make_grid(grid_width,grid_height,randomize=True)
                    running=False
                elif event.key==pygame.K_c: #clear grid using C
                    grid=make_grid(grid_width,grid_height,randomize=False)
                    running=False
                elif event.key == pygame.K_RIGHT and not running: #press right arrow to move by one step
                    grid = grid_change(grid)
            elif event.type == pygame.MOUSEBUTTONDOWN and not running: #change state of cell
                pos = pygame.mouse.get_pos()
                x= pos[0] // cell_size
                y=pos[1] //cell_size
                grid[y][x] = 1-grid[y][x]
        screen.fill(dead_colour)
        draw_grid(screen,grid)
        if running:
            grid=grid_change(grid)
            clock.tick(fps)
        pygame.display.flip()

main()






