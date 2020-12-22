import random

class Robot():
    def __init__(self):
        self.used_names = []
        self.collision_count = 0
        self.random_name()
    
    def random_letters(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letters = random.choices(alphabet, k=2)
        return ''.join(letters)
        
    def random_numbers(self):
        n = str(random.randint(0,999))
        x = 3 - len(n)
        return (x * '0') + n

    def random_name(self):
        letters = self.random_letters()
        numbers = self.random_numbers()
        if (letters + numbers) not in self.used_names:
            self.name = letters + numbers
            self.used_names.append(self.name)
        else:
            self.collision_count += 1
            self.random_name()

    def reset(self):
        self.random_name()
