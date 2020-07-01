# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


class Dress:
    def __init__(self, name_closes, size):
        self.name_closes = name_closes
        self.size = size

    def __add__(self, other):
        return self.size + other.size

    def __str__(self):
        return f'Расход ткани на: {self.name_closes}: {self.size}м'


class Coat(Dress):
    @property
    def manufacture(self):
        self.size = self.size / 6.5 + 0.5
        return self.size


class Suit(Dress):
    @property
    def manufacture(self):
        self.size = 2 * self.size + 0.5
        return self.size


coat_1 = Coat('кожанное пальто', 52) #размер пальто
result = coat_1.manufacture
print(coat_1)

suit_1 = Suit('замшевый костюм', 1.7) #рост костюма
result_2 = suit_1.manufacture
print(suit_1)
