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
    HL_Selenium_Actions.write_sentence delay for how long to wait starting a sentence.
'''
SENTENCE_OPENING_DELAY_MEAN = 1.3
SENTENCE_OPENING_DELAY_STD  = 1.0
SENTENCE_OPENING_DELAY_MIN  = 0.2
SENTENCE_OPENING_DELAY_KWARGS = {
    'mean': SENTENCE_OPENING_DELAY_MEAN,
    'std': SENTENCE_OPENING_DELAY_STD,
    'minimal': SENTENCE_OPENING_DELAY_MIN
}


'''
    HL_Selenium_Actions.write_sentence delay between characters
'''
SENTENCE_CHARACTER_DELAY_MEAN = 0.21
SENTENCE_CHARACTER_DELAY_STD  = 0.03
SENTENCE_CHARACTER_DELAY_MIN  = 0.011
SENTENCE_CHARACTER_DELAY_KWARGS = {
    'mean': SENTENCE_CHARACTER_DELAY_MEAN,
    'std': SENTENCE_CHARACTER_DELAY_STD,
    'minimal': SENTENCE_CHARACTER_DELAY_MIN
}


'''
    HL_Selenium_Actions.write_word delay for how long to wait starting a word.
'''
WORD_OPENING_DELAY_MEAN = 0.47
WORD_OPENING_DELAY_STD  = 0.21
WORD_OPENING_DELAY_MIN  = 0.05
WORD_OPENING_DELAY_KWARGS = {
    'mean': WORD_OPENING_DELAY_MEAN,
    'std': WORD_OPENING_DELAY_STD,
    'minimal': WORD_OPENING_DELAY_MIN
}

'''
    HL_Selenium_Actions.write_word delay for how long to wait after completing a word.
'''
WORD_CLOSING_DELAY_MEAN = 0.2
WORD_CLOSING_DELAY_STD  = 0.08
WORD_CLOSING_DELAY_MIN  = 0.01
WORD_CLOSING_DELAY_KWARGS = {
    'mean': WORD_CLOSING_DELAY_MEAN,
    'std': WORD_CLOSING_DELAY_STD,
    'minimal': WORD_CLOSING_DELAY_MIN
}

'''
    HL_Selenium_Actions.write_word delay between the characters in a word.
'''
WORD_CHARACTER_DELAY_MEAN = 0.21
WORD_CHARACTER_DELAY_STD  = 0.03
WORD_CHARACTER_DELAY_MIN  = 0.011
WORD_CHARACTER_DELAY_KWARGS = {
    'mean': WORD_CHARACTER_DELAY_MEAN,
    'std': WORD_CHARACTER_DELAY_STD,
    'minimal': WORD_CHARACTER_DELAY_MIN
}

'''
    HL_Selenium_Actions.write_character delay between the characters in a word.
'''
CHARACTER_SHIFT_DOWN_DELAY_MEAN = 0.06
CHARACTER_SHIFT_DOWN_DELAY_STD  = 0.035
CHARACTER_SHIFT_DOWN_DELAY_MIN  = 0.005
CHARACTER_SHIFT_DOWN_DELAY_KWARGS = {
    'mean': CHARACTER_SHIFT_DOWN_DELAY_MEAN,
    'std': CHARACTER_SHIFT_DOWN_DELAY_STD,
    'minimal': CHARACTER_SHIFT_DOWN_DELAY_MIN
}

'''
    HL_Selenium_Actions.write_character delay between the characters in a word.
'''
CHARACTER_SHIFT_UP_DELAY_MEAN = 0.03
CHARACTER_SHIFT_UP_DELAY_STD  = 0.015
CHARACTER_SHIFT_UP_DELAY_MIN  = 0.003
CHARACTER_SHIFT_UP_DELAY_KWARGS = {
    'mean': CHARACTER_SHIFT_UP_DELAY_MEAN,
    'std': CHARACTER_SHIFT_UP_DELAY_STD,
    'minimal': CHARACTER_SHIFT_UP_DELAY_MIN
}

'''
    HL_Selenium_Actions.write_character delay between the characters in a word.
'''
CHARACTER_DWELL_DELAY_MEAN = 0.06
CHARACTER_DWELL_DELAY_STD  = 0.035
CHARACTER_DWELL_DELAY_MIN  = 0.013
CHARACTER_DWELL_DELAY_KWARGS = {
    'mean': CHARACTER_DWELL_DELAY_MEAN,
    'std': CHARACTER_DWELL_DELAY_STD,
    'minimal': CHARACTER_DWELL_DELAY_MIN
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
KEY_UP_DELAY_MEAN = 0.21
KEY_UP_DELAY_STD  = 0.03
KEY_UP_DELAY_MIN  = 0.011
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
