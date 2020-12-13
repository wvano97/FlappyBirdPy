import pygame

class Tower:
    # Need to initialized outside play area and move left
    def __init__(self, surface, clock, height, X, Y,  color):
        self.Surface = surface
        self.Clock = clock
        self.Width  = 100
        self.Height = height
        self.X = X
        self.Y = Y
        self.Color = color
        self.mspeed = 5 
    
    def draw(self):
        pygame.draw.rect(self.Surface, self.Color, (self.X, self.Y, self.Width, self.Height))

    def update(self):
        self.X -= self.mspeed
    
    def __str__(self):
        return f'(X: {self.Y} Y: {self.Y}'
