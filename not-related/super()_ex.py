class User:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print('do nothing')

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, number_arrows):
        super().__init__(name)
        self.number_arrows = number_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left {self.number_arrows}')


wizard = Wizard('Merlin', 50)
archer = Archer('Robin', 100)
wizard.attack()
archer.attack()


def player_atack(char):
    char.attack()


player_atack(wizard)
player_atack(archer)

for char in [wizard, archer]:
    char.attack()
