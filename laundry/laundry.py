from laundry.clothe import Clothe


class Laundry:

    def __init__(self, quantity_incompatibilities, quantity_clothes):
        self.quantity_incompatibilities = quantity_incompatibilities
        self.incompatibilities = {}
        self.compatibilities = {}
        self.quantity_clothes = quantity_clothes
        self.clothes = []

    def add_incompatibilities(self, id_clothe1, id_clothe2):
        if id_clothe1 not in self.incompatibilities:
            self.incompatibilities[id_clothe1] = []

        self.incompatibilities[id_clothe1].append(id_clothe2)

    def remove_incompatibilities(self, id_clothe1, id_clothe2):
        self.compatibilities[id_clothe1].remove(id_clothe2)

    def add_clothes(self, id, duration):
        self.clothes.append(Clothe(id, duration))

    def add_all_clothes(self, id):
        allClothes = [i for i in range(self.quantity_clothes+1)]
        allClothes.remove(0)
        self.compatibilities[id] = allClothes
