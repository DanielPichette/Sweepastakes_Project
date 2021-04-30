from MarketingFirmCreator import MarketingFirmCreator
from MarketingFirm import MarketingFirm


def run_simulation():
    manager = MarketingFirmCreator.choose_manager_type()
    marketing = MarketingFirm(manager)
    return marketing

