import csv

from laundry.laundry import Laundry


class LaundryFactory:

    @staticmethod
    def Load(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            next(reader)
            next(reader)
            row2 = next(reader)

            quantity_clothes = int(row2[2])
            quantity_incompatibilities = int(row2[3])
            wash = Laundry(quantity_incompatibilities, quantity_clothes)

            for row in reader:
                if row[0] == 'e':
                    wash.add_incompatibilities(int(row[1]), int(row[2]))
                if row[0] == 'n':
                    wash.add_clothes(int(row[1]), int(row[2]))

        file.close()

        return wash

    @staticmethod
    def output(washes, output_file):
        washes_formated = []
        j = 0
        total = 0
        for wash in washes:
            j += 1
            total += wash[1]
            for i in wash[0]:
                washes_formated.append([i,j])

        with open(output_file, "w", newline='') as file:
            writer = csv.writer(file, delimiter=' ')
            writer.writerows(washes_formated)

        file.close()

