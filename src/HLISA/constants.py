'''
    HLISA Time (Delay) Constants

    When delays are in sets of 4 with the postfixes 
    `_MEAN`, `_STD`, `_MIN` & `_KWARGS they are used as
    argumenst to culculate a delay using HLISA.util.std_positive.
    The `_KWARGS` postfix is used for unpacking as keyword arguments.

'''



'''
    HL_Selenium_Actions.addDelayAfterAction delay constants.
'''
ACTION_DELAY_MEAN = 0.3
ACTION_DELAY_STD  = 0.1
ACTION_DELAY_MIN  = 0.025
ACTION_DELAY_KWARGS = {
    'mean': ACTION_DELAY_MEAN,
    'std': ACTION_DELAY_STD,
    'minimal': ACTION_DELAY_MIN
}

'''
    HL_Selenium_Actions.click delay for how long the mouse is held down
    during a normal click.
'''
CLICK_HOLD_DELAY_MEAN = 0.092
CLICK_HOLD_DELAY_STD  = 0.018
CLICK_HOLD_DELAY_MIN  = 0.0
CLICK_HOLD_DELAY_KWARGS = {
    'mean': CLICK_HOLD_DELAY_MEAN,
    'std': CLICK_HOLD_DELAY_STD,
    'minimal': CLICK_HOLD_DELAY_MIN
}

'''
    HL_Selenium_Actions.send_keys delay for how long to wait before adding the '.'
    at the end of a sentence.
'''
SENTENCE_CLOSING_DELAY_MEAN = 1.7
SENTENCE_CLOSING_DELAY_STD  = 0.7
SENTENCE_CLOSING_DELAY_MIN  = 0.3
SENTENCE_CLOSING_DELAY_KWARGS = {
    'mean': SENTENCE_CLOSING_DELAY_MEAN,
    'std': SENTENCE_CLOSING_DELAY_STD,
    'minimal': SENTENCE_CLOSING_DELAY_MIN
}

'''
    HL_Selenium_Actions.send_keys delay for how long to wait after completing
    an entire sentence including.
'''
SENTENCE_COMPLETION_DELAY_MEAN = 0.6
SENTENCE_COMPLETION_DELAY_STD  = 0.4
SENTENCE_COMPLETION_DELAY_MIN  = 0.05
SENTENCE_COMPLETION_DELAY_KWARGS = {
    'mean': SENTENCE_COMPLETION_DELAY_MEAN,
    'std': SENTENCE_COMPLETION_DELAY_STD,
    'minimal': SENTENCE_COMPLETION_DELAY_MIN
}

'''
    HL_Selenium_Actions.key_down delay after the action if the addDelayAfter=True
'''
KEY_DOWN_DELAY_MEAN = 0.06
KEY_DOWN_DELAY_STD  = 0.035
KEY_DOWN_DELAY_MIN  = 0.013
KEY_DOWN_DELAY_KWARGS = {
    'mean': KEY_DOWN_DELAY_MEAN,
    'std': KEY_DOWN_DELAY_STD,
    'minimal': KEY_DOWN_DELAY_MIN
}

'''
    HL_Selenium_Actions.key_up delay after the action if the addDelayAfter=True
'''
KEY_UP_DELAY_MEAN = 0.06
KEY_UP_DELAY_STD  = 0.035
KEY_UP_DELAY_MIN  = 0.013
KEY_UP_DELAY_KWARGS = {
    'mean': KEY_UP_DELAY_MEAN,
    'std': KEY_UP_DELAY_STD,
    'minimal': KEY_UP_DELAY_MIN
}

'''
    The following delays are used with the numpy.random.normal function, and
    thus the '_KWARGS' post fix version have different keys that correspond 
    to the numpy implementation.
'''

'''
    HL_Selenium_Actions.double_click delay to hold the first click.
'''
DOUBLE_CLICK_FIRST_HOLD_DELAY_MEAN = 0.083
DOUBLE_CLICK_FIRST_HOLD_DELAY_STD  = 0.034
DOUBLE_CLICK_SECOND_HOLD_DELAY_KWARGS = {
    'loc': DOUBLE_CLICK_FIRST_HOLD_DELAY_MEAN,
    'scale': DOUBLE_CLICK_FIRST_HOLD_DELAY_STD 
}

'''
    HL_Selenium_Actions.double_click delay between the two clicks.
'''
DOUBLE_CLICK_BETWEEN_DELAY_MEAN = 0.075
DOUBLE_CLICK_BETWEEN_DELAY_STD  = 0.026
DOUBLE_CLICK_BETWEEN_DELAY_KWARGS = {
    'loc': DOUBLE_CLICK_BETWEEN_DELAY_MEAN,
    'scale': DOUBLE_CLICK_BETWEEN_DELAY_STD 
}


'''
    HL_Selenium_Actions.double_click delay to hold the second click.
'''
DOUBLE_CLICK_SECOND_HOLD_DELAY_MEAN = 0.051
DOUBLE_CLICK_SECOND_HOLD_DELAY_STD  = 0.016
DOUBLE_CLICK_SECOND_HOLD_DELAY_KWARGS = {
    'loc': DOUBLE_CLICK_SECOND_HOLD_DELAY_MEAN,
    'scale': DOUBLE_CLICK_SECOND_HOLD_DELAY_STD 
}
