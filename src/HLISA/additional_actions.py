import math
import time
import random
import logging
import numpy as np

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from HLISA.selenium_actions import HL_Selenium_Actions
from HLISA.util import (behavorial_element_coordinates,
                        get_current_scrolling_position,
                        std_positive,
                        get_scrollable_elements,
                        element_is_scrollable)

from HLISA.errors import UnscrollableElementException

class HL_Additional_Actions:
    scroll_tick_size = 57

    def __init__(self, webdriver):
        self.webdriver = webdriver


    def shortPauze(self):
        """ Function that defines a short pause between actions
        """
        time.sleep(random.random() + 0.5)


    def move_to_element_outside_viewport(self, element, addDelayAfter=True):
        """ First scrolls to get the element into the viewport, then performs the movement
        """
        viewport_height = self.webdriver.execute_script("return window.innerHeight")
        y_relative = int(element.rect['y']) - get_current_scrolling_position(self.webdriver)["y"]
        y_diff = None
        if y_relative < 0 or y_relative > viewport_height:
            y_diff = y_relative if y_relative < 0 else y_relative - viewport_height/2

        if y_diff != None:
            self.scroll_by(0, y_diff)
            if get_current_scrolling_position(self.webdriver)["y"] == 0:
                # Fall back approach, if window.scrollBy does not work
                self.scroll_by_page_element(element, 0, y_diff)

        x, y = behavorial_element_coordinates(self.webdriver, element)
        selenium_actions = HL_Selenium_Actions(self.webdriver)
        selenium_actions.move_to(x, y, addDelayAfter)
        selenium_actions.perform()

    def scroll_by_page_element(self, element, x_diff, y_diff, addDelayAfter=True):
        """ Attempts scrolling via elements on the page

            @param element: the element of interest to search for scrollable parent
            elements
        """
        start = get_current_scrolling_position(self.webdriver, element)["y"]
        scrollable_elements = get_scrollable_elements(self.webdriver, element)
        while scrollable_elements and \
                start == get_current_scrolling_position(self.webdriver, element)["y"]:
            scroll = scrollable_elements.pop()
            self.scroll_by(x_diff, y_diff, addDelayAfter, scroll)


    def scroll_by(self, x_diff, y_diff, addDelayAfter=True, element=None):
        """ This function scrolls a few pixels further if the parameter is not a multiple of a standard scroll value.
            It would be detectable otherwise.
            Keyword arguments:
            x_diff -- the horizontal distance to scroll. 0 to not scroll horizontally.
            y_diff -- the vertical distance to scroll. 0 to not scroll vertically.
            element -- the element to scroll in (if None, the page is scrolled)
        """
        if x_diff != 0:
            raise NotImplementedError("Horizontal scrolling not yet implemented")
        if element is None or element_is_scrollable(self.webdriver, element):
            self.scroll_vertical(y_diff, element)
        else:
            raise UnscrollableElementException("The element can not be scrolled")
        if addDelayAfter:
            self.shortPauze()


    def scroll_vertical(self, y_diff_original, element=None):
        y_diff = y_diff_original
        scroll_ticks = 0
        current_y = get_current_scrolling_position(self.webdriver, element)["y"]
        if y_diff > 0:            
            while y_diff > 0:
                y_diff = self.scroll_tick(self.scroll_tick_size, scroll_ticks, y_diff, element)
                scroll_ticks += 1
        else:
            min_y = 0
            y_diff = max(y_diff, min_y - current_y) # Prevent scrolling too far
            while y_diff < 0:
                y_diff = self.scroll_tick((-1 * self.scroll_tick_size), scroll_ticks, y_diff, element)
                scroll_ticks += 1
        new_y = get_current_scrolling_position(self.webdriver, element)["y"]
        scrolled_distance = abs(current_y - new_y)
        if scrolled_distance == 0: # Scrolling is impossible
            return
        if scrolled_distance < abs(y_diff_original) - self.scroll_tick_size:
            if y_diff_original >= 0:
                self.scroll_vertical(y_diff_original - scrolled_distance)
            else:
                self.scroll_vertical(y_diff_original + scrolled_distance)


    def scroll_tick(self, pixelAmount, scroll_ticks, y_diff, element=None):
        """ Scrolls one tick on the window or a given element
        """
        if element:
            self.webdriver.execute_script("arguments[0].scrollBy(0, " + str(pixelAmount) + ")", element)
        else:
            self.webdriver.execute_script("window.scrollBy(0, " + str(pixelAmount) + ")")
        y_diff -= pixelAmount
        time.sleep(0.05 + (random.random()/200))
        if scroll_ticks % 7 == 0:
            time.sleep(std_positive(0.5, 0.1, 0))
        return y_diff


    def scroll_to(self, x, y, addDelayAfter=True):
        """ This function scrolls a few pixels further if the parameter is not a multiple of a standard scroll value.
            It would be detectable otherwise.
        """
        self.shortPauze()
        current_x = get_current_scrolling_position(self.webdriver)["x"]
        if current_x != x:
            raise NotImplementedError("Horizontal scrolling not yet implemented")
        current_y = get_current_scrolling_position(self.webdriver)["y"]
        y_diff = y - current_y
        self.scroll_by(x, y_diff, addDelayAfter)
