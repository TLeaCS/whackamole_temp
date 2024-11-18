#Kalea T whackamole.py
import pygame
import random

def main():
    #Ta provided this code
    try:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
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
            #Makes vertical grid lines of 20
            for i in range(21):
                pygame.draw.line(screen, pygame.Color("blue"), (i * 32, 0), (i * 32, 512))

            #Makes horizontal grid lines of 16
            for i in range(17):
                pygame.draw.line(screen, pygame.Color("purple"), (0, i * 32), (640, i * 32))


            screen.blit(mole_image, mole_image.get_rect(topleft=mole))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
