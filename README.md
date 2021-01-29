# HumanLikeSeleniumAPI

### (a better name is welcome)

This API intends to replace and extend the Python version of the ActionChains object of the Selenium API. The documentation can be found below.

## Quick start

First import the package:

`from HumanLikeSeleniumAPI.cursor import HL_ActionChains`

And create a HL_ActionChains object:

`cursor = HL_ActionChains(webdriver)`

**It is important to only initialize one HL_ActionChains object and continue using it. A new HL_ActionChains will asume the mouse is still at (0, 0).**




## Action chains
The original API can be found [here](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html).


