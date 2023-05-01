class Subjects:
    'Luokka joka kuvaa yhtä aihetta'
    def __init__(self, subject, username):
        '''Luokan konstruktori,
            args:
                subject: Aiheen nimi
                username: Kenelle aihe kuuluu
        '''
        self.subject = subject
        self.username = username
