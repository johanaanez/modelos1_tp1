def is_present_in_any_wash(clothe, washes):
    is_present = False

    for wash in washes:
        if clothe in wash[0]:
            is_present = True
    return is_present


def is_compatible_with_wash(incompatibilities, incompatibility, wash):
    is_compatible = True
    for i in wash:
        if (i in incompatibilities.keys() and (incompatibility in incompatibilities[i])) or (
                incompatibility in incompatibilities.keys() and (i in incompatibilities[incompatibility])):
            is_compatible = False
    return is_compatible


def is_compatible_with_wash2(compatibilities, incompatibility, wash):
    is_compatible = True
    for i in wash:
        if (incompatibility not in compatibilities[i]) or (i not in compatibilities[incompatibility]):
            is_compatible = False
    return is_compatible


def are_compatibles(clothe, incompatibility, incompatibilities, wash):
    return clothe != incompatibility and is_compatible_with_wash(incompatibilities, incompatibility, wash)


def are_compatibles2(clothe, compatibility, compatibilities, wash):
    return clothe != compatibility and is_compatible_with_wash2(compatibilities, compatibility, wash)


def print_time(washes):
    total_time = 0
    for wash in washes:
        total_time += wash[1]

    print("Washes quantity: ", len(washes))
    print("Washes time: ", total_time)


class LaundryManager:

    def __init__(self, laundry):
        self.laundry = laundry

    def apply_ordered(self):
        washes = []
        self.laundry.clothes = sorted(self.laundry.clothes, key=lambda x: getattr(x, 'duration'), reverse=True)

        for i in range(len(self.laundry.clothes)):
            clothe1 = self.laundry.clothes[i]
            if not is_present_in_any_wash(clothe1.id, washes):
                wash = [clothe1.id]

                for j in range(i + 1, len(self.laundry.clothes)):
                    clothe2 = self.laundry.clothes[j]
                    if are_compatibles(clothe1.id, clothe2.id, self.laundry.incompatibilities,
                                       wash) and not is_present_in_any_wash(clothe2.id, washes):
                        wash.append(clothe2.id)

                if len(wash) > 0:
                    durations = list(
                        map(lambda k: k.duration, list(filter(lambda x: x.id in wash, self.laundry.clothes))))
                    max_duration = max(durations)
                    washes.append([wash, max_duration])

        print_time(washes)
        return washes
