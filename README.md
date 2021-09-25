# HLISA

HLISA is a drop-in replacement for the ActionChains object of the Selenium [API](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html) (Python only), featuring more human-like interaction. Besides providing all functionality the original Selenium ActionChains offers, additional interaction functionality is provided. Calling interaction on elements (`element.click()`) is not provided.

## Installing and updating

### Installing

The package can be installed using pip:

`pip install HLISA`

And upgraded in the same fashion:

`pip install HLISA --upgrade`

(When using OpenWPM, it might be necessary to activate the correct conda environment before installing or upgrading HLISA: `conda activate openwpm`).

## Usage

The HLISA_ActionChains can be used just like the Selenium ActionChains object. It is however not possible to use standard Selenium interaction methods before using HLISA in a single session. This means that executing a Selenium ActionChain before executing an HLISA_ActionChain is not possible. Similarly, calling interaction on Elements (`element.click()`) can not be used before executing HLISA_ActionChains. Using Selenium actions to perform web page interaction before using HLISA in a single session can result in unexpected behavior.

### Usage example

```
from HLISA.hlisa_action_chains import HLISA_ActionChains

human_like_actions = HLISA_ActionChains(webdriver)
human_like_actions.click()
human_like_actions.perform()
```

**The chain pattern works exactly like the Selenium ActionChains:**

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

### Difference in element selection

In contrast to Selenium ActionChains, HLISA_ActionChains functions do not select items when the elements are hidden (for example behind an image). This can cause different results. If an item is not selected because it is hidden, HLISA prints a message to the console. 

### More fine-grained control

By default, HLISA introduces delays within actions to make its interaction with web pages more human-like. An additional delay is added after every action to make the collection of interactions more human-like as well. In case you want to control the delay between actions yourself, use the `addDelayAfter`-flag when adding an action to the HLISA_ActionChain:

`actions.click(addDelayAfter=False)`

This flag ensures no delay is added after the action is completed. Delays within the action are unaffected.

## Migrating from Selenium ActionChains to HLISA ActionChains

The functionality HLISA_ActionChains provides is a superset of the functionality provided by Selenium ActionChains. Therefore, migrating is trivial if the existing codebase only uses Selenium ActionChains:

1: import the HLISA ActionChains object:

`from HLISA.hlisa_action_chains import HLISA_ActionChains`

2: replace all occurrences of `ActionChains` by `HLISA_ActionChains`:

`actions = ActionChains(driver)` becomes `actions = HLISA_ActionChains(driver)`

If the syntax form of directly calling interactions on Elements is used (`element.click()`) in the existing codebase, migrating entails rewriting this syntax into ActionChains syntax. Depending on the existing codebase, this can be a time-consuming process.

