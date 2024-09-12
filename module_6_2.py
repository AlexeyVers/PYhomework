class Vehicle:
    owner = str
    __model = str
    __engine_power = int
    __color = str
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        Vehicle.owner = str(owner)
        Vehicle.__model = str(__model)
        Vehicle.__color = str(__color)
        Vehicle.__engine_power = int(__engine_power)

    def get_model(self):
        return f'Модель авто - {Vehicle.__model}'

    def get_horsepower(self):
        return f'{Vehicle.__engine_power} - лошадок'

    def get_color(self):
        return f'Цвет - {Vehicle.__color}'

    def print_info(self):
        print(f'{Vehicle.get_model(self)} \n{Vehicle.get_horsepower(self)}'
              f'\n{Vehicle.get_color(self)} \n{self.owner}')


    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
                Vehicle.__color = new_color
        else:
            print('Нельзя сменить цвет на', new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
