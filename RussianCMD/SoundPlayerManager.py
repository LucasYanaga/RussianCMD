import pygame

def init():
    pygame.mixer.init()


def stop():
    pygame.mixer.music.stop()


def set_sound(sound):
    return pygame.mixer.Sound(sound)


