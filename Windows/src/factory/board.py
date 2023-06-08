class Board:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance=super(Board, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.width = 8
        self.height = 8

        for i in range(self.width):
            self.matrix = [["none" for _ in range(self.width)]
                           for _ in range(self.height)]
