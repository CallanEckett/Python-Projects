class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.raw = name.strip().lower()

        self.value = value