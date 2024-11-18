#Kalea T Whackamole
import pygame
import random

def main():
    #Ta provided this code
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole")
        mole_image = pygame.image.load("mole.png")
        clock = pygame.time.Clock()
        running = True
        #Assigns starting coordinates to mole
        mole = (0,0)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #Checks if user has clicked mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # x mole and y mole takes the values of the x and y coordinate of the moles position
                    x_mole_cord, y_mole_cord = mole
                    #x mole checks if the mouse click is within the horizontal range of the mole
                    #y mole checks if the mouse click is within the vertical range of the mole
                    if x_mole_cord <= event.pos[0] <= x_mole_cord + 64 and y_mole_cord <= event.pos[1] <= y_mole_cord + 64:
                        #Prints moles coordinates
                        print(event.pos)
                        #Generates random x and y coordinates
                        mole = (random.randrange(0, 10) * 64, random.randrange(0, 8) * 64)

            screen.fill("light green")

            #Ta provided this code
            for i in range(10):
                pygame.draw.line(screen, color=pygame.Color("blue"), start_pos=(i * 64, 0), end_pos=(i * 64, 512))
            for i in range(8):
                pygame.draw.line(screen, color=pygame.Color("red"), start_pos=(0, i * 64), end_pos=(640, i * 64))


            screen.blit(mole_image, mole_image.get_rect(topleft=mole))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
