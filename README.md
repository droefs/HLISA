# HumanLikeSeleniumAPI

### (a better name is welcome)

This API intends to replace and extend the Python version of the ActionChains object of the Selenium API. The documentation can be found below.

## Extension

### Implemented:

**move_to_element_outside_viewport**(*element*)

Scrolls the viewport, then moves the mouse to the element.

**scroll_by**(*x_diff, y_diff*)

Scrolls by *x_diff* and *y_diff* pixels. **Warning: up to 56 pixels can be scrolled more than specified in the parameter to prevent detection.**

**scroll_to**(*x, y*)

Scrolls to pixel *x* and pixel *y*. **Warning: up to 56 pixels can be scrolled more than specified in the parameters to prevent detection.**

## Action chains
The original API can be found [here](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html).

### Quick start

### Implemented:

**click**(*on_element=None*)

**move_by_offset**(*xoffset, yoffset*)

**move_to_element**(*to_element*)

**pause**(*seconds*)

**perform**()

### Not implemented, but can be implemented:

**click_and_hold**(*on_element=None*)

**double_click**(*on_element=None*)

**drag_and_drop**(*source, target*)

**drag_and_drop_by_offset**(*source, xoffset, yoffset*)

**key_down**(*value, element=None*)

**key_up**(*value, element=None*)

**move_to_element_with_offset**(*to_element, xoffset, yoffset*)

**release**(*on_element=None*)

**send_keys**(**keys_to_send*)

**send_keys_to_element**(*element, *keys_to_send*)

### Can not be implemented:

**context_click**(*on_element=None*)

**reset_actions**()
