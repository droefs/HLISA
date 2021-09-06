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

        actions.move_by_offset(100, 100)
        actions.scroll_by(0, 100)
        actions.move_to(300, 300)

        actions.pause(5)
        actions.perform()
