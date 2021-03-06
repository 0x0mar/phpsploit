import webbrowser
from ui.color import colorize


class WebBrowser(str):
    """Web browser object. (extends str, and users webbrowser lib);

    Takes the name of an available web browser in the current system.

    >>> browser = WebBrowser('firefox')
    >>> browser()
    "/usr/bin/firefox"
    >>> browser.open('http://www.google.com/')
    True

    """
    def __new__(cls, name):
        blacklist = ['macosx']
        lst = [x for x in webbrowser._browsers.keys() if x not in blacklist]
        fmt = ", ".join(lst)
        if name and name != "default" and name not in lst:
            raise ValueError("available browsers: %s." % fmt)
        try:
            if name.lower() in ["", "default"]:
                name = webbrowser.get().name
            else:
                name = webbrowser.get(name).name
        except:
            raise ValueError("Can't bind to «%s» browser" % name)
        return str.__new__(cls, name)

    def _raw_value(self):
        return super().__str__()

    def __call__(self):
        return self._raw_value()

    def __str__(self):
        if self:
            return colorize('%Cyan', self._raw_value())
        else:
            return colorize('%Cyan', "default")

    def open(self, url):
        browser = webbrowser.get(self)
        browser.open(url)
