import math
import time
import random
import numpy as np
import inspect
import logging

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException

from HLISA.util import (behavorial_element_coordinates,
                        get_current_scrolling_position,
                        increaseMousemovementSpeed,
                        std_positive,
                        get_cursor_coordinates,
                        scale_delay_kwargs)
from HLISA.errors import (HLISAException,
                          OutOfViewportException)
from HLISA.constants import (ACTION_DELAY_KWARGS,
                             CLICK_HOLD_DELAY_KWARGS,
                             SENTENCE_CLOSING_DELAY_KWARGS,
                             SENTENCE_COMPLETION_DELAY_KWARGS,
                             KEY_DOWN_DELAY_KWARGS,
                             KEY_UP_DELAY_KWARGS,
                             SENTENCE_OPENING_DELAY_KWARGS,
                             SENTENCE_CHARACTER_DELAY_KWARGS,
                             WORD_OPENING_DELAY_KWARGS,
                             WORD_CHARACTER_DELAY_KWARGS,
                             WORD_CLOSING_DELAY_KWARGS,
                             CHARACTER_SHIFT_DOWN_DELAY_KWARGS,
                             CHARACTER_SHIFT_UP_DELAY_KWARGS,
                             CHARACTER_DWELL_DELAY_KWARGS,
                             DOUBLE_CLICK_SECOND_HOLD_DELAY_KWARGS,
                             DOUBLE_CLICK_BETWEEN_DELAY_KWARGS,
                             DOUBLE_CLICK_SECOND_HOLD_DELAY_KWARGS)

