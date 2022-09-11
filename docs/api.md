## API:

Instantiate the HLISA_ActionChains object by calling:

**HLISA_ActionChains**(*webdriver, browser_resets_cursor_location=True*)

The flag `browser_resets_cursor_location` is depriciated starting from HLISA version 1.5. It only needs to be set for HLISA versions older than 1.5. It needs to be set if your combination of Selenium and web browser do not reset the virtual cursor position to (0, 0) on a new page load. If so, specify *browser_resets_cursor_location=False*. If mouse movements end up in wrong locations, or if elements are not selected, chances are the boolean needs to be flipped.

### Actions provided by both Selenium's ActionChains object and HLISA:

**click**(*on_element=None*, *addDelayAfterAction=True*)

Clicks using the left mouse button. If an element is given, clicks on the given element.  
**Arguments:**

- *(optional)* **on_element**: The element to click.

---

**click_and_hold**(*on_element=None*, *addDelayAfterAction=True*)

Holds down the left mouse button. If an element is given, holds down the mouse on the given element.  
**Arguments:**

- *(optional)* **on_element**: The element to hold down the mouse button on.

---

**context_click**(*on_element=None*)

Clicks using the right mouse button. If an element is given, clicks on the given element. **Note:** This function is **not** human like because functionality to implement it is missing in Selenium. Although clearly not human like, it is still more human like than the normal Selenium *context_click()* function.  
**Arguments:**

- *(optional)* **on_element**: The element to click on with the right mouse button.

---

**double_click**(*on_element=None*, *addDelayAfterAction=True*)

Double-clicks. If an element is given, double-clicks on the given element.  
**Arguments:**

- *(optional)* **on_element**: The element to double-click on.

---

**drag_and_drop**(*source, target*, *addDelayAfterAction=True*)

