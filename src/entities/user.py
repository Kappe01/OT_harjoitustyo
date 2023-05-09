class User:
    'Yksittäistä käyttäjää kuvaava luokka'

    def __init__(self, username, password):
        '''
        args:
            username: Käyttäjän tunnus
            password: Käyttäjän salsana
        '''
        self.username = username
        self.password = password
