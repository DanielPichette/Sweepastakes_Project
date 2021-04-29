class Contestant:
    def __init__(self):
        self.first_name: None
        self.last_name: None
        self.email_address: None
        self.registration_number: None
# member methods

    def notify(self):
        print('has been notified')

    def create_contestant(self):
        self.first_name: input('first name: ')
        self.last_name: input('last name: ')
        self.email_address: input('email address: ')
        self.registration_number: input('registration number: ')
