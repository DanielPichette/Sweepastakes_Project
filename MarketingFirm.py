from Sweepstake import Sweepstake


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager
        # DEPENDENCY INJECTION : allows various outcomes without having to change the code.
        self.sweepstakes = None

    # member methods
    def create_sweepstakes(self):
        self.sweepstakes = Sweepstake()

    create_sweepstakes()