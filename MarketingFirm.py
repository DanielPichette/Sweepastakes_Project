from Sweepstake import Sweepstake
from SweepstakesQueueManager import SweepstakesQueueManager
from SweekpstakesStackManager import SweepstakesStackManger


class MarketingFirm:
    def __init__(self, manager):
        self.manager: manager  # DEPENDENCY INJECTION : allows various outcomes without having to change the code.

    # member methods
    def create_sweepstakes(self):
        sweepstakes = Sweepstake()
        return sweepstakes
