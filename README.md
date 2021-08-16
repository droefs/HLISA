# HLISA

This API replaces and extends the Python version of the ActionChains object of the Selenium API. The documentation can be found below. The original Selenium API can be found [here](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html).

## Installing and updating

### Installing

The package can be installed using pip. To do so, first clone this repository

`git clone git@github.com:droefs/HLISA.git`

Change directories into the project folder

`cd HLISA`

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

## Usage

The HLISA_ActionChains can be used just like the Selenium ActionChains object. It is **not** possible to use the standard Selenium ActionChains object alongside HLISA. For details, see the limitations section.

### Example

```
from hlisa.hlisa_action_chains import HLISA_ActionChains
human_like_actions = HLISA_ActionChains(webdriver)
human_like_actions.click()
human_like_actions.perform()
```

**The chain pattern works just like the Selenium ActionChains:**

```
actions = HLISA_ActionChains(webdriver)
menu = webdriver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = webdriver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
actions.move_to_element(menu).click(hidden_submenu).perform()
```

**And so does queuing up:**

```
menu = webdriver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = webdriver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
actions = HLISA_ActionChains(webdriver)`
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
```

## Migrating from Selenium ActionChains to HLISA ActionChains

The HLISA ActionChains API is a strict superset of the Selenium ActionChains API (as soon as it is completely implemented). Therefore, it is possible to migrate in two steps:

1: import the HLISA ActionChains object:

`from hlisa.hlisa_action_chains import HLISA_ActionChains`

2: replace all occurrences of `ActionChains` by `HLISA_ActionChains`:

`actions = ActionChains(driver)` becomes `actions = HLISA_ActionChains(driver)`

## API:

### Selenium actions:

#### Implemented:

**click**(*on_element=None*)

**click_and_hold**(*on_element=None*)

**move_by_offset**(*xoffset, yoffset*)

**move_to_element**(*to_element*)

**pause**(*seconds*)

**perform**()

**release**(*on_element=None*)

**send_keys**(**keys_to_send*)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Note:** characters that are pressed realistically, as if they were typed on a US-International keyboard, are: 0-9, a-z, A-Z, keys in &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[selenium.webdriver.common.keys.Keys](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys) and all of the following: !@#$%^&*()_+{}|:>?-=[]\;,./

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Dead keys](https://en.wikipedia.org/wiki/Dead_key) in the US-International layout can cause detection.

#### Not implemented, but can be implemented:

**double_click**(*on_element=None*)

**drag_and_drop**(*source, target*)

**drag_and_drop_by_offset**(*source, xoffset, yoffset*)

**key_down**(*value, element=None*)

**key_up**(*value, element=None*)

**move_to_element_with_offset**(*to_element, xoffset, yoffset*)

**send_keys_to_element**(*element, *keys_to_send*)

**reset_actions**()

### Can not be implemented human like:

**context_click**(*on_element=None*)


### Additional actions:

**move_to_element_outside_viewport**(*element*)

Scrolls the viewport, then moves the mouse to the element.

**scroll_by**(*x_diff, y_diff*)

Scrolls by *x_diff* and *y_diff* pixels. **Warning: up to 56 pixels can be scrolled more than specified in the parameter to prevent detection.**

**scroll_to**(*x, y*)

Scrolls to pixel *x* and pixel *y*. **Warning: up to 56 pixels can be scrolled more than specified in the parameters to prevent detection.**


### Limitations

- Not all functions are implemented yet.
- It is not possible to call interactions on Elements, like so:

`text_field = webdriver.find_element_by_id("text_field")`

`text_field.send_keys("HLISA")`

This will function, but the interaction is performed by Selenium, not HLISA, and therefore does not seem human like.

- It is not possible to use HL_ActionChains mouse movements after calling mouse movement functions from the original Selenium ActionChains API.

## Further notes

Apart from special keys (as noted above), Selenium and HLISA can be immediately detected if a headful instance of the browser is minimized while actions are being performed by Selenium or HLISA. This can be prevented by never minimizing the window with Selenium or HLISA active.