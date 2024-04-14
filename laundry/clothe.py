class Clothe:
    def __init__(self, id_wash, duration):
        self.id = id_wash
        self.duration = duration

    def __repr__(self):
        return str([self.id, self.duration])