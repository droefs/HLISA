import math
import time
import random
import numpy as np

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from HLISA.selenium_actions import HL_Selenium_Actions
from HLISA.additional_actions import HL_Additional_Actions

class HLISA_ActionChains:
    """ This object holds its own chain of actions in self.chain.
        Every API call on this object adds the action to the chain,
        and if the action is ActionChain based itself (meaning it
        only executes after a .perform()), the .perform() is also
        called.
    """
    def __init__(self, webdriver, browser_resets_cursor_location=True):
        self.webdriver = webdriver
        self.chain = []

    ##### Standard Selenium action chain methods #####

    def click(self, element=None, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.click(element, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def click_and_hold(self, on_element=None, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.click_and_hold(on_element, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def context_click(self, on_element=None, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.context_click(on_element, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def double_click(self, on_element=None, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.double_click(on_element, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def drag_and_drop(self, source, target, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.drag_and_drop(source, target, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def drag_and_drop_by_offset(self, source, xoffset, yoffset, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.drag_and_drop_by_offset(source, xoffset, yoffset, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def key_down(self, value, element=None, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.key_down(value, element, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def key_up(self, value, element=None, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.key_up(value, element, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def move_by_offset(self, x, y, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.move_by_offset(x, y, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def move_to_element(self, element, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.move_to_element(element, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def move_to_element_with_offset(self, to_element, xoffset, yoffset, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.move_to_element_with_offset(to_element, xoffset, yoffset, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def pause(self, seconds):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.pause(seconds))
        self.chain.append(lambda: actions.perform())
        return self

    def perform(self):
        for action in self.chain:
            action()
        if HL_Selenium_Actions.selenium_version >= 4:
            self.reset_actions()
        return self

    def release(self, on_element=None, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.release(on_element, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def reset_actions(self):
        self.chain = []
        return self

    def send_keys(self, keys_to_send, element=None, addDelayAfter=True, speed_scaling=1.0):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.send_keys(keys_to_send, element, addDelayAfter, speed_scaling=speed_scaling))
        self.chain.append(lambda: actions.perform())
        return self

    def send_keys_to_element(self, element, keys_to_send, addDelayAfter=True, speed_scaling=1.0):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.send_keys_to_element(element, keys_to_send, addDelayAfter, speed_scaling=speed_scaling))
        self.chain.append(lambda: actions.perform())
        return self

    ##### Additional actions #####

    def move_to(self, x, y, addDelayAfter=True):
        actions = HL_Selenium_Actions(self.webdriver)
        self.chain.append(lambda: actions.move_to(x, y, addDelayAfter))
        self.chain.append(lambda: actions.perform())
        return self

    def move_to_element_outside_viewport(self, element, addDelayAfter=True):
        additional_actions = HL_Additional_Actions(self.webdriver)
        self.chain.append(lambda: additional_actions.move_to_element_outside_viewport(element, addDelayAfter))
        return self

    def scroll_by(self, x_diff, y_diff, addDelayAfter=True, element=None):
        additional_actions = HL_Additional_Actions(self.webdriver)
        self.chain.append(lambda: additional_actions.scroll_by(x_diff, y_diff, addDelayAfter, element))
        return self

    def scroll_to(self, x_diff, y_diff, addDelayAfter=True):
        additional_actions = HL_Additional_Actions(self.webdriver)
        self.chain.append(lambda: additional_actions.scroll_to(x_diff, y_diff, addDelayAfter))
        return self

    def back(self):
        self.webdriver.back()
        return self

    def forward(self):
        self.webdriver.forward()
        return self
