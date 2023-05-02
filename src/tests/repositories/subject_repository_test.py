import unittest

from entities.subjects import Subjects
from repository.subject_repository import subject_repo
from repository.user_repository import user_repo
from entities.user import User

class TestSubjectRepository(unittest.TestCase):
    def setUp(self) -> None:
        user_repo.delete_all_users()
        self.user_muumi = User('Muumi', 'muumi123')
        self.user_nipsu = User('Nipsu', 'Nipsu123')
        subject_repo.delete_all()
        self.maths = Subjects('Maths', 'All')
        self.programming = Subjects('Programming', self.user_muumi.username)

    def test_new_subject(self):
        subject_repo.new_subject(self.maths)

        subjects = subject_repo.get_all()

        self.assertEqual(len(subjects), 1)

    def test_get_all_for_user(self):
        subject_repo.new_subject(self.maths)
        subject_repo.new_subject(self.programming)

        subjects = subject_repo.get_all_for_user(self.user_muumi.username)

        self.assertEqual(len(subjects), 1)

    def test_delete_subject(self):
        subject_repo.new_subject(self.programming)

        self.assertEqual(len(subject_repo.get_all()),1)

        subject_repo.delete_subject(self.programming)

        self.assertEqual(len(subject_repo.get_all()), 0)

    def test_delete_all(self):
        subject_repo.new_subject(self.maths)
        subject_repo.new_subject(self.programming)

        self.assertEqual(len(subject_repo.get_all()), 2)

        subject_repo.delete_all()

        self.assertEqual(len(subject_repo.get_all()), 0)