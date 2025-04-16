class Dog:

    def sound(self):
        return "waw waw"
    
class Cat:

    def sound(self):
        return "meow meow"


def sound_catcher(objcet):
    return objcet.sound()

dog = Dog()
cat = Cat()

print(sound_catcher(dog))
print(sound_catcher(cat))