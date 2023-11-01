import math
import time
import random
import numpy as np
from HLISA.errors import (ElementBoundariesWereZeroException,
                            IllegalArgumentException,
                            NoCursorCoordinatesException)

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.remote.webelement import WebElement

from selenium.common.exceptions import MoveTargetOutOfBoundsException

class HL_Util:
    def create_pointer_move(self, duration=50, x=None, y=None, origin=None):
        """ The function to replace the original Selenium function that does not support specifying the duration.
        """
        action = dict(type="pointerMove", duration=duration)
        action["x"] = x
        action["y"] = y
        if isinstance(origin, WebElement):
            action["origin"] = {"element-6066-11e4-a52e-4f735466cecf": origin.id}
        elif origin is not None:
            action["origin"] = origin

        self.add_action(action)

def behavorial_element_coordinates(webdriver, element):
    """ Takes an element and returns coordinates somewhere in the element. If the element is not visable, it returns None.
        Uses a normal distribution, to bias the click towards the center of the element.
    """
    x_relative = int(element.rect['x']) - get_current_scrolling_position(webdriver)["x"]
    y_relative = int(element.rect['y']) - get_current_scrolling_position(webdriver)["y"]
    viewport_width = webdriver.execute_script("return window.innerWidth")
    viewport_height = webdriver.execute_script("return window.innerHeight")
    if element.rect['width'] == 0 or element.rect['height'] == 0:
        error_msg = """
            The element's plane was zero. To avoid this issue, you may want to use:
                from HLISA.util import best_effort_element_selection as best_selection
                from HLISA.errors import ElementBoundariesWereZeroException
                try:
                    click_with_HLISA(driver, el)
                except ElementBoundariesWereZeroException:
                    best_el = best_selection(driver, el)
                    click_with_HLISA(driver, best_el[0])
        """
        raise ElementBoundariesWereZeroException(error_msg)
    for _ in range(100): # Try 10 random positions, as some positions are not in round buttons.
        x = x_relative + int(np.random.normal(int(element.rect['width']*0.5), int(element.rect['width']*0.2)))
        y = y_relative + int(np.random.normal(int(element.rect['height']*0.5), int(element.rect['height']*0.2)))
        
        if x < 0 or y < 0 or x > viewport_width or y > viewport_height:
            continue
        
        coords_in_button = webdriver.execute_script(f"return document.elementFromPoint({x}, {y}) === arguments[0];", element)
        coords_in_descendant = webdriver.execute_script(f"""
            let el = document.elementFromPoint({x}, {y});
            return [...arguments[0].querySelectorAll('*')].includes(el);""", element)

        if coords_in_button or coords_in_descendant:
            return (x, y)
    return None

def std_positive(mean, std, minimal):
    """ Returns a number from a normal distribution that is larger or equal to parameter 'minimal'.
        Due to the minimum value, the returned values will not form a normal distribution.
        To minimize this effect, values that would have been smaller than the minimum are not drawn
        again, but get added a random small value. The new number will never become larger as the mean.
    """
    if minimal > mean:
        raise IllegalArgumentException(
            f"\n\tMethod util.std_positive expects argument 'minimal' <= 'mean'\n" + \
            f"\tGot:\n\t\tminimal: {minimal}\n\t\tmean: {mean}"
        )
    sample = np.random.normal(mean, std)
    if sample < minimal:
        sample += (minimal-sample) + (mean - minimal)*random.random()
    return sample

def scale_delay_kwargs(scaling, delay_kwargs):
    return {
        'mean': delay_kwargs['mean'] * (1/scaling),
        'std': delay_kwargs['mean'],
        'minimal': delay_kwargs['mean'],
    }
    

def increaseMousemovementSpeed():
    """ Replace a function in the original Selenium API to increase mouse movement speed.
    """
    PointerInput.create_pointer_move = HL_Util.create_pointer_move

def get_current_scrolling_position(webdriver, element=None):
    """ Returns the x and y offset for scrolling
    """
    if element:
        return ({"x": int(element.get_attribute("scrollLeft")), "y": int(element.get_attribute("scrollTop"))})
    return webdriver.execute_script("return {'x':window.pageXOffset, 'y':window.pageYOffset};")

def get_scrollable_elements(webdriver, element):
    """
    """
    script = """
        let scrollNodes = [];
        let node = arguments[0];

        function getScrollParent(node) {
          if (node == null) {
            return null;
          }
          if (node.scrollHeight > node.clientHeight) {
              return node;
          } else {
            return getScrollParent(node.parentNode);
          }
        }

        while (node != null){
          node = getScrollParent(node.parentNode);
          if (node != null){
              scrollNodes.push(node);
          }
        }
        return scrollNodes;
    """
    return webdriver.execute_script(script, element)

def element_is_scrollable(webdriver, element):
    """
    """
    script = """
        let node = arguments[0];
        if (node == null) {
            return false;
        }
        return node.scrollHeight > node.clientHeight;
    """
    return webdriver.execute_script(script, element)

def best_effort_element_selection(webdriver, element):
    """ Collection of best efforts approaches to select a clickable element
    """
    if element.rect["height"] == 0 or element.rect["width"] == 0:
        script ="""
            let res = [];
            arguments[0].querySelectorAll('*').forEach(el => {
                if (el.clientWidth > 0 && el.clientHeight > 0){
                    res.push(el);
                }
            });
            return res;"""
        candidates = webdriver.execute_script(script, element)
        return candidates

# Use the coordinate information from the Selenium 
# MoveTargetOutOfBoundsException to get the coordinates
# of the Selenium mouse cursor.
def get_cursor_coordinates(driver):
    MOVE_PIXELS = 30000
    try:
        ac = ActionChains(driver)
        ac.move_by_offset(MOVE_PIXELS, MOVE_PIXELS)
        ac.perform()
    except MoveTargetOutOfBoundsException as ex:
        error_message = str(ex)[10:23]
        x = error_message[0:5]
        y = error_message[7:12]
        try:
            x = int(x)
            y = int(y)
        except Exception as e:
            raise NoCursorCoordinatesException() # If the coordinates are not integers, something went wrong
        if x < 0 or y < 0:
            raise NoCursorCoordinatesException()
        return (x - MOVE_PIXELS, y - MOVE_PIXELS)
    raise NoCursorCoordinatesException() # If no exception occured, something went wrong
