import math
import time
import random
import numpy as np

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HL_ActionChains:
    
    def __init__(self, webdriver):
        self.x_pos = 0
        self.y_pos = 0
        self.webdriver = webdriver
        self.actions = ActionChains(webdriver)

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

    # Moves to a position in the viewport
    # Args:
    #   x: x-coordinate to move to
    #   y: y-coordinate to move to
    def move_to(self, x, y):
        t_cursor = TheoreticalCursor(self.x_pos, self.y_pos, x, y, self.webdriver, self.actions)
        self.x_pos = t_cursor.x_pos
        self.y_pos = t_cursor.y_pos

    def move_by_offset(self, x, y):
        self.move_to(self.x_pos + x, self.y_pos + y)

    def move_to_element(self, element):
        viewport_height = self.webdriver.execute_script("return window.innerHeight")
        y_relative = int(element.rect['y']) - self.webdriver.execute_script("return window.pageYOffset;")
        if y_relative < 0:
            print("not possible, out of viewport")
        elif y_relative > viewport_height:
            print("not possible, out of viewport")
        x, y = self.behavorial_element_coordinates(self.webdriver, element)
        print("x: " + str(x) + " y: " + str(y))
        print("xpos: " + str(self.x_pos) + " ypos: " + str(self.y_pos))
        self.move_to(x, y)

    def perform(self):
        self.actions.perform()
        self.actions = ActionChains(self.webdriver)


    ##### Non-Action chain methods #####


    #First scrolls to get the element into the viewport, then performs the movement
    def move_to_element_outside_viewport(self, element):
        viewport_height = self.webdriver.execute_script("return window.innerHeight")
        y_relative = int(element.rect['y']) - self.webdriver.execute_script("return window.pageYOffset;")
        print("y relative: " + str(y_relative) + " pageyoffset: " + str(self.webdriver.execute_script("return window.pageYOffset;")))
        if y_relative < 0:
            self.scroll_by(self.webdriver, 0, y_relative)
        elif y_relative > viewport_height:
            self.scroll_by(self.webdriver, 0, y_relative - viewport_height/2)
        x, y = self.behavorial_element_coordinates(self.webdriver, element)
        #actions = ActionChains(self.webdriver)        
        self.move_to(x, y)
        self.perform()

    # This function scrolls a few pixels further if the parameter is not a multiple of a standard scroll value.
    # It would be detectable otherwise.
    def scroll_by(self, webdriver, x_diff, y_diff):
        #self.x_pos += x_diff
        #self.y_pos += y_diff
        #print("y+diff" + str(y_diff))
        #print("y+poss " + str(self.y_pos))
        time.sleep(random.random() + 0.5)    
        if x_diff != 0:
            logger.error("Scrolling horizontal not implemented")
        if y_diff > 0:
            self.scroll_down(webdriver, y_diff)
        else:
            self.scroll_up(webdriver, y_diff)

    def scroll_down(self, webdriver, y_diff):
        current_y = webdriver.execute_script("return window.pageYOffset;")
        max_y = webdriver.execute_script("return document.body.scrollHeight;")
        y_diff = min(y_diff, max_y - current_y) # Prevent scrolling too far
        scroll_ticks = 0
        while y_diff > 0:
            webdriver.execute_script("window.scrollBy(0, 57)")
            y_diff -= 57
            time.sleep(0.05 + (random.random()/200))
            scroll_ticks += 1
            if scroll_ticks % 7 == 0:
                time.sleep(0.5)

    def scroll_up(self, webdriver, y_diff):
        current_y = webdriver.execute_script("return window.pageYOffset;")
        min_y = 0
        y_diff = max(y_diff, min_y - current_y) # Prevent scrolling too far
        scroll_ticks = 0
        while y_diff < 0:
            webdriver.execute_script("window.scrollBy(0, -57)")
            y_diff += 57
            time.sleep(0.05 + (random.random()/200))
            scroll_ticks += 1
            if scroll_ticks % 7 == 0:
                time.sleep(0.5)

    # This function scrolls a few pixels further if the parameter is not a multiple of a standard scroll value.
    # It would be detectable otherwise.
    def scroll_to(self, webdriver, x, y):
        time.sleep(random.random() + 0.5)   
        current_x = webdriver.execute_script("return window.pageXOffset;")
        if current_x != x:
            logger.error("Scrolling horizontal not yet implemented")
        current_y = webdriver.execute_script("return window.pageYOffset;")
        y_diff = y - current_y
        self.scroll_by(webdriver, x, y_diff)
        
    

    ##### Helper functions #####

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
            print(" speciale y: " + str(y))
            if coords_in_button:
                return (x, y)
        return None

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
        interval = 60 # Once in 'interval' pixels, the cursor is actually moved.
        sample_points = []
        initialDelay = interval
        delay = initialDelay
        for i in range(1, minimalDiff):
            #sample_points.append(1-(1/i**(i/minimalDiff)))
            #sample_points = [round(j * minimalDiff) for j in sample_points]
            if i % 50 == 0:#delay == 0:            
                sample_points.append(i/minimalDiff)
                initialDelay *= 0.7
                delay = initialDelay
            delay -= 1
        sample_points = [round(j * minimalDiff) for j in sample_points]
        print(sample_points)
        return sample_points