class HL_Selenium_Actions:

    selenium_version = -1 # -1: unknown; 3: selenium < 4; 4: selenium >= 4
    
    def __init__(self, webdriver):
        self.webdriver = webdriver
        # Determine whether monkey patching is still necessary (starting from Selenium 4 its not necessary anymore):
        # (Selenium 4 introduced an optional third argument to the constructor of ActionChains to specify mouse
        # movement speed, so if there are less than 3 arguments, monkeypatch, otherwise use the new feature).
        if len(inspect.getfullargspec(ActionChains.__init__)[0]) < 3:
            HL_Selenium_Actions.selenium_version = 3
            self.actions = ActionChains(webdriver)
            increaseMousemovementSpeed()
        else:
            HL_Selenium_Actions.selenium_version = 4
            self.actions = ActionChains(webdriver, 50)

    def addDelayAfterAction(self):
        self.actions.pause(std_positive(**ACTION_DELAY_KWARGS))

    ##### Action chain methods #####

    # Clicks an element.
    # Args:	
    #   on_element: The element to click. If None, clicks on current mouse position.
    def click(self, element=None, addDelayAfter=True):
        if element is not None:
            self.move_to_element(element)
        self.actions.click_and_hold()
        # self.actions.pause(np.random.normal(0.092, 0.018))
        self.actions.pause(std_positive(**CLICK_HOLD_DELAY_KWARGS))
        self.actions.release()
        if addDelayAfter:
            self.addDelayAfterAction()
        return self

    def move_by_offset(self, x, y, addDelayAfter=True):
        current_x, current_y = get_cursor_coordinates(self.webdriver)
        self.move_to(current_x + x, current_y + y, addDelayAfter)
        return self

    def move_to_element(self, element, addDelayAfter=True):
        viewport_height = self.webdriver.execute_script("return window.innerHeight")
        viewport_width = self.webdriver.execute_script("return window.innerWidth")
        y_relative = int(element.rect['y']) - get_current_scrolling_position(self.webdriver)["y"]
        x_relative = int(element.rect['x']) - get_current_scrolling_position(self.webdriver)["x"]
        if y_relative < 0 or x_relative < 0 or y_relative > viewport_height or x_relative > viewport_width:
            error_msg = "Moving to the element is not possible. The given element is outside of the viewport"
            raise OutOfViewportException(error_msg)
        coordinates = behavorial_element_coordinates(self.webdriver, element)
        if coordinates:
            x, y = coordinates
            self.move_to(x, y, addDelayAfter)
        else:
            error_msg = "The element could not be moved to. This is likely an error in HLISA,\
                please raise an issue if it happens"
            raise HLISAException(error_msg)
        return self

    def perform(self):
        self.actions.perform()
        self.actions = ActionChains(self.webdriver)
        return self

    def pause(self, seconds):
        self.actions.pause(seconds)
        return self

    def send_keys(self, keys_to_send, element=None, addDelayAfter=True, speed_scaling=1.0):
        if element is not None:
            self.click(element)
        sentences = keys_to_send.split(". ")
        for i in range(len(sentences)-1):
            self.write_sentence(sentences[i], speed_scaling=speed_scaling)
            self.actions.pause(
                std_positive(**scale_delay_kwargs(speed_scaling, SENTENCE_CLOSING_DELAY_KWARGS))
            ) # Closing a sentence
            self.write_character(".") # Add the removed dot and space again
            self.actions.pause(
                std_positive(**scale_delay_kwargs(speed_scaling, SENTENCE_COMPLETION_DELAY_KWARGS))
            ) # After closing a sentence
            self.write_character(" ")
        self.write_sentence(sentences[len(sentences)-1], speed_scaling=speed_scaling)
        if addDelayAfter:
            self.addDelayAfterAction()
        return self

    def click_and_hold(self, on_element=None, addDelayAfter=True):
        if on_element is not None:
            self.move_to_element(on_element)
        self.actions.click_and_hold()
        if addDelayAfter:
            self.addDelayAfterAction()
        return self

    def double_click(self, element=None, addDelayAfter=True):
        if element is not None:
            self.move_to_element(element)
        self.actions.click_and_hold()
        self.actions.pause(np.random.normal(**DOUBLE_CLICK_SECOND_HOLD_DELAY_KWARGS))
        self.actions.release()
        self.actions.pause(np.random.normal(**DOUBLE_CLICK_BETWEEN_DELAY_KWARGS))
        self.actions.click_and_hold()
        self.actions.pause(np.random.normal(**DOUBLE_CLICK_SECOND_HOLD_DELAY_KWARGS))
        self.actions.release()
        if addDelayAfter:
            self.addDelayAfterAction()
        return self
        
    def drag_and_drop(self, source, target, addDelayAfter=True):
        self.move_to_element(source)
        self.actions.drag_and_drop(source, target)
        if addDelayAfter:
            self.addDelayAfterAction()
        return self

    def drag_and_drop_by_offset(self, source, xoffset, yoffset, addDelayAfter=True):
        self.move_to_element(source)
        self.actions.drag_and_drop_by_offset(source, xoffset, yoffset)
        if addDelayAfter:
            self.addDelayAfterAction()
        return self

    def key_down(self, value, element=None, addDelayAfter=True):
        if element is not None:
            self.click(element)
        self.actions.key_down(value)
        if addDelayAfter:
            self.actions.pause(std_positive(**KEY_DOWN_DELAY_KWARGS))
        return self

    def key_up(self, value, element=None, addDelayAfter=True):
        if element is not None:
            self.click(element)
        self.actions.key_up(value)
        if addDelayAfter:
            self.actions.pause(std_positive(**KEY_UP_DELAY_KWARGS))
        return self

    def move_to_element_with_offset(self, to_element, xoffset, yoffset, addDelayAfter=True):
        left_relative = to_element.rect['x'] - get_current_scrolling_position(self.webdriver)["x"]
        top_relative = to_element.rect['y'] - get_current_scrolling_position(self.webdriver)["y"]
        self.move_to(left_relative + xoffset, top_relative + yoffset, addDelayAfter)
        return self

    def release(self, on_element=None, addDelayAfter=True):
        if on_element is not None:
            self.move_to_element(on_element)
        self.actions.release()
        if addDelayAfter:
            self.addDelayAfterAction()
        return self

    def send_keys_to_element(self, element, keys_to_send, addDelayAfter=True, speed_scaling=1.0):
        self.send_keys(keys_to_send, element, addDelayAfter, speed_scaling=speed_scaling)
        return self

    def reset_actions():
        raise NotImplementedError("This functionality is not yet implemented")

    def context_click(self, on_element=None, addDelayAfter=True):
        if on_element is not None:
            self.move_to_element(on_element)
        self.actions.context_click()
        if addDelayAfter:
            self.addDelayAfterAction()
        return self
    
    ##### Non-Selenium action chain methods #####

    # Moves to a position in the viewport
    # Args:
    #   x: x-coordinate to move to
    #   y: y-coordinate to move to
    def move_to(self, x, y, addDelayAfter=True):
        t_cursor = TheoreticalCursor(x, y, self.webdriver, self.actions)
        if addDelayAfter:
            self.addDelayAfterAction()
        return self

    ##### Util functions #####

    def write_sentence(self, sentence, speed_scaling=1.0):
        self.actions.pause(
            std_positive(**scale_delay_kwargs(speed_scaling, SENTENCE_OPENING_DELAY_KWARGS))
        ) # Opening a sentence
        words = sentence.split(" ")
        if len(words) > 0:
            for i in range(len(words)-1):
                self.write_word(words[i], speed_scaling=speed_scaling)
                self.actions.pause(
                    std_positive(**scale_delay_kwargs(speed_scaling, SENTENCE_CHARACTER_DELAY_KWARGS))
                ) # Pauze between characters (within a word)
                self.write_character(" ")
            self.write_word(words[-1], speed_scaling=speed_scaling)

    def write_word(self, word, speed_scaling=1.0):
        self.actions.pause(
            std_positive(**scale_delay_kwargs(speed_scaling, WORD_OPENING_DELAY_KWARGS))
        ) # Opening a word
        characters = list(word)
        if len(characters) > 0:
            for i in range(len(characters)-1):
                self.write_character(characters[i])
                self.actions.pause(
                    std_positive(**scale_delay_kwargs(speed_scaling, WORD_CHARACTER_DELAY_KWARGS))
                ) # Pauze between characters (within a word)
            self.write_character(characters[-1])
        self.actions.pause(
            std_positive(**scale_delay_kwargs(speed_scaling, WORD_CLOSING_DELAY_KWARGS))
        ) # Closing a word

    def write_character(self, character):
        special_characters = "!@#$%^&*()_+{}|:<>?"
        if character.isupper() or character in special_characters:
            self.actions.key_down("\ue008")
            self.actions.pause(std_positive(**CHARACTER_SHIFT_DOWN_DELAY_KWARGS)) # Time after shift press
        self.actions.key_down(character)
        self.actions.pause(std_positive(**CHARACTER_DWELL_DELAY_KWARGS)) # Dwell time
        self.actions.key_up(character)
        if character.isupper() or character in special_characters:
            self.actions.pause(std_positive(**CHARACTER_SHIFT_UP_DELAY_KWARGS)) # Time before shift release
            self.actions.key_up("\ue008")

