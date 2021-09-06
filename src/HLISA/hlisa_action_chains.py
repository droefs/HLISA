import math
import time
import random
import numpy as np

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from HLISA.util import HL_Util
from HLISA.selenium_actions import HL_Selenium_Actions
from HLISA.additional_actions import HL_Additional_Actions

# This object holds its own chain of actions in self.chain.
# Every API call on this object adds the action to the chain,
# and if the action is ActionChain based itself (meaning it 
# only executes after a .perform()), the .perform() is also 
# called.
class HLISA_ActionChains:

    def __init__(self, webdriver, browser_resets_cursor_location=True):
        self.webdriver = webdriver
        self.chain = []
        HL_Selenium_Actions.browser_resets_cursor_location = browser_resets_cursor_location

    ##### Standard Selenium action chain methods #####

    # Clicks an element.
    # Args:	
    #   on_element: The element to click. If None, clicks on current mouse position.
    def click(self, element=None):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.click(element))
        self.chain.append(lambda: actions.perform())
        return self

    # Holds down the left mouse button on an element.
    # Args:	
    #   on_element: The element to mouse down. If None, clicks on current mouse position.
    def click_and_hold(self, on_element=None):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.click_and_hold(on_element))
        self.chain.append(lambda: actions.perform())
        return self

    # Performs a context-click (right click) on an element.
    # Args:	
    #   on_element: The element to context-click. If None, clicks on current mouse position.
    def context_click(self, on_element=None):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.context_click(on_element))
        self.chain.append(lambda: actions.perform())
        return self

    # Double-clicks an element.
    # Args:	
    #   on_element: The element to double-click. If None, clicks on current mouse position.
    def double_click(self, on_element=None):
        raise NotImplementedError("This functionality is not yet implemented")

    # Holds down the left mouse button on the source element,
    # then moves to the target element and releases the mouse button.
    # Args:	
    #   source: The element to mouse down.
    #   target: The element to mouse up.
    def drag_and_drop(self, source, target):
        raise NotImplementedError("This functionality is not yet implemented")

    # Holds down the left mouse button on the source element,
    #    then moves to the target offset and releases the mouse button.
    # Args:
    #    source: The element to mouse down.
    #    xoffset: X offset to move to.
    #    yoffset: Y offset to move to.
    def drag_and_drop_by_offset(self, source, xoffset, yoffset):
        raise NotImplementedError("This functionality is not yet implemented")

    # Sends a key press only, without releasing it.
    #    Should only be used with modifier keys (Control, Alt and Shift).
    # Args:	
    #    value: The modifier key to send. Values are defined in Keys class.
    #    element: The element to send keys. If None, sends a key to current focused element.
    def key_down(self, value, element=None):
        raise NotImplementedError("This functionality is not yet implemented")

    # Releases a modifier key.
    # Args:	
    #    value: The modifier key to send. Values are defined in Keys class.
    #    element: The element to send keys. If None, sends a key to current focused element.
    def key_up(self, value, element=None):
        raise NotImplementedError("This functionality is not yet implemented")

    # Moving the mouse to an offset from current mouse position.
    # Args:	
    #    xoffset: X offset to move to, as a positive or negative integer.
    #    yoffset: Y offset to move to, as a positive or negative integer.
    def move_by_offset(self, x, y):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.move_by_offset(x, y))
        self.chain.append(lambda: actions.perform())
        return self

    #  Moving the mouse to a random location in an element.
    # Args:	
    #    to_element: The WebElement to move to.
    def move_to_element(self, element):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.move_to_element(element))
        self.chain.append(lambda: actions.perform())
        return self

    # Move the mouse by an offset of the specified element.
    #     Offsets are relative to the top-left corner of the element.
    # Args:	
    #    to_element: The WebElement to move to.
    #    xoffset: X offset to move to.
    #    yoffset: Y offset to move to.
    def move_to_element_with_offset(self, to_element, xoffset, yoffset):
        raise NotImplementedError("This functionality is not yet implemented")

    # Pause all inputs for the specified duration in seconds
    def pause(self, seconds):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.pause(seconds))
        self.chain.append(lambda: actions.perform())
        return self

    # Performs all stored actions.
    def perform(self):
        for action in self.chain:
            action()
        return self

    # Releasing a held mouse button on an element.
    # Args:
    #    on_element: The element to mouse up. If None, releases on current mouse position.
    def release(self, on_element=None):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.release(on_element))
        self.chain.append(lambda: actions.perform())
        return self

    # Clears actions that are already stored locally
    def reset_actions(self):
        self.chain = []
        return self

    # Sends keys to current focused element.
    # Args:	
    #    keys_to_send: The keys to send. Modifier keys constants can be found in the ‘Keys’ class.
    def send_keys(self, keys_to_send):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.send_keys(keys_to_send))
        self.chain.append(lambda: actions.perform())
        return self

    #     Sends keys to an element.
    # Args:	
    #    element: The element to send keys.
    #    keys_to_send: The keys to send. Modifier keys constants can be found in the ‘Keys’ class.
    def send_keys_to_element(self, element, keys_to_send):
        raise NotImplementedError("This functionality is not yet implemented")

    ##### Additional actions #####

    #   Move the mouse a given location.
    # Args:
    #   x: x position to move to.
    #   y: y position to move to.
    def move_to(self, x, y):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.move_to(x, y))
        self.chain.append(lambda: actions.perform())
        return self

    # Moving the mouse to a random location in an element. The element can be outside the viewport.
    # Args:	
    #    to_element: The WebElement to move to.
    def move_to_element_outside_viewport(self, element):
        additional_actions = HL_Additional_Actions(self.webdriver)
        self.chain.append(lambda: additional_actions.move_to_element_outside_viewport(element))

    # Scrolls the viewport by an offset. Scrolling happens in fixed steps of 57 pixels to prevent detection.
    # NOTE: The scrolled distance can thus deviate up to 56 pixels from the distance specified.
    # Args:
    # x_diff: X offset to scroll by.
    # y_diff: Y offset to scroll by.
    def scroll_by(self, x_diff, y_diff):
        additional_actions = HL_Additional_Actions(self.webdriver)
        self.chain.append(lambda: additional_actions.scroll_by(x_diff, y_diff))

    # Scrolls the viewport to a location. Scrolling happens in fixed steps of 57 pixels to prevent detection.
    # NOTE: The scrolled distance can thus deviate up to 56 pixels from the distance specified.
    # Args:
    # x_diff: X location to scroll to.
    # y_diff: Y location to scroll to.
    def scroll_to(self, x_diff, y_diff):
        additional_actions = HL_Additional_Actions(self.webdriver)
        self.chain.append(lambda: additional_actions.scroll_to(x_diff, y_diff))
