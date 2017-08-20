import unittest

from pets import *

class Test_Pets(unittest.TestCase):

    def test_cats(self):
        cat = Cat(name = "Kitty", hates_dog = True)

        self.assertEqual("Kitty", cat.name)

    def test_cats_1(self):
        cat = Cat(name = "Kitty", hates_dog = True)

        self.assertEqual(True, cat.hates_dog)

    def test_cats_2(self):
        cat = "Meow, meow!!!"

        self.assertEqual("Meow, meow!!!", cat)

    def test_cats_3(self):
        cat = Cat(name = "Kitty", hates_dog = True)

        self.assertEqual("Kit", cat.name)

    def test_cats_4(self):
        cat = Cat(name = "Kitty", hates_dog = False)

        self.assertEqual(True, cat.hates_dog)

    def test_cats_5(self):
        cat = "Woof, woof!!!"

        self.assertEqual("Meow, meow!!!", cat)

    def test_dogs(self):
        dog = Dog(name = "Bars", chases_cats = True)

        self.assertEqual("Bars", dog.name)

    def test_dog_1(self):
        dog = Dog(name = "Bars", chases_cats = True)

        self.assertEqual(True, dog.chases_cats)

    def test_dog_2(self):
        dog = "Woof, woof!!!"

        self.assertEqual("Woof, woof!!!", dog)

    def test_dog_3(self):
        dog = Dog(name = "Bar", chases_cats = True)

        self.assertEqual("Bars", dog.name)

    def test_dog_4(self):
        dog = Dog(name = "Bars", chases_cats = False)

        self.assertEqual(True, dog.chases_cats)

    def test_dog_5(self):
        dog = "Eek, eek!!!"

        self.assertEqual("Woof, woof!!!", dog)

    def test_mouse(self):
        mouse = Mouse(name = "Jerry", like_cheese = True)

        self.assertEqual("Jerry", mouse.name)

    def test_mouse_1(self):
        mouse = Mouse(name = "Jerry", like_cheese = True)

        self.assertEqual(True, mouse.like_cheese)

    def test_mouse_2(self):
        mouse = "Eek, eek!!"

        self.assertEqual("Eek, eek!!!", mouse)

    def test_mouse_3(self):
        mouse = Mouse(name = "Jer", like_cheese = True)

        self.assertEqual("Jerry", mouse.name)

    def test_mouse_4(self):
        mouse = Mouse(name = "Jerry", like_cheese = False)

        self.assertEqual(True, mouse.like_cheese)

    def test_mouse_5(self):
        mouse = "Pi, pi!!!"

        self.assertEqual("Eek, eek!!!", mouse)

    def test_pet(self):
        pig = Pet(name = "Piggy", species = "pig")

        self.assertEqual("Piggy", pig.name)

    def test_pet_1(self):
        pig = Pet(name = "Piggy", species = "pig")

        self.assertEqual("pig", pig.species)

    def test_pet_2(self):
        pig = Pet(name = "Piggy", species = "pig")

        self.assertEqual("pig", pig.name)

    def test_pet_2(self):
        pig = Pet(name = "Piggy", species = "pig")

        self.assertEqual("jig", pig.species)


if __name__=='__main__':
    unittest.main()
