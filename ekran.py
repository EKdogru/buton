import pygame
import sys
import socket
import threading

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# UDP bağlantısı için ayarlar
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

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
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
        elif self.dance_mode == 'ankara':
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y - 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x - 20, self.y - 20), (self.x - 40, self.y), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x + 20, self.y - 20), (self.x + 40, self.y), 2)
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
        elif self.dance_mode == 'floss':
            if self.dance_step % 40 < 10:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 20, self.y + 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 20, self.y + 20), 2)
            elif self.dance_step % 40 < 20:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 40, self.y + 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 40, self.y + 20), 2)
            elif self.dance_step % 40 < 30:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 60, self.y + 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 60, self.y + 20), 2)
            else:
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x - 80, self.y + 20), 2)
                pygame.draw.line(screen, (0, 0, 0), (self.x, self.y - 10), (self.x + 80, self.y + 20), 2)

        # Bacaklar
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 30), (self.x - 10, self.y + 50), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 30), (self.x + 10, self.y + 50), 2)
        if self.dance_mode:
            self.dance_step += 1

    def handle_keys(self, keys):
        if keys[self.control_keys['left']]:
            self.x -= self.vel_x
        if keys[self.control_keys['right']]:
            self.x += self.vel_x
        if not self.is_jumping:
            if keys[self.control_keys['jump']]:
                self.is_jumping = True
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

# Çöp adam listesi
stick_figures = []

# UDP dinleme ve çöp adam oluşturma fonksiyonu
def udp_listener():
    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8')
        if message == 'YeniKarekter':
            stick_figures.append(StickFigure(400, 300, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP}))
        elif message.startswith('DansModu'):
            _, dance_mode = message.split()
            for stick_figure in stick_figures:
                stick_figure.dance_mode = dance_mode
                stick_figure.dance_step = 0
        elif message == 'Stop':
            pygame.quit()
            sys.exit()

# UDP dinleme işlevini ayrı bir iş parçacığında çalıştırma
threading.Thread(target=udp_listener, daemon=True).start()

# Ana döngü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    for stick_figure in stick_figures:
        stick_figure.handle_keys(keys)

    screen.fill((255, 255, 255))
    for stick_figure in stick_figures:
        stick_figure.draw(screen)
    pygame.display.flip()
    clock.tick(30)
