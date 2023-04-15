import unittest

from entities.questions import Question
from repository.question_repository import question_repo
from repository.user_repository import user_repo
from entities.user import User

class TestQuestionsRepo(unittest.TestCase):
    def setUp(self) -> None:
        user_repo.delete_all_users()
        self.user_muumi = User('Muumi', 'muumi123')
        self.user_nipsu = User('Nipsu', 'Nipsu123')
        question_repo.delete_all()
        self.oneplusone = Question('1+1', 'Maths', '2', 'Normal', 'All')
        self.twoplustwo = Question('2+2', 'Maths', '4', 'Normal', 'Nipsu')
        self.programming = Question('One programming language', 'Programming', 'Python', 'Normal', 'Muumi')

    def test_new_question(self):
        question_repo.create(self.oneplusone)
        question_repo.create(self.twoplustwo)
        questions = question_repo.get_all()

        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0].question, '1+1')

    def test_delete_one_question(self):
        question_repo.create(self.oneplusone)
        question_repo.create(self.twoplustwo)
        questions = question_repo.get_all()

        self.assertEqual(len(questions), 2)

        question_repo.delete_one_question(self.oneplusone.question)

        uestions = question_repo.get_all()

        self.assertEqual(len(uestions), 1)

    def test_finds_correct_questions(self):
        question_repo.create(self.oneplusone)
        question_repo.create(self.twoplustwo)
        question_repo.create(self.programming)

        questions = question_repo.get_questions([self.user_nipsu.username, 'Maths', 2])

        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0].question, '2+2')