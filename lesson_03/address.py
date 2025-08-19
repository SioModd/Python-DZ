class Address:
    def __init__(self, index, gorod, uliza, dom, kvartira):
        self.index = index
        self.gorod = gorod
        self.uliza = uliza
        self.dom = dom
        self.kvartira = kvartira

    def __str__(self):
            return f"{self.index}, {self.gorod}, {self.uliza}, {self.dom} - {self.kvartira}"