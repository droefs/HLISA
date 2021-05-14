import math
import time
import random
import numpy as np

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from human_like_selenium_api.hl_util import HL_Util

class HL_Actions:
    def __init__(self, hl_action_chain, webdriver):
        self.webdriver = webdriver
        self.hl_action_chain = hl_action_chain

    #First scrolls to get the element into the viewport, then performs the movement
    def move_to_element_outside_viewport(self, element):
        viewport_height = self.webdriver.execute_script("return window.innerHeight")
        y_relative = int(element.rect['y']) - self.webdriver.execute_script("return window.pageYOffset;")
        if y_relative < 0:
            self.scroll_by(0, y_relative)
        elif y_relative > viewport_height:
            self.scroll_by(0, y_relative - viewport_height/2)
        x, y = HL_Util.behavorial_element_coordinates("", self.webdriver, element)  
        self.hl_action_chain.move_to(x, y)
        self.hl_action_chain.perform()

    # This function scrolls a few pixels further if the parameter is not a multiple of a standard scroll value.
    # It would be detectable otherwise.
    def scroll_by(self, x_diff, y_diff):
        time.sleep(random.random() + 0.5)    
        if x_diff != 0:
            logger.error("Scrolling horizontal not implemented")
        self.scroll_vertical(y_diff)

    def scroll_vertical(self, y_diff):
        scroll_ticks = 0
        current_y = self.webdriver.execute_script("return window.pageYOffset;")
        if y_diff > 0:
            max_y = self.webdriver.execute_script("return document.body.scrollHeight;")
            y_diff = min(y_diff, max_y - current_y) # Prevent scrolling too far
            while y_diff > 0:
                y_diff = self.scroll_tick(57, scroll_ticks, y_diff)
                scroll_ticks += 1
        else:
            min_y = 0
            y_diff = max(y_diff, min_y - current_y) # Prevent scrolling too far
            while y_diff < 0:
                y_diff = self.scroll_tick(-57, scroll_ticks, y_diff)
                scroll_ticks += 1

    # Scrolls one tick
    def scroll_tick(self, pixelAmount, scroll_ticks, y_diff):
        self.webdriver.execute_script("window.scrollBy(0, " + str(pixelAmount) + ")")
        y_diff -= pixelAmount
        time.sleep(0.05 + (random.random()/200))
        if scroll_ticks % 7 == 0:
            time.sleep(0.5)
        return y_diff

    # This function scrolls a few pixels further if the parameter is not a multiple of a standard scroll value.
    # It would be detectable otherwise.
    def scroll_to(self, x, y):
        time.sleep(random.random() + 0.5)   
        current_x = self.webdriver.execute_script("return window.pageXOffset;")
        if current_x != x:
            logger.error("Scrolling horizontal not yet implemented")
        current_y = self.webdriver.execute_script("return window.pageYOffset;")
        y_diff = y - current_y
        self.scroll_by(x, y_diff)
