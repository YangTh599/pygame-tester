import pygame
import sys
from colors import *

import states as st
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes

class Menu(st.State):

    def __init__(self, window, state_mng):

        super().__init__(window, state_mng)

        text