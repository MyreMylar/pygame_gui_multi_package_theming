import pygame
import pygame_gui

pygame.init()


pygame.display.set_caption('Multi-package Theming Test')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
clock = pygame.time.Clock()

# Change 'package_one' to 'package_two'
manager = pygame_gui.UIManager((800, 600),
                               pygame_gui.PackageResource('package_two', 'theme.json'))

button_row_width = 200
button_row_height = 150
spacing = 50
num_buttons = 1
for i in range(1, 4):
    position = (i * spacing + ((i - 1) * button_row_width), spacing)
    pygame_gui.elements.UIButton(relative_rect=pygame.Rect(position,
                                                           (button_row_width,
                                                            button_row_height)),
                                 text=str(num_buttons),
                                 manager=manager,
                                 object_id='#'+str(num_buttons))
    num_buttons += 1

is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
