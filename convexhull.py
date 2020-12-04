import pygame
import numpy as np

point_color = (249, 127, 81)
hull_color = (27, 156, 252)
line_color = (37, 204, 247)


def direction(a, b, c):
    #(b-a) x (c-a)
    #The points are according to python
    return (((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])) < 0)


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Convex Hull")
    n = 40  #No of points
    points = np.random.randint(25, 455, size=2*n)
    coords = []
    hull = []
    
    #Generting points for convex hull
    for i in range(0, len(points)-1, 2):
        pygame.draw.circle(win, point_color, (points[i], points[i+1]), 4)
        coords.append([points[i], points[i+1]])
    pygame.display.update()

    #find leftmost point, considering only one point
    leftmost_x = min([xcoord[0] for xcoord in coords])
    leftmost_point = [t for t in coords if leftmost_x is t[0]][0]
    pygame.draw.circle(win, (0,0,255), leftmost_point, 4)
    
    current_point = leftmost_point
    
    #Check all points for the next boundary point.
    #The most counter-clockwise point is selected
    while(True):
        hull.append(current_point)
        pygame.draw.circle(win, hull_color, current_point, 5)
        next_point = coords[(coords.index(current_point) + 1)%n]
        #print(next_point, current_point)
        for check_point in coords:
            #With my current point and next point, checking if check_point is to the counter-clockwise
            #if cuurent point and next point both are equal, all values will be 0
            clock.tick(20)
            #pygame.draw.line(win, (0,255,0), current_point,next_point, 2)
            pygame.draw.line(win, (255,0,0), current_point,check_point, 1)
            pygame.display.update()
            if(direction(current_point, next_point, check_point)):
                #print(check_point)
                next_point = check_point
                     
        pygame.draw.line(win, line_color, current_point,next_point, 4)
        current_point = next_point 
        if(current_point == hull[0]):
            break

    #print(l, len(hull))
    #print(hull)
    #pygame.draw.polygon(win, fill_color, hull, 0)
    pygame.display.update()
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
main()

