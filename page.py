import time
from playwright.sync_api import Playwright, sync_playwright

class ExtractContent:
    def __init__(self, playwright: Playwright,headless=True):
        self.browser = playwright.start().chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def go_to_page(self, url):
        response = self.page.goto(url)
        if response.status == 200:
            return self.page.content()
        else:
            return False

    def close_browser(self):
        if self.browser:
            self.browser.close()
            self.browser = None
            self.context = None  # Close the context along with the browser
            self.page = None
        else:
            raise Exception("Browser not initialized. Call initialize_browser() first.")

if __name__ == "__main__":
    browser = ExtractContent(sync_playwright(),headless=False)
    response = browser.go_to_page("https://google.com")
    if response:
        print(response)

    browser.close_browser()
