import pygame

def pygame_setup(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        s = "sound"
        self.food_sound = pygame.mixer.Sound(os.path.join('food.ogg'))
        self.defeat_sound = pygame.mixer.Sound(os.path.join('defeat.ogg'))
        music = pygame.mixer.music.load(os.path.join('music.ogg'))
        pygame.mixer.music.play(-1)


