class Question:
    'Luokka joka kuvaa yhtä kysymystä'

    def __init__(self, question, subject, answer, q_type, username):
        '''
        Luokan konstruktori
        args:
            question: Kysymys
            subject: Kysmyksen aihe
            answer: Vastaus kysymykseen
            q_type: Kysymyksen tyyppi
            username: Käyttäjä kenelle kysymys kuuluu
        '''
        self.question = question
        self.subject = subject
        self.answer = answer
        self.q_type = q_type
        self.username = username
