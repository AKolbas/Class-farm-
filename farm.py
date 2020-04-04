class Animal():
    def __init__(self, kind, name, voice, weight):
        """Инициализируем вид и имя животного"""
        self.kind = kind
        self.name = name
        self.voice = voice
        self.weight = weight

    def description_name(self):
        """Выводим вид и имя животного"""
        desc = self.kind + ' ' + self.name
        print(desc)

    def eat(self):
        """Животное ест"""
        print(self.kind + ' ' + self.name + " ест")

    def voice_of_animal(self):
        """Животное говорит"""
        print("говорит" + ' ' + self.voice)

    def weight_of_animal(self):
        print(str(self.weight) + " " + 'kg')

class Eggs():
    """Собираем яйца у птиц"""
    def __init__(self, eggs=0):
        self.eggs = eggs
        #print('Собрали яйца')
    def description_eggs(self):
        print('Собрали ' + str(self.eggs) + ' яиц')


class Goose(Animal):

    def __init__(self, kind, name, voice, weight):
        super().__init__(kind, name, voice, weight)
        self.eggs = Eggs(15)

goose_1 = Goose('гусь', 'Серый', 'Гага', 5)
goose_2 = Goose('гусь', 'Белый', 'Гага', 8)

class Milk():
    """Доение животных"""
    def __init__(self, milk=0):
       self.milk = milk
    def description_milk(self):
        print('Надоили ' + str(self.milk) + ' литров молока')

class Cow(Animal):
    def __init__(self, kind, name, voice, weight):
        super().__init__(kind, name, voice, weight)
        self.milk = Milk(20)

cow = Cow('корова', 'Манька', 'Му', 500)

#cow.milk()
#cow.weight_of_animal()

class Sheep(Animal):

    def __init__(self, kind, name, voice, weight):
        super().__init__(kind, name, voice, weight)
    def cut(self):
        print('Овцу подстригли!')

sheep_1 = Sheep('овца', 'Барашек', 'Ме-ме', 50)
sheep_2 = Goose('овца', 'Кударявый', 'Ме-ме', 55)

#cow.milk.description_milk()

class Chicken(Animal):

    def __init__(self, kind, name, voice, weight):
        super().__init__(kind, name, voice, weight)
        self.eggs = Eggs(10)

chicken_1 = Chicken('курица', 'Ко-ко', 'куд-куда', 5)
chicken_2 = Chicken('курица', 'Кукареку', 'куд-куда', 5)

class Coat(Animal):
    def __init__(self, kind, name, voice, weight):
        super().__init__(kind, name, voice, weight)
        self.milk = Milk(10)

coat_1 = Coat('коза', 'Рога', 'бе', '40')
coat_2 = Coat('коза', 'Копыта', 'бе', '45')
#coat_2.milk.description_milk()

class Duck(Animal):
    def __init__(self, kind, name, voice, weight):
        super().__init__(kind, name, voice, weight)

duck_1 = Duck('утка', 'Кряква', 'кря', '5')

animal_list = {'гусь_1': 5, 'гусь_2': 8, 'корова': 500, 'овца_1': 50, 'овца': 55, 'курица_1': 5, 'курица_2': 5,
               'коза_1': 40, 'коза_2': 40, 'утка': 5}
#animal_list = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, coat_1, coat_2, duck_1]

def sum_weight():
    sum_w = 0
    for i in animal_list.values():
        sum_w += i
    print('Общий вес всех животных: ' + str(sum_w) + ' kg')

sum_weight()
print(type(animal_list))

def max_weight():
    #animal_weight_list = []
    x = max(list(animal_list.values()))
    print(x)
    for animal, weight in animal_list.items():
        if weight == x:
            print(f'Больше всех весит {animal} - {weight} кг')

#max_weight()








