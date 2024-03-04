import pygame
import math

def getRotatedImage(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    new_rect = new_image.get_rect(center=rect.center)
    return new_image, new_rect


def angleBetweenPoints(x1, y1, x2, y2):
    x_diffrence = x2 - x1
    y_diffrence = y2 - y1
    angle = math.degrees(math.atan2(-y_diffrence,  x_diffrence))
    return angle
