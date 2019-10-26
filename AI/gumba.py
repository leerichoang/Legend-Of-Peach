import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """Base Enemy Class, where the AI will control """
    def __init__(self, hub, x, y, direction, name, images, frame, scale):
        """Seting up values for AI"""
        super().__init__()
        # Values
        self.name = name
        self.hub = hub
        self.original_pos = [x, y]
        self.move = direction
        self.velX = self.hub.velocityAI
        self.velY = 0
        self.state = hub.WALK

        # Screen Camera
        self.screen = hub.main_screen
        self.screen_rect = self.screen.get_rect()
        self.camera = hub.camera

        # Images
        self.index = 0
        self.frameRate = frame
        self.clock = pygame.time.get_ticks() + self.frameRate
        self.image_index = images
        self.image = self.image_index[self.index]
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = self.original_pos[0]
        self.rect.y = self.original_pos[1]

        # Physics Values
        self.gravity = 9.8
        self.velocity = 0
        self.check_direction()

        # AI BOOLS
        self.kill = False

    def check_direction(self):
        if self.move == self.hub.STAND or self.hub.modeFreeze == True:
            self.velX = 0
        elif self.move == self.hub.LEFT:
            self.velX = -self.hub.velocityAI
        elif self.move == self.hub.RIGHT:
            self.velX = self.hub.velocityAI

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update the Enemy Logic"""
        # Apply gravity
        self.rect.y += self.gravity
        self.curr_state()
        self.rect.x = self.original_pos[0] - self.camera.world_offset_x
        self.check_collision()
        print(self.name + " is " + self.state)
        self.check_fell()

    def flip_direction(self):
        if self.move == self.hub.LEFT:
            self.move = self.hub.RIGHT
        else:
            self.move = self.hub.LEFT

    def check_rightedge(self):
        if self.rect.right >= self.screen_rect.right:
            return True

    def check_collision(self):
        if self.rect.left <= 0:
            self.kill = True

    def check_fell(self):
        if self.rect.top == self.screen_rect.bottom:
            self.kill = True

    def curr_state(self):
        """Enemy State Behavior"""
        if self.state == self.hub.WALK:
            self.walking()
        if self.state == self.hub.STOMPED:
            self.stomped()

    def stomped(self):
        """Placeholder for when enemy stomped"""
        pass

    def walking(self):
        # Check if hit right wall, if so move left
        if self.check_rightedge():
            self.move = self.hub.LEFT

        self.check_direction()
        # Apply movement
        # Move Right
        self.original_pos[0] += self.velX


    def death_fall(self, direction):
        """Death Jump State"""
        self.velY = -10
        self.index = 3
        self.image = self.image_index[self.index]
        self.state = self.hub.STOMPED

    def death_fall(self, direction):
        """Death falling"""
        self.rect.y += self.velY
        self.rect.x += self.velX


    def next_frame(self):
        """Frame change"""
        self.image = self.image_index[self.index]


class Gumba(Enemy):
    def __init__(self, hub, x, y):
        self.name = "goomba"
        self.frame = 60
        self.scale = (50, 50)
        self.direction = hub.RIGHT
        self.image_index = [pygame.image.load("imgs/Cut-Sprites-For-Mario/Characters/113_goomba.png")]

        super().__init__(hub=hub, x=x, y=y, direction=self.direction, name=self.name,
                         images=self.image_index, frame=self.frame, scale=self.scale)


class Paratroops(Enemy):
    def __init__(self, hub, x, y):
        self.name = "paratroop"
        self.frame = 60
        self.scale = (50, 50)
        self.direction = "LEFT"
        self.image_index = [pygame.image.load("")]

        super().__init__(hub=hub, x=x, y=y, direction=self.direction, name=self.name,
                         images=self.image_index, frame=self.frame, scale=self.scale)


class Koopatroops(Enemy):
    def __init__(self, hub, x, y):
        self.name = "koopatroop"
        self.frame = 60
        self.scale = (50, 50)
        self.direction = "LEFT"
        self.image_index = [pygame.image.load("")]

        super().__init__(hub=hub, x=x, y=y, direction=self.direction, name=self.name,
                         images=self.image_index, frame=self.frame, scale=self.scale)


class Piranhaplant(Enemy):
    def __init__(self, hub, x, y):
        self.name = "piranhaplant"
        self.frame = 60
        self.scale = (50, 50)
        self.direction = "STILL"
        self.image_index = [pygame.image.load("")]

        super().__init__(hub=hub, x=x, y=y, direction=self.direction, name=self.name,
                         images=self.image_index, frame=self.frame, scale=self.scale)