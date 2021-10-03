class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(self.name + " bird can fly")

    def walk(self):
        print(self.name + " can walk")

    def __str__(self):
        return self.name + " bird can walk"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="seed"):
        super(NonFlyingBird, self).__init__(name)
        self.ration = ration

    def swim(self):
        print(self.name + " can swim")

    def eat(self):
        print(self.name + " eats mostly " + self.ration)

    def fly(self):
        raise AttributeError("NonFlyingBird cannot fly!")

    def __str__(self):
        return self.name + " can walk and swim"


class FlyingBird(Bird):
    def __init__(self, name, ration="seed"):
        super(FlyingBird, self).__init__(name)
        self.ration = ration

    def swim(self):
        print(self.name + " can swim")

    def eat(self):
        print(self.name + " eats mostly " + self.ration)

    def __str__(self):
        return self.name + " can fly, walk and swim"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration):
        FlyingBird.__init__(self, name, ration)
        NonFlyingBird.__init__(self, name, ration)

    def fly(self):
        return Bird.fly(self)


print(SuperBird.mro())
b = NonFlyingBird("d")
b.swim()
s = SuperBird("Igor Grom", "shawarma")
s.fly()
s.swim()
s.walk()
b.fly() # error