Moves the mouse to the source element, holds down the left mouse button, moves the mouse to the target element, releases the mouse button. **Note:** This function is **not** human like because functionality to implement it is missing in Selenium. Although clearly not human like, it is still more human like than the normal Selenium *drag_and_drop()* function. **Note**: this functionality might not work, [just as in Selenium](https://github.com/SeleniumHQ/selenium/issues/8345).  
**Arguments:**

- **source**: the element to drag.
- **target**: the element to end the drag on.

---

**drag_and_drop_by_offset**(*source, xoffset, yoffset*, *addDelayAfterAction=True*)

Moves the mouse to the source element, holds down the left mouse button, moves the mouse by the given offset, releases the mouse button. **Note:** This function is **not** human like because functionality to implement it is missing in Selenium. Although clearly not human like, it is still more human like than the normal Selenium *drag_and_drop_by_offset()* function. **Note**: this functionality might not work, [just as in Selenium](https://github.com/SeleniumHQ/selenium/issues/8345).  
**Arguments:**

- **source**: the element to drag.
- **xoffset**: the horizontal distance to move the mouse.
- **yoffset**: the vertical distance to move the mouse.

---

**key_down**(*value, element=None*, *addDelayAfterAction=True*)

Sends a key down event. If an element is specified, the event is send to the given element.  
**Arguments:**

- **value**: the key to send a key down event for.
- *(optional)* **element**: the element to send the key down event to.

---

**key_up**(*value, element=None*, *addDelayAfterAction=True*)

Sends a key release event. If an element is specified, the event is send to the given element.  
**Arguments:**

- **value**: the key to send a key down event for.
- *(optional)* **element**: the element to send the key up event to.

---

**move_by_offset**(*xoffset, yoffset*, *addDelayAfterAction=True*)

Moves the mouse by the given offset.  
**Arguments:**

- **xoffset**: the horizontal distance to move the mouse.
- **yoffset**: the vertical distance to move the mouse.

---

**move_to_element**(*to_element*, *addDelayAfterAction=True*)

Moves to the given element.  
**Arguments:**

- **to_element**: the element to move to.

---

**move_to_element_with_offset**(*to_element, xoffset, yoffset*, *addDelayAfterAction=True*)

Moves to the given offset of an element's top left corner.  
**Arguments:**

- **to_element**: the element to which the offset is relative.
- **xoffset**: the horizontal distance from the left top corner the mouse should move to.
- **yoffset**: the vertical distance from the left top corner the mouse should move to.

---

**pause**(*seconds*)

Introduces a pause between actions.  
**Arguments:**

- **seconds**: the time to pause, in seconds.

---

**perform**()

  Executes all actions on the chain. If you are using `selenium` version 4 or later, calling `perform()` will also remove all actions from the chain (like `reset_actions()` does). If you use a `selenium` version prior to version 4, actions are not removed. This is consistent with how Selenium's `perform()` function behavior changed between version 3 and 4.

---

**release**(*on_element=None*, *addDelayAfterAction=True*)

Releases the left mouse button. If an element is given, releases the mouse on the given element.  
**Arguments:**

- *(optional)* **on_element**: the element to release the mouse button on.

---

**send_keys**(*keys_to_send, element*, *addDelayAfterAction=True*)

Types the given text. If an element is specified, the element is selected before typing starts.  
**Arguments:**

- **keys_to_send**: a string containing the text to send.
- *(optional)* **element**: the element to send the keys to.

---

**send_keys_to_element**(*element, *keys_to_send*, *addDelayAfterAction=True*)

Selects the given element and types the given text.  
**Arguments:**

- **element**: the element to send the keys to.
- **keys_to_send**: a string containing the text to send.

**Note:** characters that are pressed realistically, as if they were typed on a US-International keyboard, are: 0-9, a-z, A-Z, keys in [selenium.webdriver.common.keys.Keys](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys) and all of the following: !@#$%^&*()_+{}|:>?-=[]\;,./


[Dead keys](https://en.wikipedia.org/wiki/Dead_key) in the US-International layout can cause detection.

---

**reset_actions**()

Removes all actions from the chain. **Note:** in contrast to Selenium's `reset_actions()`, which [sometimes](https://stackoverflow.com/questions/67614276/perform-and-reset-actions-in-actionchains-not-working-selenium-python) does [not function as expected](https://github.com/SeleniumHQ/selenium/issues/6837), HLISA's `reset_actions()` does work as described. Consequently, it works not exactly the same as Selenium's `reset_actions()`.  

---

## Additional actions available in HLISA:

These actions are not provided by the standard Selenium API (version 3.141), but they are provided by HLISA to support more human-like scrolling. Also some actions are provided for convenience.

**move_to**(*x, y*, *addDelayAfterAction=True*)

Moves the mouse cursor to the specified coordinates relative to the viewport. The position after the movement will correspond to MouseEvent.clientX and MouseEvent.clientY as specified by [UI Events specification](https://w3c.github.io/uievents/#event-type-mousemove).  
**Arguments:**

- **x**: the x position, relative to the current viewport, to move to.
- **y**: the y position, relative to the current viewport, to move to.

---

**move_to_element_outside_viewport**(*element*, *addDelayAfterAction=True*)

Scrolls the viewport, then moves the mouse to the element.  
**Arguments:**

- **element**: the element to move to (may or may not be outside the current viewport). 

---

**scroll_by**(*x_diff, y_diff*, *addDelayAfterAction=True*, element=None)

Scrolls by *x_diff* and *y_diff* pixels. Scrolling happens in fixed steps of 57 pixels to prevent detection. **Warning: up to 56 pixels can be scrolled more than specified in the parameter to prevent detection.**
**Arguments:**

- **x_dif**: the horizontal distance to scroll. 0 to not scroll horizontally.
- **x_dif**: the vertical distance to scroll. 0 to not scroll vertically.
- **element**: the element to scroll in. If None, the page is scrolled.

---

**scroll_to**(*x, y*, *addDelayAfterAction=True*)

Scrolls to let the viewport top left corner be at pixel *x* and pixel *y*. Scrolling happens in fixed steps of 57 pixels to prevent detection. **Warning: up to 56 pixels can be scrolled more than specified in the parameters to prevent detection.**  
**Arguments:**

- **x**: the x coordinate to scroll the top left corner of the viewport to.
- **y**: the y coordinate to scroll the top left corner of the viewport to.

---

## Other actions:

**back**()

The browser is instructed to go back one page in the browsing history. This function needs to be used instead of the back() function Selenium's **webdriver** object. 

---

**forward**()

The browser is instructed to go forward one page in the browsing history. This function needs to be used instead of the forward() function of Selenium's **webdriver** object.

---

