# HumanLikeSeleniumAPI

### (a better name is welcome)

This API intends to replace and extend the Python version of the ActionChains object of the Selenium API. The documentation can be found below. The original API can be found [here](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html).

## Action chains

### Example

`from HumanLikeSeleniumAPI.hl_action_chains import HL_ActionChains`

`from HumanLikeSeleniumAPI.hl_actions import HL_Actions`

**The chain pattern works just like the Selenium ActionChains:**

`actions = HL_ActionChains(webdriver)`

`menu = driver.find_element(By.CSS_SELECTOR, ".nav")`

`hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")`

`actions.move_to_element(menu).click(hidden_submenu).perform()`

**Just as queuing up:**

`menu = driver.find_element(By.CSS_SELECTOR, ".nav")`

`hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")`

`actions = HL_ActionChains(webdriver)`

`actions.move_to_element(menu)`

`actions.click(hidden_submenu)`

`actions.perform()`

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


## Extension

These functions are part of the HL_Actions class. The extension functions **do not** support the chain pattern. They can **not** be queued up. The function actions are executed directly when the method is called.

### Example

`from HumanLikeSeleniumAPI.hl_action_chains import HL_ActionChains`

`from HumanLikeSeleniumAPI.hl_actions import HL_Actions`

`actions = HL_ActionChains(webdriver)`

`extension = HL_Actions(actions, webdriver)`

`extension.scroll_by(0, 500)`

### Implemented:

**move_to_element_outside_viewport**(*element*)

Scrolls the viewport, then moves the mouse to the element.

**scroll_by**(*x_diff, y_diff*)

Scrolls by *x_diff* and *y_diff* pixels. **Warning: up to 56 pixels can be scrolled more than specified in the parameter to prevent detection.**

**scroll_to**(*x, y*)

Scrolls to pixel *x* and pixel *y*. **Warning: up to 56 pixels can be scrolled more than specified in the parameters to prevent detection.**

