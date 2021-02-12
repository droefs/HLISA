import math
import time
import random
import numpy as np

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.remote.webelement import WebElement

class HL_Util:
    # (normal distribution)
    # Takes an element and returns coordinates somewhere in the element. If the element is not visable, it returns 0.
    def behavorial_element_coordinates(self, webdriver, element):
        x_relative = int(element.rect['x']) - webdriver.execute_script("return window.pageXOffset;")
        y_relative = int(element.rect['y']) - webdriver.execute_script("return window.pageYOffset;")
        counter = 0
        for i in range(10): # Try 10 random positions, as some positions are not in round buttons.
            x = x_relative + np.random.normal(int(element.rect['width']*0.5), int(element.rect['width']*0.2))
            y = y_relative + np.random.normal(int(element.rect['height']*0.5), int(element.rect['height']*0.2))
        
            coords_in_button = webdriver.execute_script("return document.elementFromPoint(" + str(x) + ", " + str(y) + ") === arguments[0];", element)

            if coords_in_button:
                return (x, y)
        return None

    def std_positive(mean, std, minimal):
        sample = np.random.normal(mean, std)
        while sample < minimal:
            sample += random.random() * (mean - minimal)
        return sample

    def create_pointer_move(self, duration=50, x=None, y=None, origin=None):
        action = dict(type="pointerMove", duration=duration)
        action["x"] = x
        action["y"] = y
        if isinstance(origin, WebElement):
            action["origin"] = {"element-6066-11e4-a52e-4f735466cecf": origin.id}
        elif origin is not None:
            action["origin"] = origin

        self.add_action(action)

    def increaseMousemovementSpeed():
        PointerInput.create_pointer_move = HL_Util.create_pointer_move

    
