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

        from hlisa.hlisa_action_chains import HLISA_ActionChains

        webdriver.maximize_window()
        webdriver.get('http://localhost:8000/')

        actions = HLISA_ActionChains(webdriver)

        button1 = webdriver.find_element_by_id("button1")
        for i in range(10):
            actions.click(button1)

        actions.perform()