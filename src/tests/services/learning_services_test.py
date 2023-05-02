import unittest

from entities.user import User
from entities.subjects import Subjects
from entities.questions import Question

from repository.user_repository import user_repo
from repository.subject_repository import subject_repo
from repository.question_repository import question_repo

from services.learning_services import learning_service

class LearningServicesTest(unittest.TestCase):
    def setUp(self) -> None:
        user_repo.delete_all_users()
        self.user_muumi = User('Muumi', 'muumi123')
        self.user_nipsu = User('Nipsu', 'Nipsu123')
        subject_repo.delete_all()
        self.maths = Subjects('Maths', 'All')
        self.prog = Subjects('Programming', self.user_muumi.username)
        question_repo.delete_all()
        self.oneplusone = Question('1+1', 'Maths', '2', 'Normal', 'All')
        self.twoplustwo = Question('2+2', 'Maths', '4', 'Normal', 'Nipsu')
        self.programming = Question(
            'One programming language', 'Programming', 'Python', 'Normal', 'Muumi')