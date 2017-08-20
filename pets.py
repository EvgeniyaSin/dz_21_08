class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return "{} is a {}".format(self.name, self.species)


class Dog(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, 'dog')
        self.chases_cats = chases_cats

    def is_chases_cats(self):
        return self.chases_cats

    def say_smth(self):
        print "Woof, woof!!!"


class Cat(Pet):
    def __init__(self, name, hates_dog):
        Pet.__init__(self, name, 'cat')
        self.hates_dog = hates_dog

    def is_hates_dog(self):
        return self.hates_dog

    def say_smth(self):
        print "Meow, meow!!!"


class Mouse(Pet):
    def __init__(self, name, like_cheese):
        Pet.__init__(self, name, 'mouse')
        self.like_cheese = like_cheese

    def is_like_cheese(self):
        return self.like_cheese

    def say_smth(self):
        print  "Eek, eek!!!"