class TheoreticalCursor():

    def roundNumber(self, number):
        if number % 1 != 0:
            logging.warning("please provide integers as coordinates in move_to functions to prevent unexpected behavior.")
            return int(number)
        else:
            return number

    def __init__(self, x, y, webdriver, actions):
        x = self.roundNumber(x)
        y = self.roundNumber(y)
        
        windowWidth = webdriver.execute_script("return window.innerWidth;")
        windowHeight = webdriver.execute_script("return window.innerHeight;")
        if (x > windowWidth or y > windowHeight or x < 0 or y < 0):
            raise MoveTargetOutOfBoundsException("(HLISA) (" + str(x) + ", " + str(y) + ") is out of bounds of viewport width (" + str(windowWidth) + ") and height (" + str(windowHeight) + ")")
        
        self.init_variables(webdriver)
        minimalDiff = self.calculatePointsAndDistances(x, y)

        self.sample_points = self.sample_points(minimalDiff)
        self.actions = actions

        for i in range(minimalDiff):
            self.calculate_point(minimalDiff, i, x, y, webdriver)

    def init_variables(self, webdriver):
        x_start, y_start = get_cursor_coordinates(webdriver)
        self.x_pos = x_start
        self.y_pos = y_start
        self.startPosX = self.x_pos # The point where the movement started
        self.startPosY = self.y_pos
        self.previousX = self.x_pos # Previous position of the cursor
        self.previousY = self.y_pos
        self.xMismatch = 0 # How far the cursor is from the real curve
        self.yMismatch = 0
        self.roundingErrorX = 0 # The cursor can only be moved in integers. This keeps track of the rounding error
        self.roundingErrorY = 0
        self.ranSumX = 0 # The sum of random movements that are theoretically performed
        self.ranSumY = 0

    def calculatePointsAndDistances(self, x, y):
        xDiffTotal = x - self.x_pos
        yDiffTotal = y - self.y_pos

        # Caluculate the third point for the Bezier curve
        self.viaX = xDiffTotal * 0.82
        self.viaY = yDiffTotal * 0.5

        # Calculate the minimal distance in pixels for a straight line
        return math.ceil(math.sqrt(xDiffTotal * xDiffTotal + yDiffTotal * yDiffTotal))

    def calculate_point(self, minimalDiff, i, x, y, webdriver):
        t = i / minimalDiff # the percentage of how far in the Bezier curve the point is
        if i == (minimalDiff - 1):
            t = 1 # Set the percentage to 1 at the end
        minT = 1 - t
        
        # Add random imperfections to the line
        self.add_imperfections()
        
        # Bezier curve inspired curve coordinate calculation. 
        currentX = minT * (minT * self.startPosX + t * (self.viaX + self.startPosX)) + t * (minT * (self.viaX + self.startPosX) + t * (x)) # Current position of the cursor
        currentY = minT * (minT * self.startPosY + t * (self.viaY + self.startPosY)) + t * (minT * (self.viaY + self.startPosY) + t * (y))
        if i in self.sample_points or t == 1:
            self.sample_point(t, minimalDiff, currentX, currentY, webdriver)

    def sample_point(self, t, minimalDiff, currentX, currentY, webdriver):
        # Keep track of how far the cursor is of the true curve and calculate a compensation. The compensation should let the line end in the correct position in the end.    
        xMismatchCompensation, yMismatchCompensation = self.compensate_mismatch(t, minimalDiff)
        
        # Compute how much the cursor should be moved
        moveX, moveY = self.compute_move_amount(currentX, currentY, xMismatchCompensation, yMismatchCompensation)

        # Check if the move is within the viewport, if it is then actually move the cursor (this is realistic, as no mouse events are sends if the cursor is outside the viewport for a real user)
        viewportWidth = webdriver.execute_script("return window.innerWidth")
        viewportHeight = webdriver.execute_script("return window.innerHeight")
        if self.x_pos + moveX < viewportWidth and self.x_pos + moveX >= 0 and self.y_pos + moveY < viewportHeight and self.y_pos + moveY >= 0:
            self.move_real_cursor(moveX, moveY, currentX, currentY)
            self.xMismatch += xMismatchCompensation
            self.yMismatch += yMismatchCompensation
 

    def add_imperfections(self):
        ranX = round(np.random.normal(0, 0.6))
        ranY = round(np.random.normal(0, 0.6))
        self.ranSumX += ranX
        self.ranSumY += ranY
        self.xMismatch += ranX
        self.yMismatch += ranY

    def compute_move_amount(self, currentX, currentY, xMismatchCompensation, yMismatchCompensation):
        moveX = ((currentX - self.previousX) + self.ranSumX) + xMismatchCompensation # How far the cursor is moved in an iteration
        moveY = ((currentY - self.previousY) + self.ranSumY) + yMismatchCompensation
         
        moveX -= round(self.roundingErrorX) # To compensate for the fact that the cursor can only be moved whole pixels
        moveY -= round(self.roundingErrorY)
        return moveX, moveY

    def compensate_mismatch(self, t, minimalDiff):
        xMismatchCompensation = round(self.xMismatch / ((1 - t) * minimalDiff**(0.5) + 1)) * -1
        yMismatchCompensation = round(self.yMismatch / ((1 - t) * minimalDiff**(0.5) + 1)) * -1
        return xMismatchCompensation, yMismatchCompensation

    def move_real_cursor(self, moveX, moveY, currentX, currentY):
        self.actions.move_by_offset(round(moveX), round(moveY))
        self.roundingErrorX -= round(self.roundingErrorX)
        self.roundingErrorY -= round(self.roundingErrorY)
        self.roundingErrorX += round(moveX) - moveX
        self.roundingErrorY += round(moveY) - moveY
        self.previousX = currentX
        self.previousY = currentY
        self.ranSumX = 0
        self.ranSumY = 0
        self.x_pos += round(moveX)
        self.y_pos += round(moveY)


    # Samples points to which the cusor will move
    def sample_points(self, minimalDiff):
        sample_points = []
        counter = 10
        newCounterValue = counter
        for i in range(1, minimalDiff):
            if counter == 0:
                sample_points.append(i/minimalDiff)
                if i/minimalDiff <= 0.7:
                    newCounterValue *= 1.05 # Accelerate
                else:
                    newCounterValue /= 1.10 # Decelerate
                counter = round(newCounterValue)
            counter -= 1
        sample_points = [round(j * minimalDiff) for j in sample_points]
        return sample_points
