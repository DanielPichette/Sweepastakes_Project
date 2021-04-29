from Sweepstake import Sweepstake
from MarketingFirmCreator import MarketingFirmCreator

class MarketingFirm:
    def __init__(self, manager):
        self.manager: MarketingFirmCreator.choose_manager_type()
        # DEPENDENCY INJECTION : allows various outcomes without having to change the code.

    # member methods
    def create_sweepstakes(self):
        sweepstakes = Sweepstake()
        return sweepstakes
