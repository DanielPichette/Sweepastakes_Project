from data_stack import Stack


class SweepstakesStackManger:
    def __init__(self):
        self.stack: Stack()

    # member methods
    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)

    def get_sweepstakes(self):
        self.stack.pop()

