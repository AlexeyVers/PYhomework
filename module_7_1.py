from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        read_ = open(self.__file_name, 'r')
        product = read_.read()
        read_.close()
        return product

    def add(self, *products):
        current_products = self.get_products()
        write_ = open(self.__file_name, 'a')
        for i in products:
            if str(i) in current_products:
                current_products += str(i) + '\n'
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                write_.write(f'{i}\n')
        write_.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
