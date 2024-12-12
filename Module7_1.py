
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')    #откроет файл txt
        f = file.read()                       # прочитает
        file.close()                          # закроет
        return f'\n{f}'                       # вернет строку с содержимым

    def add(self, *products):   #принимает на себя несколько объектов класса Product
        for i in products:      # берет каждый из них
            if str(i) not in self.get_products():    #проверяет, есть он в списке, список берет из функции
                file = open(self.__file_name, 'a')   # если продукта нет, открывает файл
                file.write(f'\n{i}')                 # добавляет новый объект
                file.close()                         # закрывает файл
            else:
                n = str(i).split(',')[0]             # это создание переменной, в которую записан только name экзепляра
                print(f'Продукт {n} уже есть в магазине')     #если уже был такой, то выдаст строку


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())




