class NumberSet:
    """ NumberSet class to hold 2 numbers. """
    
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
    
t = NumberSet(6, 10)

class Animal:
    """ Animal Class. """

    def __init__(self, initX, initY):

        self.arms = initX
        self.legs = initY

    def limbs(self):
        return self.arms + self.legs

spider = Animal(4, 4)
spidlimbs = spider.limbs()

class Cereal:
    def __init__(self, s1, s2, n1):
        self.name = s1
        self.brand = s2
        self.fiber = n1
    def __str__(self):
        return '{} cereal is produced by {} and has {} grams of fiber in every serving!'.format(self.name, self.brand, self.fiber)
c1 = Cereal('Corn Flakes', "Kellogg's", 2)
c2 = Cereal('Honey Nut Cheerios', 'General Mills', 3)
print(c1)
print(c2)