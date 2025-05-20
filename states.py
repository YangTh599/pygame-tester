import pygame
import sys

pygame.init()
pygame.font.init()

class StateManager:

    def __init__(self, window, current_state):
        self.window = window
        self.current_state = current_state

    def get_state(self):
        return self.current_state
    
    def set_state(self, new_state):
        self.current_state = new_state

class State:

    def __init__(self, window, scene_manager):
        self.window = window
        self.scene_manager = scene_manager


    def run(self):
        raise NotImplementedError("run() needs to be implemented")
    
    def update(self):
        raise NotImplementedError("update() needs to be implemented")
    
    def draw(self):
        raise NotImplementedError("draw() needs to be implemented")

    
class MainMenu(State):

    def __init__(self, window, scene_manager):
        super().__init__(window, scene_manager)

    def run(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
