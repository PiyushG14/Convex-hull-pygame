import pygame
import numpy as np




def main():
    pygame.init()
    win = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Convex Hull")
    points = np.random.randint(50, 750, size=40)
    coords = []

    #Generting points for convex hull
    for i in range(0, len(points)-1):
        pygame.draw.circle(win, (255,255,255), (points[i], points[i+1]), 5)
        coords.append([points[i], points[i+1]])
        pygame.display.update()

    #find leftmost point, considering only one point
    first_coord = min([xcoord[0] for xcoord in coords])
    print(first_coord, coords)


    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
main()

