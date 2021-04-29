from SweekpstakesStackManager import SweepstakesStackManger
from SweepstakesQueueManager import SweepstakesQueueManager
class MarketingFirmCreator:

    def choose_manager_type(self):
        choice = input("type '1' to use a Stack manager. type '2' to use a Queue manager")
        if choice == '1':
            return SweepstakesStackManger()
        if choice == '2':
            return SweepstakesQueueManager()
