import pygame
import random

# make a comment
def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect.collidepoint(event.pos.get_rect()) in pygame.Rect.collidepoint(mole_image.get_rect()):
                        new_pos = random.radrange()

            screen.fill("light blue")

            vert_counter = 0
            vert_start_x = 32
            vert_start_y = 0
            vert_end_x = 32
            vert_end_y = 512

            horiz_counter = 0
            horiz_start_x = 0
            horiz_start_y = 32
            horiz_end_x = 640
            horiz_end_y = 32
            vert_line = pygame.draw.line(screen, "dark blue", (vert_start_x, vert_start_y), (vert_end_x, vert_end_y))
            while vert_counter != 32:
                vert_counter += 1
                vert_start_x += 32
                vert_end_x += 32
                vert_line = pygame.draw.line(screen, "dark blue", (vert_start_x, vert_start_y), (vert_end_x,vert_end_y))
                print(vert_line)

            horiz_line = pygame.draw.line(screen, "dark blue", (horiz_start_x, horiz_start_y),
                                          (horiz_end_x, horiz_end_y))
            while horiz_counter != 32:
                horiz_counter += 1
                horiz_start_y += 32
                horiz_end_y += 32
                horiz_line = pygame.draw.line(screen, "dark blue", (horiz_start_x, horiz_start_y),
                                             (horiz_end_x, horiz_end_y))
                print(horiz_line)

            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
