"""
Progama desenvolvido por José Isac
20 de julho, 8:32 Pm

Este progama vai tocar uma música com o auxílio da biblioteca pygames.
O segundo exercício desse curso que eu tive dificuldades pois não sabia qual biblioteca utilizar.

Não funciona;
"""

import pygame

pygame.init()
pygame.mixer.music.load('taik.mp3')
pygame.mixer.music.play()
pygame.event.wait()
