import pygame

def check_key():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("check_key")
    bg_color = (0, 255, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        screen.fill(bg_color)
        pygame.display.flip()

check_key()
