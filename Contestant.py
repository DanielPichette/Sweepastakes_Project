class Contestant:
    def __init__(self):
        self.first_name = input('first name: ')
        self.last_name = input('last name: ')
        self.email_address = input('email address: ')
        self.registration_number = int((input('registration number: ')))

    # member methods

    def notify(self):
        print('has been notified')
