# HumanLikeSeleniumAPI

### (a better name is welcome)

This API intends to replace and extend the Python version of the ActionChains object of the Selenium API. The documentation can be found below. The original API can be found [here](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html).

## Installing and updating

### Installing

The package can be installed using pip. To do so, first clone this repository

`git clone git@github.com:droefs/HumanLikeSeleniumAPI.git`

Change directories into the project folder

`cd HumanLikeSeleniumAPI`

Activate the OpenWPM conda environment if applicable

`conda activate openwpm`

Now install the package using

`pip install .`

### Updating

In the git repository, retrieve the newest version

`git pull`

Activate the OpenWPM conda environment if applicable

`conda activate openwpm`

Update the package using

`pip install . --upgrade`

## Action chains

### Limitations

- It is not possible to create multiple instances of the HL_ActionChains class. Creating multiple instances will cause the mouse moves to end at a wrong location.
- It is not possible to use HL_ActionChains mouse movements after calling mouse movement functions from the original Selenium ActionChains API.
- Not all functions are yet implemented. Please let me know if any function is needed with priority.

### Example

`from human_like_selenium_api.hl_action_chains import HL_ActionChains`

`from human_like_selenium_api.hl_actions import HL_Actions`

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

**send_keys**(**keys_to_send*)

### Not implemented, but can be implemented:

**click_and_hold**(*on_element=None*)

**double_click**(*on_element=None*)

**drag_and_drop**(*source, target*)

**drag_and_drop_by_offset**(*source, xoffset, yoffset*)

**key_down**(*value, element=None*)

**key_up**(*value, element=None*)

**move_to_element_with_offset**(*to_element, xoffset, yoffset*)

**release**(*on_element=None*)

**send_keys_to_element**(*element, *keys_to_send*)

### Can not be implemented:

**context_click**(*on_element=None*)

**reset_actions**()


## Extension

These functions are part of the HL_Actions class. The extension functions **do not** support the chain pattern. They can **not** be queued up. The function actions are executed directly when the method is called.

### Example

`from human_like_selenium_api.hl_action_chains import HL_ActionChains`

`from human_like_selenium_api.hl_actions import HL_Actions`

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

