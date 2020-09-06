import random

class RandomChar:
    def __init__(self):
        self.all_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.all_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        self.all_digits = '0123456789'
        self.all_specials = '~!@#$%^&*'
    
    def pick_random_item(self, sequence):
        random_int = random.randint(0, len(sequence) - 1)
        return sequence[random_int]

    def uppercase(self):
        return self.pick_random_item(self.all_uppercase)

    def lowercase(self):
        return self.pick_random_item(self.all_lowercase)

    def digit(self):
        return self.pick_random_item(self.all_digits)

    def special(self):
        return self.pick_random_item(self.all_specials)

    def anyone(self):
        return self.pick_random_item(self.all_uppercase + self.all_lowercase + self.all_digits + self.all_specials)

