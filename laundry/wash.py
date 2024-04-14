class Wash:
    def __init__(self, clothes, duration):
        self.clothes = clothes
        self.duration = duration

    def __repr__(self):
        return str([self.clothes, self.duration])