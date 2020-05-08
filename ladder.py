class Ladder:
    amount_of_ladders = 0

    def __init__(self, producer="Intertool", max_length_in_metres=5, max_load=150, width=40, mass_in_kilograms=4,
                 material="aluminum", warranty_in_years=7):
        self.producer = producer
        self.max_length_in_metres = max_length_in_metres
        self.max_load = max_load
        self.material = material
        self.width = width
        self.mass_in_kilograms = mass_in_kilograms
        self.warranty_in_years = warranty_in_years
        Ladder.amount_of_ladders += 1

    def __del__(self):
        "ladder deleted"

    def __str__(self):
        return self.producer + ', ' + str(self.max_length_in_metres) + ', ' + str(
            self.max_load) + ', ' + self.material + ', ' + str(self.width) + ', ' + str(
            self.mass_in_kilograms) + ', ' + str(self.warranty_in_years)

    @staticmethod
    def get_amount_of_ladders():
        return Ladder.amount_of_ladders


if __name__ == "__main__":
    first_ladder = Ladder('Dnipro-m', 3, 120)
    second_ladder = Ladder('Forte', 4, 140, 30, 5, 'iron', 10)
    third_ladder = Ladder()

    print('First ladder:', first_ladder)
    print('Second ladder:', second_ladder)
    print('Third ladder:', third_ladder)
    print('\nAmount of ladders:', Ladder.get_amount_of_ladders())
