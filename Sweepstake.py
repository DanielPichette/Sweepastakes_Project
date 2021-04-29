import random

from Contestant import Contestant


class Sweepstake:
    def __init__(self):
        self.contestants: {}
        self.name: input('what is the name of this sweepstakes?')

    # member methods
    def register_contestant(self, contestant):
        self.contestants[contestant.registration_number] = (contestant.first_name + ' ' + contestant.last_name)

    def pick_winner(self):
        list_of_contestants = list(self.contestants.items())
        winner = random.choice(list_of_contestants)
        return winner

    def print_contestant_info(self, contestant):
        print(contestant)
