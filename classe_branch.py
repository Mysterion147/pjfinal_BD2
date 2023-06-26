class Branch:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.corp = None

    def set_corp(self, corp):
        self.corp = corp