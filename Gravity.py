import pygame
from pygame.draw import rect

WIDTH,HEIGHT=400,400
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
SQUARE_D=(10,10)
PARTCOUNT=3000
# gravity
GRAV=0.2
# energy loss from bouncing
LOSS=0.65

class Particle(pygame.Rect):
    def __init__(self,x,y, l,w,color=GREEN,xv=0.0,yv=0.0,bounced=False):
        super().__init__(x, y, l,w)
        self.color = color 
        self.xv=xv
        self.yv=yv
        self.bounced=bounced
        
    
def bounce(rect):
    if rect.color==RED:
        rect.color=GREEN
    else:
        rect.color=RED
    rect.yv*= -1*LOSS
    rect.y=HEIGHT-1

def accelerate (rect):
    rect.yv+=GRAV
    rect.y+=rect.yv

def update_rects(rect_arr):
    i =0
    while i < len(rect_arr):
        if(rect_arr[i].y>=HEIGHT):
            if rect_arr[i].yv>4:
                bounce(rect_arr[i])
                pygame.draw.rect(WIN,rect_arr[i].color,rect_arr[i])
            else:
                # particle gets deleted after becoming too slow
                rect_arr.remove(rect_arr[i])
        else: 
            accelerate(rect_arr[i])
            pygame.draw.rect(WIN,rect_arr[i].color,rect_arr[i])
        
        i+=1
        

# def colide(rect_arr):
#     i=0
#     while i<len(rect_arr):
#         x=0
#         while x<len(rect_arr):
#             if not x==i and rect_arr[i].collidepoint(rect_arr[x].x,rect_arr[x].y):
#                 pygame.draw.rect(WIN,RED,rect_arr[x])
#                 pygame.draw.rect(WIN,BLUE,rect_arr[i])
#             x+=1
#         i+=1

def main():
    clock = pygame.time.Clock()
    run=True
    rect_arr=[]
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        if pygame.mouse.get_pressed()[0] and len(rect_arr)<PARTCOUNT:
            mousepos=pygame.mouse.get_pos()
            rect=Particle(mousepos[0],mousepos[1],10,10)
            rect_arr.append(rect)
            pygame.draw.rect(WIN,rect.color,rect)
        update_rects(rect_arr)
        # colide(rect_arr)
        pygame.display.update()
        WIN.fill(BLACK)
    pygame.quit()

if __name__ == "__main__":
    main()