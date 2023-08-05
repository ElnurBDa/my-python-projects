
class Food:
    what_is_this = 'This is Food!'


class Fruit(Food):
    fruit_count = 0
    fruits_data = []

    @staticmethod
    def get_info():
        print('The fruits are so tasty!')
        print('There are ' + str(Fruit.fruit_count) + ' kinds of fruits.')

    def __str__(self):
        return 'This is Fruit class'

    def __init__(self):

        Fruit.fruit_count += 1
        self.__code=2*Fruit.fruit_count+7+Fruit.fruit_count**2

    def f_1(self, name, cost_per_kg, kg, color=''):
        self.name = name
        self.cost_per_kg = cost_per_kg
        self.kg = kg
        self.cost = round(cost_per_kg * kg, 5)
        self.color = color
        self.info = str(Fruit.fruit_count) + ') The ' + color + ' ' + name + ' costs per kg ' + str(
            cost_per_kg) + '.\nThere is ' + str(
            kg) + ' kg of ' + name + ' and it costs ' + str(self.cost) + ' .\n'
        code=self.__code
        Fruit.fruits_data.append((Fruit.fruit_count, name, color, cost_per_kg, kg, self.cost, self.info,code))





apple = Fruit()
apple.f_1('apple', .47, 3.67, 'red')
orange = Fruit()
orange.f_1('orange', .98, 6.7)
banana = Fruit()
banana.f_1('banana', 1.29, 2.13)
pear = Fruit()
pear.f_1('pear', .77, 4.11, 'green')
grape=Fruit()
grape.f_1('grape',1.3,12.3,'blue')