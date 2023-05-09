from entities.user import User
from db import get_db_connection


def get_user_by_row(row):
    'Tapa saada käyttäjät riveittäin'
    return User(row['username'], row['password']) if row else None


class UserRepo:
    'Käyttäjä luokan tietokanta toiminnot'

    def __init__(self, conn):
        '''Luokan konstruktori
        args:
            conn: Tietokantaan yhdistys
        '''
        self._conn = conn

    def new_user(self, user):
        '''Lisää uuden käyttäjän tietokantaan
        args:
            user: Käyttäjä luokka
        '''
        cur = self._conn.cursor()

        cur.execute('''
        INSERT INTO users (username, password) VALUES (?,?)''',
                    (user.username, user.password))

        self._conn.commit()

        return user

    def find_all(self):
        'Hakee kaikki käyttäjät tietokannasta'
        cur = self._conn.cursor()

        cur.execute('SELECT * FROM users')

        rows = cur.fetchall()

        return list(map(get_user_by_row, rows))

    def find_one_user(self, user):
        '''Hakee yhden käyttäjän tietokannasta
        args:
            user: Käyttäjätunnus
        '''
        cur = self._conn.cursor()

        cur.execute('SELECT * FROM users WHERE username = ?',
                    (user, ))

        row = cur.fetchone()

        return get_user_by_row(row)

    def delete_one_user(self, username):
        '''Poistaa käyttäjän tietokannasta
        args:
            username: Käyttäjätunnus
        '''
        cur = self._conn.cursor()

        cur.execute('DELETE FROM users WHERE username = ?',
                    (username, ))

        self._conn.commit()

        return username

    def delete_all_users(self):
        'Poistaa kaikki käyttäjät tietokannasta'
        cur = self._conn.cursor()

        cur.execute('DELETE FROM users')

        self._conn.commit()


user_repo = UserRepo(get_db_connection())
