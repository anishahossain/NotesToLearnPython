class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')


class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')
        print(f'   Annual: {self.is_annual}')
        print(f'   Color of flowers: {self.color_of_flowers}')


def print_list(my_garden):
    for items in range(len(my_garden)):
        print(f'Plant {items + 1} Information:')
        my_garden[items].print_info()
        print('')
# TODO:  Define the print_list() function that prints a list of plant (or flower) objects

if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []
    user_string = input()

    while user_string != '-1':
        list_items = user_string.split(' ')
        if list_items[0] == 'plant':
            plant_name = list_items[1]
            plant_cost = list_items[2]
            pl = Plant(plant_name, plant_cost)
            my_garden.append(pl)
        elif list_items[0] == 'flower':
            plant_name = list_items[1]
            plant_cost = list_items[2]
            is_annual = list_items[3]
            color_of_flowers = list_items[4]
            fl = Flower(plant_name, plant_cost, is_annual, color_of_flowers)
            my_garden.append(fl)

        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        user_string = input()
    print_list(my_garden)
    # TODO: Call the print_list() function to print my_garden
