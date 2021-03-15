import math
import time
import random
import numpy as np

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from human_like_selenium_api.hl_util import HL_Util

class HL_ActionChains:
    
    def __init__(self, webdriver):
        self.x_pos = 0
        self.y_pos = 0
        self.webdriver = webdriver
        self.actions = ActionChains(webdriver)
        HL_Util.increaseMousemovementSpeed()

    ##### Action chain methods #####

    # Clicks an element.
    # Args:	
    #   on_element: The element to click. If None, clicks on current mouse position.
    def click(self, element=None):
        if element is not None:
            self.move_to_element(element)
        self.actions.click_and_hold()
        self.actions.pause(np.random.normal(0.092, 0.018))
        self.actions.release()
        return self

    # Moves to a position in the viewport
    # Args:
    #   x: x-coordinate to move to
    #   y: y-coordinate to move to
    def move_to(self, x, y):
        t_cursor = TheoreticalCursor(self.x_pos, self.y_pos, x, y, self.webdriver, self.actions)
        self.x_pos = t_cursor.x_pos
        self.y_pos = t_cursor.y_pos
        return self

    def move_by_offset(self, x, y):
        self.move_to(self.x_pos + x, self.y_pos + y)
        return self

    def move_to_element(self, element):
        viewport_height = self.webdriver.execute_script("return window.innerHeight")
        y_relative = int(element.rect['y']) - self.webdriver.execute_script("return window.pageYOffset;")
        if y_relative < 0:
            print("not possible, out of viewport")
        elif y_relative > viewport_height:
            print("not possible, out of viewport")
        x, y = HL_Util.behavorial_element_coordinates("", self.webdriver, element)
        self.move_to(x, y)
        return self

    def perform(self):
        self.actions.perform()
        self.actions = ActionChains(self.webdriver)
        return self

    def pause(self, seconds):
        self.actions.pause(seconds)
        return self

    def send_keys(self, keys_to_send):
        sentences = keys_to_send.split(". ")
        for i in range(len(sentences)-1):
            self.write_sentence(sentences[i])
            self.actions.pause(HL_Util.std_positive(1.7, 0.7, 0.3)) # Closing a sentence
            self.write_character(".") # Add the removed dot and space again
            self.actions.pause(HL_Util.std_positive(0.6, 0.4, 0.05)) # After closing a sentence
            self.write_character(" ")
        self.write_sentence(sentences[len(sentences)-1])

    def click_and_hold(self, on_element=None):
        raise NotImplementedError("This functionality is not yet implemented")

    def double_click(self, on_element=None):
        raise NotImplementedError("This functionality is not yet implemented")
        
    def drag_and_drop(self, source, target):
        raise NotImplementedError("This functionality is not yet implemented")

    def drag_and_drop_by_offset(self, source, xoffset, yoffset):
        raise NotImplementedError("This functionality is not yet implemented")

    def key_down(self, value, element=None):
        raise NotImplementedError("This functionality is not yet implemented")

    def key_up(self, value, element=None):
        raise NotImplementedError("This functionality is not yet implemented")

    def move_to_element_with_offset(self, to_element, xoffset, yoffset):
        raise NotImplementedError("This functionality is not yet implemented")

    def release(self, on_element=None):
        raise NotImplementedError("This functionality is not yet implemented")

    def send_keys_to_element(self, element, keys_to_send):
        raise NotImplementedError("This functionality is not yet implemented")

    def reset_actions():
        raise NotImplementedError("This functionality is not yet implemented")

    def context_click(on_element=None):
        raise NotImplementedError("This functionality is not yet implemented")
    
    ##### Util functions #####

    def write_sentence(self, sentence):
        self.actions.pause(HL_Util.std_positive(1.3, 1, 0.2)) # Opening a sentence
        words = sentence.split(" ")
        if len(words) > 0:
            for i in range(len(words)-1):
                self.write_word(words[i])
                self.actions.pause(HL_Util.std_positive(0.21, 0.03, 0.011)) # Pauze between characters (within a word)
                self.write_character(" ")
            self.write_word(words[-1])

    def write_word(self, word):
        self.actions.pause(HL_Util.std_positive(0.47, 0.21, 0.05)) # Opening a word
        characters = list(word)
        if len(characters) > 0:
            for i in range(len(characters)-1):
                self.write_character(characters[i])
                self.actions.pause(HL_Util.std_positive(0.21, 0.03, 0.011)) # Pauze between characters (within a word)
            self.write_character(characters[-1])
        self.actions.pause(HL_Util.std_positive(0.2, 0.08, 0.01)) # Closing a word

    def write_character(self, character):
        self.actions.key_down(character)
        self.actions.pause(HL_Util.std_positive(0.06, 0.035, 0.013)) # Dwell time
        self.actions.key_up(character)

class TheoreticalCursor():

    def __init__(self, x_start, y_start, x, y, webdriver, actions):
        self.init_variables(x_start, y_start)        
        minimalDiff = self.calculatePointsAndDistances(x, y)

        self.sample_points = self.sample_points(minimalDiff)
        self.actions = actions

        for i in range(minimalDiff):
            self.calculate_point(minimalDiff, i, x, y, webdriver)

    def init_variables(self, x_start, y_start):
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
 

    def add_imperfections(self):
        ranX = round(np.random.normal(0, 0.6))
        ranY = round(np.random.normal(0, 0.6))
        self.ranSumX += ranX
        self.ranSumY += ranY

    def compute_move_amount(self, currentX, currentY, xMismatchCompensation, yMismatchCompensation):
        moveX = currentX - self.previousX + self.ranSumX + xMismatchCompensation # How far the cursor is moved in an iteration
        moveY = currentY - self.previousY + self.ranSumY + yMismatchCompensation
        if round(self.roundingErrorX) != 0 or round(self.roundingErrorY) != 0: # To compensate for the fact that the cursor can only be moved whole pixels
            moveX -= round(self.roundingErrorX)
            self.roundingErrorX -= round(self.roundingErrorX)
            moveY -= round(self.roundingErrorY)
            self.roundingErrorY -= round(self.roundingErrorY)
        return moveX, moveY

    def compensate_mismatch(self, t, minimalDiff):
        self.xMismatch += self.ranSumX
        self.yMismatch += self.ranSumY
        xMismatchCompensation = round(self.xMismatch / ((1 - t) * minimalDiff**(0.5) + 1)) * -1
        yMismatchCompensation = round(self.yMismatch / ((1 - t) * minimalDiff**(0.5) + 1)) * -1
        self.xMismatch += xMismatchCompensation
        self.yMismatch += yMismatchCompensation
        return xMismatchCompensation, yMismatchCompensation

    def move_real_cursor(self, moveX, moveY, currentX, currentY):
        self.actions.move_by_offset(round(moveX), round(moveY))

        self.roundingErrorX += round(moveX) - moveX
        self.roundingErrorY += round(moveY) - moveY
        self.previousX = currentX
        self.previousY = currentY
        self.ranSumX = 0
        self.ranSumY = 0
        self.x_pos += moveX
        self.y_pos += moveY


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
