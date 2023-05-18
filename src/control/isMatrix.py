class isMatrix:
    def __init__(self, item):
        self.item = item

    def is_matrix(self):
        if isinstance(self.item, list):
            if all(isinstance(self.item, list) for i in self.item):
                return True
            else:
                return False

