# HLISA

HLISA is a drop-in replacement for the ActionChains object of the Selenium [API](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html) (Python only), featuring more human-like interaction. Besides providing all functionality the original Selenium ActionChains offers, additional interaction functionality is [provided](https://github.com/droefs/HLISA/blob/master/docs/api.md#additional-actions-available-in-hlisa). HLISA does currently not support Chrome-based browsers, unless an older HLSIA version is used. For details and other considerations of using HLISA, see [the limitations section](https://github.com/droefs/HLISA#limitations).

## Important documents
- [API documentation](https://github.com/droefs/HLISA/blob/master/docs/api.md)
- [Changelog](https://github.com/droefs/HLISA/blob/master/docs/changelog.md)

## Demo

![Demo of HLISA and default Selenium in action](https://github.com/droefs/HLISA/raw/master/hlisa_demo.gif "Demo of HLISA and default Selenium in action")

## Installing and updating

### Installing

The package can be installed using pip:

`pip install HLISA`

And upgraded in the same fashion:

`pip install HLISA --upgrade`

(When using OpenWPM, it might be necessary to activate the correct conda environment before installing or upgrading HLISA: `conda activate openwpm`).

## Usage

See the [API description](https://github.com/droefs/HLISA/blob/master/docs/api.md) for all functions. The HLISA_ActionChains can be used just like the Selenium ActionChains object. It is however not possible to use standard Selenium interaction methods before using HLISA in a single session. This means that executing a Selenium ActionChain before executing an HLISA_ActionChain is not possible. Similarly, calling interaction on Elements (`element.click()`) can not be used before executing HLISA_ActionChains. Using Selenium actions to perform web page interaction before using HLISA in a single session can result in unexpected behavior.

### Usage example

```python
from HLISA.hlisa_action_chains import HLISA_ActionChains

human_like_actions = HLISA_ActionChains(webdriver)
human_like_actions.click()
human_like_actions.perform()
```

**The chain pattern works exactly like the Selenium ActionChains:**

```python
actions = HLISA_ActionChains(webdriver)
menu = webdriver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = webdriver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
actions.move_to_element(menu).click(hidden_submenu).perform()
```

**And so does queuing up:**

```python
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

This flag ensures no delay is added after the action is completed. Delays within the action are unaffected. This also holds for composite actions, for example `.click` with an element specified `.click(element)`: this first moves the mouse to the element, then performs a click. Even if `addDelayAfter=False` is specified, there will be a pause between the mouse movement and the click (only the delay after the click is removed). To remove both delays, call `.move_to_element(element, addDelayAfter=False)` and `.click(addDelayAfter=False)` instead of `.click(element, addDelayAfter=False)`. This allows for complete control over delays between actions, because no delay or a custom delay can be specified this way. Example:

Standard delay after the mouse movement, standard delay after the click:

```python
HLISA_ActionChains(wd)
.click(element)
.perform()
```

Standard delay after the mouse movement, no delay after the click:

```python
HLISA_ActionChains(wd)
.click(element, addDelayAfter=False)
.perform()
```

No delay after the mouse movement, no delay after the click:

```python
HLISA_ActionChains(wd)
.move_to_element(element, addDelayAfter=False)
.click(addDelayAfter=False)
.perform()
```

Custom delay after the mouse movement, custom delay after the click:

```python
HLISA_ActionChains(wd)
.move_to_element(element, addDelayAfter=False)
.pause(0.1)
.click(addDelayAfter=False)
.pause(0.2)
.perform()
```

## API
Check the [API description under docs/api.md.](https://github.com/droefs/HLISA/blob/master/docs/api.md)

## Migrating from Selenium ActionChains to HLISA ActionChains

The functionality HLISA_ActionChains provides is a superset of the functionality provided by Selenium ActionChains. Therefore, migrating is trivial if the existing codebase only uses Selenium ActionChains:

1: import the HLISA ActionChains object:

`from HLISA.hlisa_action_chains import HLISA_ActionChains`

2: replace all occurrences of `ActionChains` by `HLISA_ActionChains`:

`actions = ActionChains(driver)` becomes `actions = HLISA_ActionChains(driver)`

If the syntax form of directly calling interactions on Elements is used (`element.click()`) in the existing codebase, migrating entails rewriting this syntax into ActionChains syntax. Depending on the existing codebase, this can be a time-consuming process.

3: only applicable if `element.click()`-like syntax (calling interaction directly on elements) was used: replace this type of syntax with HLISA_ActionChains syntax (which is equal to Selenium's ActionChains syntax). For example, `element.click()` becomes `HLISA_ActionChains(driver).click(element).perform()`.

## How does it work?

HLISA uses the Selenium API to interact with web pages. Some actions only feature additional delays. For example, HLISA_ActionChains(wd)[.click()](https://github.com/droefs/HLISA/blob/962d5bbc6b8dca64171dbc465be69f9e5dcd1bd4/src/HLISA/selenium_actions.py#L35) is implemented as:

```python
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
'''

## Notes on detection

HLISA (and Selenium) can be immediately detected if the browser is minimized while actions are being performed HLISA. This can be prevented by never minimizing the window when HLISA is active. Also note, that special keys can be detected, when not covered by HLISA (see the API description *send_keys_to_element* for details).

## Limitations

- HLISA does currently not support Chrome-based browsers. A workaround is to use HLISA 1.4.1 (`pip install HLISA==1.4.1`), but it contains some bugs. It is advised to use Firefox instead. See [#31](https://github.com/droefs/HLISA/issues/31) for details. 
- HLISA does not support [threading](https://docs.python.org/3/library/threading.html). It does support [multiprocessing](https://docs.python.org/3/library/multiprocessing.html).
- HLISA does not support a remote end (Selenium Server).
- It is not possible to call interactions on Elements (`element.click()`-like syntax):

`text_field = webdriver.find_element_by_id("text_field")`

`text_field.send_keys("keys")`

This syntax has to be replaced by ActionChains syntax:

`text_field = webdriver.find_element_by_id("text_field")`

`HLISA_ActionChains(webdriver).send_keys("keys", text_field).perform()`

- It is not possible to use HLISA functionality after calling mouse movement functions of the original Selenium ActionChains API.

- The *context_click()* function is not human like.
- The *drag_and_drop()* function is not human like.
- The *drag_and_drop_by_offset()* function is not human like.

- HLISA is slow - it interacts with a web page web only as fast as a standard human would. This contrasts to Selenium which interacts with web pages in a superhuman fashion - just like a standard robot would. Please note that although HLISA is slow, this is only caused by intentionally introduced delays; HLISA is not significantly more resource intensive than Selenium.

- The **back**() and **forward**() functions of Selenium's **webdriver** object are not combatible with HLISA. Instead, the HLISA_ActionChains provides the functions back() and forward() to be used instead, exposing the same functionality.

## Publication and citation

For more details, please see [our IMC 2021 publication](https://doi.org/10.1145/3487552.3487843). If you use HLISA, you can cite our
work as follow:

```
HLISA: towards a more reliable measurement tool. D. Goßen, H. Jonker, S. Karsch,
B. Krumnow and D. Roefs. In Proceedings of the 21st ACM⁄SIGCOMM Internet 
Measurement Conference (IMC’21). ACM, pp. 380–389, 2021. 
```

or by using this BibTeX entry:

```
@inproceedings{GJKKR21,
  author    = {Daniel Go{\ss}en and
               Hugo Jonker and
               Stefan Karsch and
               Benjamin Krumnow and
               David Roefs},
  title     = {{HLISA:} towards a more reliable measurement tool},
  booktitle	= {Proceedings of the 21st ACM Internet Measurement Conference ({IMC'21})},
  pages		= {380--389},
  year      = {2021},
  url       = {https://doi.org/10.1145/3487552.3487843},
  doi       = {10.1145/3487552.3487843}
}
```
