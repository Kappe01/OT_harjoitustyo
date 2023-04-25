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

class LearningService:
    def __init__(
            self,
            user_repo = default_user_repo,
            subject_repo = default_subject_repo,
            question_repo = default_question_repo
    ):
        self._user = None
        self._user_repo = user_repo
        self._subject_repo = subject_repo
        self._question_repo = question_repo
        self._chosen_subjects = []

        self.default_questions()

    def default_questions(self):
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

        user = self._user_repo.find_one_user(username)

        if not user or user.password != password:
            raise InvalidCredentialsError('Invalid username or password!')
        
        self._user = user

        return user
    
    def add_subject_to_list(self, subject, check):
        if check:
            self._chosen_subjects.append(subject)
        if not check and subject in self._chosen_subjects:
            self._chosen_subjects.remove(subject)
        return subject

    def get_current_user(self):
        return self._user
    
    def get_users(self):
        return self._user_repo.find_all()
    
    def get_subjects(self):
        return self._subject_repo.get_all_for_user(self._user.username)
    
    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):
        existing_user = self._user_repo.find_one_user(username)

        if existing_user:
            raise UsernameExistsError(f'Username {username} already exists')
        
        user = self._user_repo.new_user(User(username, password))

        if login:
            self._user = user

        return user
    
    def add_question(self, question, subject, q_type, answer):
        try:
            question = self._question_repo.create(Question(question, subject, answer, q_type, self._user.username))
        except:
            raise QuestionExistserror(f'Question already exists')
        return question

learning_service = LearningService()