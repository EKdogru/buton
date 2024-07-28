import pygame
import math

# Pygame'i başlat
pygame.init()

# Ekran boyutları
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Çöp Adam")

# Renkler
black = (0, 0, 0)
white = (255, 255, 255)

# Çöp adamın başlangıç konumu
x, y = width // 2, height // 2
left_upper_arm_angle = 0
left_lower_arm_angle = 0
right_upper_arm_angle = 0
right_lower_arm_angle = 0
left_upper_leg_angle = -75  # Sol üst bacak açısı
left_lower_leg_angle = -75  # Sol alt bacak açısı
right_upper_leg_angle = 75  # Sağ üst bacak açısı
right_lower_leg_angle = 75  # Sağ alt bacak açısı
angle_increment = 15
arm_length = 50
leg_length = 50

clock = pygame.time.Clock()

def draw_stick_figure(screen, x, y, left_upper_arm_angle, left_lower_arm_angle, right_upper_arm_angle, right_lower_arm_angle, left_upper_leg_angle, left_lower_leg_angle, right_upper_leg_angle, right_lower_leg_angle):
    # Vücut
    pygame.draw.line(screen, black, (x, y - 50), (x, y + 50), 2)  # Vücut
    pygame.draw.circle(screen, black, (x, y - 70), 20, 2)  # Kafa

    # Sol Kol
    left_shoulder_x, left_shoulder_y = x, y - 30
    left_elbow_x = left_shoulder_x + arm_length * math.cos(math.radians(left_upper_arm_angle - 180))
    left_elbow_y = left_shoulder_y + arm_length * math.sin(math.radians(left_upper_arm_angle - 180))
    left_hand_x = left_elbow_x + arm_length * math.cos(math.radians(left_lower_arm_angle - 180))
    left_hand_y = left_elbow_y + arm_length * math.sin(math.radians(left_lower_arm_angle - 180))

    pygame.draw.line(screen, black, (left_shoulder_x, left_shoulder_y), (left_elbow_x, left_elbow_y), 2)  # Üst kol
    pygame.draw.line(screen, black, (left_elbow_x, left_elbow_y), (left_hand_x, left_hand_y), 2)  # Alt kol

    # Sağ Kol
    right_shoulder_x, right_shoulder_y = x, y - 30
    right_elbow_x = right_shoulder_x + arm_length * math.cos(math.radians(right_upper_arm_angle))
    right_elbow_y = right_shoulder_y + arm_length * math.sin(math.radians(right_upper_arm_angle))
    right_hand_x = right_elbow_x + arm_length * math.cos(math.radians(right_lower_arm_angle))
    right_hand_y = right_elbow_y + arm_length * math.sin(math.radians(right_lower_arm_angle))

    pygame.draw.line(screen, black, (right_shoulder_x, right_shoulder_y), (right_elbow_x, right_elbow_y), 2)  # Üst kol
    pygame.draw.line(screen, black, (right_elbow_x, right_elbow_y), (right_hand_x, right_hand_y), 2)  # Alt kol

    # Sol Bacak
    left_hip_x, left_hip_y = x, y + 50
    left_knee_x = left_hip_x + leg_length * math.cos(math.radians(left_upper_leg_angle - 180))
    left_knee_y = left_hip_y + leg_length * math.sin(math.radians(left_upper_leg_angle - 180))
    left_foot_x = left_knee_x + leg_length * math.cos(math.radians(left_lower_leg_angle - 180))
    left_foot_y = left_knee_y + leg_length * math.sin(math.radians(left_lower_leg_angle - 180))

    pygame.draw.line(screen, black, (left_hip_x, left_hip_y), (left_knee_x, left_knee_y), 2)  # Üst bacak
    pygame.draw.line(screen, black, (left_knee_x, left_knee_y), (left_foot_x, left_foot_y), 2)  # Alt bacak

    # Sağ Bacak
    right_hip_x, right_hip_y = x, y + 50
    right_knee_x = right_hip_x + leg_length * math.cos(math.radians(right_upper_leg_angle))
    right_knee_y = right_hip_y + leg_length * math.sin(math.radians(right_upper_leg_angle))
    right_foot_x = right_knee_x + leg_length * math.cos(math.radians(right_lower_leg_angle))
    right_foot_y = right_knee_y + leg_length * math.sin(math.radians(right_lower_leg_angle))

    pygame.draw.line(screen, black, (right_hip_x, right_hip_y), (right_knee_x, right_knee_y), 2)  # Üst bacak
    pygame.draw.line(screen, black, (right_knee_x, right_knee_y), (right_foot_x, right_foot_y), 2)  # Alt bacak

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_upper_arm_angle = min(left_upper_arm_angle + angle_increment, 90)
            elif event.key == pygame.K_s:
                left_upper_arm_angle = max(left_upper_arm_angle - angle_increment, -90)
            elif event.key == pygame.K_d:
                left_lower_arm_angle = min(left_lower_arm_angle + angle_increment, 90)
            elif event.key == pygame.K_a:
                left_lower_arm_angle = max(left_lower_arm_angle - angle_increment, -90)
            elif event.key == pygame.K_k:
                right_upper_arm_angle = min(right_upper_arm_angle + angle_increment, 90)
            elif event.key == pygame.K_i:
                right_upper_arm_angle = max(right_upper_arm_angle - angle_increment, -90)
            elif event.key == pygame.K_l:
                right_lower_arm_angle = min(right_lower_arm_angle + angle_increment, 90)
            elif event.key == pygame.K_j:
                right_lower_arm_angle = max(right_lower_arm_angle - angle_increment, -90)
            elif event.key == pygame.K_UP:
                left_upper_leg_angle = min(left_upper_leg_angle + angle_increment, 90)
            elif event.key == pygame.K_DOWN:
                left_upper_leg_angle = max(left_upper_leg_angle - angle_increment, -90)
            elif event.key == pygame.K_LEFT:
                left_lower_leg_angle = min(left_lower_leg_angle + angle_increment, 90)
            elif event.key == pygame.K_RIGHT:
                left_lower_leg_angle = max(left_lower_leg_angle - angle_increment, -90)
            elif event.key == pygame.K_KP8:
                right_upper_leg_angle = min(right_upper_leg_angle + angle_increment, 90)
            elif event.key == pygame.K_KP2:
                right_upper_leg_angle = max(right_upper_leg_angle - angle_increment, -90)
            elif event.key == pygame.K_KP4:
                right_lower_leg_angle = min(right_lower_leg_angle + angle_increment, 90)
            elif event.key == pygame.K_KP6:
                right_lower_leg_angle = max(right_lower_leg_angle - angle_increment, -90)




    screen.fill(white)
    draw_stick_figure(screen, x, y, left_upper_arm_angle, left_lower_arm_angle, right_upper_arm_angle, right_lower_arm_angle, left_upper_leg_angle, left_lower_leg_angle, right_upper_leg_angle, right_lower_leg_angle)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
