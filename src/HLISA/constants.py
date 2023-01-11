'''
    HLISA Time (Delay) Constants

    When delays are in sets of 4 with the postfixes 
    `_MEAN`, `_STD`, `_MIN` & `_KWARGS they are used 
    argumenst to culculate a delay using HLISA.util.std_positive.
    The `_KWARGS` postfix is used for unpacking as keyword arguments.

'''



'''
    HL_Selenium_Actions.addDelayAfterAction delay constants
'''
ACTION_DELAY_MEAN = 0.3
ACTION_DELAY_STD  = 0.1
ACTION_DELAY_MIN  = 0.025
ACTION_DELAY_KWARGS = {
    'mean': ACTION_DELAY_MEAN,
    'std': ACTION_DELAY_STD,
    'min': ACTION_DELAY_MIN
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
    'min': CLICK_HOLD_DELAY_MIN
}

'''

'''

def foo(b, a):
    print(a, b)

if __name__ == "__main__":
    x = {'a': 12, 'b': 17}
    foo(**x)