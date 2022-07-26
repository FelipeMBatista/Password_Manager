# Password Generator Project
import random

class PasswordGenerator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't',
                        'u', 'v',
                        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                        'P',
                        'Q', 'R',
                        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def random_password_generator(self):
        password_list = [random.choice(self.letters) for char in range(random.randint(8, 10))]
        password_list += [random.choice(self.symbols) for char in range(random.randint(2, 4))]
        password_list += [random.choice(self.numbers) for char in range(random.randint(2, 4))]
        random.shuffle(password_list)

        password = "".join(password_list)

        return password