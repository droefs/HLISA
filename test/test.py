#!/usr/bin/env python

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium_firefox import FirefoxBinary, FirefoxLogInterceptor, Options
from HLISA.hlisa_action_chains import HLISA_ActionChains
import os.path
import sys
import time

fb = FirefoxBinary(firefox_path="firefox/firefox")
webdriver = webdriver.Firefox(firefox_binary=fb)


webdriver.maximize_window()
webdriver.set_page_load_timeout(30)


webdriver.get('http://localhost:8000/')

# Clicking test:
actions = HLISA_ActionChains(webdriver)
actions.scroll_by(0, 100)
button1 = webdriver.find_element_by_id("button1")
for i in range(10):
    actions.click(button1)

# Context clicking test:

button2 = webdriver.find_element_by_id("button2")
actions.context_click(button2)

# Test whether cursor location is correct after scroll:

actions.scroll_by(0, 100)
button3 = webdriver.find_element_by_id("button3")
actions.click(button3)
        
actions.perform()

# Test whether the cursor location is correcter after a different page has been loaded:

webdriver.get('http://localhost:8000/page2.html')

actions.reset_actions()
button1 = webdriver.find_element_by_id("button1")
actions.click(button1)

# Test drag and drop:

draggable_element = webdriver.find_element_by_id("draggable_element")
drag_endpoint = webdriver.find_element_by_id("drag_endpoint")
actions.drag_and_drop(draggable_element, drag_endpoint)

# Element with offset test:

element_with_offset = webdriver.find_element_by_id("element_with_offset")
actions.move_to_element_with_offset(element_with_offset, 12, 34)
actions.click()

# Double click test:

double_click_element = webdriver.find_element_by_id("double_click")
actions.double_click(double_click_element)

# Test drag and drop with offset:

draggable_element_offset = webdriver.find_element_by_id("draggable_element_offset")
drag_endpoint_offset = webdriver.find_element_by_id("drag_endpoint_offset")
actions.drag_and_drop_by_offset(draggable_element_offset, 500, 80)

# Send keys to element test:

send_keys_to_element_test = webdriver.find_element_by_id("send_keys_to_element_test")
actions.send_keys_to_element(send_keys_to_element_test, "test test")

# Key up and key down test:

key_up_key_down_test = webdriver.find_element_by_id("key_up_key_down_test")
actions.key_down("a", key_up_key_down_test)
actions.key_up("a")
actions.key_down("b")
actions.key_up("b")

# End of tests

actions.pause(50)
actions.perform()