import pygame.mixer, os

pygame.mixer.init()
s = "sound"
food_sound = pygame.mixer.Sound(os.path.join('sounds/food.ogg'))
defeat_sound = pygame.mixer.Sound(os.path.join('sounds/defeat.ogg'))
music = pygame.mixer.music.load(os.path.join('sounds/music.ogg'))       
food_sound_ptr = food_sound
defeat_sound_ptr = defeat_sound



