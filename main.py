from World import World
import pygame

world = World()
world.drawWorld()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or \
                    event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                world.takeTurn(event)
            elif event.key == pygame.K_s:
                world.save('save_file')
                print("Game state saved")
            elif event.key == pygame.K_l:
                world.load('save_file')
                print("Game state loaded")
                world.drawWorld()

