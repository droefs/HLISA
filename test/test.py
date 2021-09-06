class HLISATests(BaseCommand):
    """This command runs HLISA tests"""

    def __init__(self) -> None:
        self.logger = logging.getLogger("openwpm")

    def __repr__(self) -> str:
        return "HLISATestsCommand"

    def execute(
        self,
        webdriver,
        browser_params,
        manager_params,
        extension_socket,
    ) -> None:

        from HLISA.hlisa_action_chains import HLISA_ActionChains

        webdriver.maximize_window()
        webdriver.get('http://localhost:8000/')

        # Clicking test:
        actions = HLISA_ActionChains(webdriver)

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

        actions.reset_actions()
        page2link = webdriver.find_element_by_id("page2link")
        actions.click(page2link)
        actions.perform()

        actions.reset_actions()
        button1 = webdriver.find_element_by_id("button1")
        actions.click(button1)

        # End of tests

        actions.pause(50)
        actions.perform()
