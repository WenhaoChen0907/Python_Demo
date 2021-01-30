class Person:

    def __init__(self, name, weight):

        self.name = name

        self.weight = weight

    def __str__(self):

        return "%s 的体重是 %.2f" % (self.name, self.weight)

    def run(self):

        self.weight -= 0.5

    def eat(self):

        self.weight += 1


xiaoming = Person("小明", 70.5)

xiaoming.run()
xiaoming.eat()

print(xiaoming)