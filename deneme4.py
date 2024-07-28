import pygame
import sys
from hareketsemasi import *

pygame.init()

# Ekran boyutları
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Çöp adamı tanımlayan sınıf
class StickFigure:
    def __init__(self, x, y, control_keys):
        self.x = x
        self.y = y
        self.vel_x = 5
        self.vel_y = 10
        self.is_jumping = False
        self.jump_count = 10
        self.dance_mode = None
        self.dance_step = 0
        self.control_keys = control_keys

    def draw(self, screen):
        # Baş
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y - 20), 10)
        # Gövde
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x, self.y + 30), 2)

        # Kollar
        if self.dance_mode == 'gangnam':
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 10, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 10, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 10, self.y - 40), (self.x - 30, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 10, self.y - 40), (self.x + 30, self.y - 20), 2)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 10, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 10, self.y - 40), (self.x - 30, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 40), (self.x + 40, self.y - 20), 2)
            else:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 10, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 40), (self.x - 40, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 10, self.y - 40), (self.x + 30, self.y - 20), 2)
        elif self.dance_mode == 'ankara':
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 40, self.y - 10), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 40, self.y - 10), (self.x + 60, self.y + 10), 2)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 40, self.y - 10), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 40, self.y - 10), (self.x - 60, self.y + 10), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y + 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 40), (self.x - 40, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y + 20), (self.x + 40, self.y + 40), 2)
            else:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y + 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y + 40), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y + 40), (self.x - 40, self.y + 60), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y + 40), (self.x + 40, self.y + 60), 2)
        else:
            pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y), 2)
            pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y), 2)
            pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y), (self.x - 40, self.y + 20), 2)
            pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y), (self.x + 40, self.y + 20), 2)

        # Bacaklar
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 30), (self.x - 20, self.y + 60), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 30), (self.x + 20, self.y + 60), 2)

    def move_right(self):
        self.x += self.vel_x

    def move_left(self):
        self.x -= self.vel_x

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True

    def update_jump(self):
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

    def start_dance(self, mode):
        self.dance_mode = mode

    def stop_dance(self):
        self.dance_mode = None

    def update_dance(self):
        if self.dance_mode:
            self.dance_step += 1

    # Çöp adamları oluştur


stick_figures = [
    StickFigure(50, 50, {
        'right': pygame.K_RIGHT,
        'left': pygame.K_LEFT,
        'jump': pygame.K_UP,
        'dance1': pygame.K_1,
        'dance2': pygame.K_2,
        'stop_dance': pygame.K_3
    })
]


# Yeni çöp adam yaratma fonksiyonu
def create_stick_figure():
    positions = [(750, 50), (50, 550), (750, 550)]
    control_keys = [
        {'right': pygame.K_d, 'left': pygame.K_a, 'jump': pygame.K_w, 'dance1': pygame.K_q, 'dance2': pygame.K_e,
         'stop_dance': pygame.K_r},
        {'right': pygame.K_l, 'left': pygame.K_j, 'jump': pygame.K_i, 'dance1': pygame.K_o, 'dance2': pygame.K_p,
         'stop_dance': pygame.K_u},
        {'right': pygame.K_h, 'left': pygame.K_f, 'jump': pygame.K_t, 'dance1': pygame.K_y, 'dance2': pygame.K_u,
         'stop_dance': pygame.K_i}
    ]

    if len(stick_figures) < 4:
        new_position = positions[len(stick_figures) - 1]
        new_keys = control_keys[len(stick_figures) - 1]
        stick_figures.append(StickFigure(*new_position, new_keys))


# Ana döngü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                create_stick_figure()

    keys = pygame.key.get_pressed()

    for stick_figure in stick_figures:
        if keys[stick_figure.control_keys['right']]:
            stick_figure.move_right()
        if keys[stick_figure.control_keys['left']]:
            stick_figure.move_left()
        if keys[stick_figure.control_keys['jump']]:
            stick_figure.jump()
        if keys[stick_figure.control_keys['dance1']]:
            stick_figure.start_dance('gangnam')
        if keys[stick_figure.control_keys['dance2']]:
            stick_figure.start_dance('ankara')
        if keys[stick_figure.control_keys['stop_dance']]:
            stick_figure.stop_dance()

    for stick_figure in stick_figures:
        stick_figure.update_jump()
        stick_figure.update_dance()



    screen.fill((255, 255, 255))
    for stick_figure in stick_figures:
        stick_figure.draw(screen)
    pygame.display.flip()
    clock.tick(30)

