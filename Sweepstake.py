import random

from Contestant import Contestant


class Sweepstake:
    def __init__(self):
        self.contestants = {}  # Dictionary
        self.name = input('what is the name of this sweepstakes?')

    # member methods
    def register_contestant(self, contestant):
        key = contestant.registration_number
        value = (contestant.first_name + contestant.last_name)
        return self.contestants.update({key: value})

    def pick_winner(self):
        list_of_contestants = list(self.contestants.items())
        winner = random.choice(list_of_contestants)
        return winner

    def print_contestant_info(self, contestant):
        print(contestant)


test = Sweepstake()
test.register_contestant(Contestant())
test.register_contestant(Contestant())
test.register_contestant(Contestant())
print(test.contestants)