3: only applicable if `element.click()`-like syntax (calling interaction directly on elements) was used: replace this type of syntax with HLISA_ActionChains syntax (which is equal to Selenium's ActionChains syntax). For example, `element.click()` becomes `HLISA_ActionChains(driver).click(element).perform()`.

## API:

Instantiate the HLISA_ActionChains object by calling:

**HLISA_ActionChains**(*webdriver, browser_resets_cursor_location=True*)

If your combination of Selenium and web browser do not reset the virtual cursor position to (0, 0) on a new page load, specify *browser_resets_cursor_location=False*. If mouse movements end up in wrong locations, or if elements are not selected, chances are this setting needs to altered.

### Actions provided by both Selenium's ActionChains object and HLISA:

**click**(*on_element=None*)

**click_and_hold**(*on_element=None*)

**context_click**(*on_element=None*) **Note:** This function is **not** human like because functionality to implement it is missing in Selenium. Although clearly not human like, it is still more human like than the normal Selenium *context_click()* function.

**double_click**(*on_element=None*)

**drag_and_drop**(*source, target*)

Warning: this functionality might not work, [just as in Selenium](https://github.com/SeleniumHQ/selenium/issues/8345).

**drag_and_drop_by_offset**(*source, xoffset, yoffset*)

Warning: this functionality might not work, [just as in Selenium](https://github.com/SeleniumHQ/selenium/issues/8345).

**key_down**(*value, element=None*)

**key_up**(*value, element=None*)

**move_by_offset**(*xoffset, yoffset*)

**move_to_element**(*to_element*)

**move_to_element_with_offset**(*to_element, xoffset, yoffset*)

**pause**(*seconds*)

**perform**()

**release**(*on_element=None*)

**send_keys**(**keys_to_send*)

**send_keys_to_element**(*element, *keys_to_send*)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Note:** characters that are pressed realistically, as if they were typed on a US-International keyboard, are: 0-9, a-z, A-Z, keys in &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[selenium.webdriver.common.keys.Keys](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys) and all of the following: !@#$%^&*()_+{}|:>?-=[]\;,./

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Dead keys](https://en.wikipedia.org/wiki/Dead_key) in the US-International layout can cause detection.

**reset_actions**()

### Additional actions available in HLISA:

These actions are not provided by the standard Selenium API (version 3.141), but they are provided by HLISA to support more human-like scrolling. Also some actions are provided for convenience.

**move_to**(*x, y*)

Moves the mouse cursor to the specified coordinates relative to the viewport. The position after the movement will correspond to MouseEvent.clientX and MouseEvent.clientY as specified by [UI Events specification](https://w3c.github.io/uievents/#event-type-mousemove).

**move_to_element_outside_viewport**(*element*)

Scrolls the viewport, then moves the mouse to the element.

**scroll_by**(*x_diff, y_diff*)

Scrolls by *x_diff* and *y_diff* pixels. **Warning: up to 56 pixels can be scrolled more than specified in the parameter to prevent detection.**

**scroll_to**(*x, y*)

Scrolls to let the viewport top left corner be at pixel *x* and pixel *y*. **Warning: up to 56 pixels can be scrolled more than specified in the parameters to prevent detection.**

### Limitations

- HLISA does not support a remote end (Selenium Server).
- It is not possible to call interactions on Elements (`element.click()`-like syntax):

`text_field = webdriver.find_element_by_id("text_field")`

`text_field.send_keys("keys")`

This syntax has to be replaced by ActionChains syntax:

`text_field = webdriver.find_element_by_id("text_field")`

`HLISA_ActionChains(webdriver).send_keys(text_field, "keys").perform()`

- It is not possible to use HLISA functionality after calling mouse movement functions of the original Selenium ActionChains API.

- The *context_click()* function is not human like.

- HLISA is slow - it interacts with a web page web only as fast as a standard human would. This contrasts to Selenium which interacts with web pages in a superhuman fashion - just like a standard robot would. Please note that although HLISA is slow, this is only caused by intentionally introduced delays; HLISA is not significantly more resource intensive than Selenium.

## Further notes

Apart from special keys (as noted above), Selenium and HLISA can be immediately detected if a headful instance of the browser is minimized while actions are being performed by Selenium or HLISA. This can be prevented by never minimizing the window when Selenium or HLISA is active.

## How does it work?

HLISA uses the Selenium API to interact with web pages. Some actions only feature additional delays. For example, HLISA_ActionChains(wd)[.click()](https://github.com/droefs/HLISA/blob/962d5bbc6b8dca64171dbc465be69f9e5dcd1bd4/src/HLISA/selenium_actions.py#L35) is implemented as:

```
    def click(self, element=None):
        if element is not None:
            self.move_to_element(element)
        self.actions.click_and_hold()
        self.actions.pause(np.random.normal(0.092, 0.018))
        self.actions.release()
        self.addDelayAfterAction()
        return self
```

Other functions add additional actions. For example, a HLISA mouse movement consists of hundreds of tiny Selenium mouse movements that together form a jittery curve.