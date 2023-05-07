from entities.user import User
from entities.subjects import Subjects
from entities.questions import Question

from repository.user_repository import (
    user_repo as default_user_repo
)

from repository.subject_repository import (
    subject_repo as default_subject_repo
)

from repository.question_repository import (
    question_repo as default_question_repo
)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class QuestionExistserror(Exception):
    pass


class NoSubjectsChosenError(Exception):
    pass


class LearningService:
    'Sovelluksen logiikka'
    def __init__(
            self,
            user_repo=default_user_repo,
            subject_repo=default_subject_repo,
            question_repo=default_question_repo
    ):
        self._user = None
        self._user_repo = user_repo
        self._subject_repo = subject_repo
        self._question_repo = question_repo
        self._chosen_subjects = []
        self._questions = []
        self._results = []

    def default_questions(self):
        'Lisää tietokantaan alustavat tiedot'
        try:
            self._subject_repo.new_subject(
                Subjects('Maths', 'all'))
            self._subject_repo.new_subject(
                Subjects('Physics', 'all'))
            self._subject_repo.new_subject(
                Subjects('Programming', 'all'))

            self._question_repo.create(
                Question('What is 1+1', 'Maths', '2',
                         'Text', 'All'))
            self._question_repo.create(
                Question('Derive x: x^2+x+1', 'Maths',
                         '2x+1', 'Text', 'All'))
            self._question_repo.create(
                Question('Solve x: 5x+5=5', 'Maths',
                         'x=0', 'Text', 'All'))

            self._question_repo.create(Question(
                'What is the gravitational acceleration of the earth?',
                'Physics', '9,81m/s^2', 'Text', 'All'))
            self._question_repo.create(Question(
                'What is the unit for energy?', 'Physics', 'Joule (J)', 'Text', 'All'))
            self._question_repo.create(Question('What are the two main components of a generator?',
                                                'Physics', 'A coil and a magnet', 'Text', 'All'))

            self._question_repo.create(Question(
                'What is the timecomplexity of a for loop?',
                'Programming', 'O(n)', 'Text', 'All'))
            self._question_repo.create(Question(
                'Name 3 programming languages', 'Programming',
                'Python, Java, C++', 'Text', 'All'))
            self._question_repo.create(Question(
                'What is a käpistelijä?', 'Programming',
                'CS student', 'Text', 'All'))
        except:
            pass

    def login(self, username, password):
        '''Kirjaa käyttäjän sisään
        args:
            username: käyttäjänimi
            password: salasana
        '''
        user = self._user_repo.find_one_user(username)

        if not user or user.password != password: #Tarkistaa onko salasana ja käyttäjänimi oikein
            raise InvalidCredentialsError('Invalid username or password!')

        self._user = user

        return user

    def add_subject_to_list(self, subject, check):
        '''Lisää aiheen valittujen aiheitten listaan
        args:
            subject: Aihe
            check: Tarkistus onko aihe jo listassa vai ei
        '''
        if check:
            self._chosen_subjects.append(subject)
        if not check and subject in self._chosen_subjects:
            self._chosen_subjects.remove(subject)
        return subject

    def get_current_user(self):
        'Palauttaa nykyisen käyttäjän'
        return self._user

    def get_users(self):
        'Palauttaa kaikki käyttäjät'
        return self._user_repo.find_all()

    def get_subjects(self):
        'Palauttaa kaikki nykyisen käyttäjän aiheet'
        return self._subject_repo.get_all_for_user(self._user.username)

    def logout(self):
        'Kirjaa käyttäjän ulos'
        self._user = None

    def create_user(self, username, password, login=True):
        '''Lisää käyttäjän tietokantaan
        args: 
            username: Käyttäjänimi
            password: Salsana
            login: Kirjataanko käyttäjä sisään vai ei
        '''
        existing_user = self._user_repo.find_one_user(username)

        if existing_user:
            raise UsernameExistsError(f'Username {username} already exists')

        user = self._user_repo.new_user(User(username, password))

        if login:
            self._user = user

        return user
    
    def get_all_questions(self):
        'Palauttaa kaikki kysymykset tietokannasta'

        all_q = self._question_repo.get_all_for_one_user(self.get_current_user().username)

        return all_q
    
    def delete_question(self, question):
        self._question_repo.delete_one_question(question)

    def add_question(self, question, subject, q_type, answer):
        '''Lisää kysymyksen tietokantaan
        args:
            question: Kysymys
            subject: Kysmyksen aihe
            q_type: Kysmyksen tyyppi
            answer: Vastaus kysymykseen
        '''
        all_q = self._question_repo.get_all()

        if Question(question, subject, answer, q_type, self._user.username) in all_q:
            raise QuestionExistserror('Question already exists')

        question = self._question_repo.create(
            Question(question, subject, answer, q_type, self._user.username))

        return question

    def get_questions(self, amount):
        '''Palauttaa halutun määrän kysymyksiä
        args:
            amount: Haluttu määrä kysymyksiä
        '''
        if not self._chosen_subjects:
            raise NoSubjectsChosenError('You have not chosen any subjects!')

        info = [self._user.username]
        for i in self._chosen_subjects:
            info.append(i)
        info.append(amount)

        self._questions = self._question_repo.get_questions(info)
        return self._questions

    def get_current_questions(self):
        'Palauttaa nykyiset kysymykset'
        return self._questions

    def result(self, subject, question, answer):
        '''Lisää tuloksen listaan
        args:
            subject: Aihe
            question: Kysymys
            answer: Tulos
        '''
        self._results.append([subject, question, answer])

    def reset_results(self):
        'Tyhjentää tulos listan'
        self._results = []

    def reset_subjects(self):
        'Tyhjentää aihe listan'
        self._chosen_subjects = []

    def reset_questions(self):
        'Tyhjentää kysymys listan'
        self._questions = []

    def get_results(self):
        'Palauttaa tulos listan'
        return self._results


learning_service = LearningService()
