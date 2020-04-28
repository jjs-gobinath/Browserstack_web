from selenium import webdriver


class Driver:

    def __init__(self):
        self.instance = webdriver.Chrome()

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")

    def getWindowHandles(self):
        return self.instance.window_handles

    def getWindowTitle(self,pos):
        handles = self.instance.window_handles
        self.instance.switch_to.window(handles[pos])
        return self.instance.title