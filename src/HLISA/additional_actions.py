import math
import time
import random
import logging
import numpy as np

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from HLISA.util import HL_Util
from HLISA.selenium_actions import HL_Selenium_Actions

class HL_Additional_Actions:
    scroll_tick_size = 57

    def __init__(self, webdriver):
        self.webdriver = webdriver

    # Function that defines a short pause between actions
    def shortPauze(self):
        time.sleep(random.random() + 0.5)

    # First scrolls to get the element into the viewport, then performs the movement
    def move_to_element_outside_viewport(self, element, addDelayAfter=True):
        viewport_height = self.webdriver.execute_script("return window.innerHeight")
        y_relative = int(element.rect['y']) - self.webdriver.execute_script("return window.pageYOffset;")
        if y_relative < 0:
            self.scroll_by(0, y_relative)
        elif y_relative > viewport_height:
            self.scroll_by(0, y_relative - viewport_height/2)
        x, y = HL_Util.behavorial_element_coordinates("", self.webdriver, element)
        selenium_actions = HL_Selenium_Actions(self.webdriver)
        selenium_actions.move_to(x, y, addDelayAfter)
        selenium_actions.perform()

    # This function scrolls a few pixels further if the parameter is not a multiple of a standard scroll value.
    # It would be detectable otherwise.
    def scroll_by(self, x_diff, y_diff, addDelayAfter=True):    
        if x_diff != 0:
            logging.critical("Scrolling horizontal not implemented")
        self.scroll_vertical(y_diff)
        if addDelayAfter:
            self.shortPauze()

    def scroll_vertical(self, y_diff):
        scroll_ticks = 0
        current_y = self.webdriver.execute_script("return window.pageYOffset;")
        if y_diff > 0:
            max_y = self.webdriver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
            y_diff = min(y_diff, max_y - current_y) # Prevent scrolling too far
            while y_diff > 0:
                y_diff = self.scroll_tick(self.scroll_tick_size, scroll_ticks, y_diff)
                scroll_ticks += 1
        else:
            min_y = 0
            y_diff = max(y_diff, min_y - current_y) # Prevent scrolling too far
            while y_diff < 0:
                y_diff = self.scroll_tick((-1 * self.scroll_tick_size), scroll_ticks, y_diff)
                scroll_ticks += 1
        new_y = self.webdriver.execute_script("return window.pageYOffset;")
        scrolled_distance = abs(current_y - new_y)
        if scrolled_distance <= abs(y_diff) - self.scroll_tick_size:
            if y_diff >= 0:
                self.scroll_vertical(y_diff - scrolled_distance)
            else:
                self.scroll_vertical(y_diff + scrolled_distance)

    # Scrolls one tick
    def scroll_tick(self, pixelAmount, scroll_ticks, y_diff):
        self.webdriver.execute_script("window.scrollBy(0, " + str(pixelAmount) + ")")
        y_diff -= pixelAmount
        time.sleep(0.05 + (random.random()/200))
        if scroll_ticks % 7 == 0:
            time.sleep(HL_Util.std_positive(0.5, 0.1, 0))
        return y_diff

    # This function scrolls a few pixels further if the parameter is not a multiple of a standard scroll value.
    # It would be detectable otherwise.
    def scroll_to(self, x, y, addDelayAfter=True):
        self.shortPauze()  
        current_x = self.webdriver.execute_script("return window.pageXOffset;")
        if current_x != x:
            logger.error("Scrolling horizontal not yet implemented")
        current_y = self.webdriver.execute_script("return window.pageYOffset;")
        y_diff = y - current_y
        self.scroll_by(x, y_diff, addDelayAfter)
