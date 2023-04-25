import unittest
from entities.user import User
from repository.user_repository import user_repo


class TestUserRepo(unittest.TestCase):
    def setUp(self) -> None:
        user_repo.delete_all_users()
        self.user_muumi = User('Muumi', 'muumi123')
        self.user_nipsu = User('Nipsu', 'Nipsu123')

    def test_new_user(self):
        user_repo.new_user(self.user_nipsu)
        user_repo.new_user(self.user_muumi)
        users = user_repo.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_nipsu.username)

    def test_delete_one_user(self):
        user_repo.new_user(self.user_muumi)
        users = user_repo.find_all()
        self.assertEqual(len(users), 1)

        user_repo.delete_one_user(self.user_muumi.username)

        users = user_repo.find_all()
        self.assertEqual(len(users), 0)

    def test_find_one_user(self):
        user_repo.new_user(self.user_nipsu)

        user = user_repo.find_one_user(
            self.user_nipsu.username)

        self.assertEqual(user.username, self.user_nipsu.username)
