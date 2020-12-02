import pygame
import numpy as np


point_color = (249, 127, 81)
hull_color = (27, 156, 252)
line_color = (37, 204, 247)



def main():    
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Convex Hull")
    n = 10
    points = np.random.randint(25, 455, size=2*n)
    
    coords = []
    hull = []
    
    for i in range(0, len(points)-1, 2):
        pygame.draw.circle(win, point_color, (points[i], points[i+1]), 4)
        coords.append([points[i], points[i+1]])
    pygame.display.update()

    
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
   
main()
