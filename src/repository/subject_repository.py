from entities.subjects import Subjects
from db import get_db_connection


def get_subjects_by_row(row):
    'Tapa saada aiheet rivi kerrallaan'
    return Subjects(row['subject'], row['username']) if row else None


class SubjectRepo:
    'Aiheitten tietokanta toiminnot'

    def __init__(self, conn):
        '''Luokan konstruktori
        args:
            conn: tietokantaan yhdistys
        '''
        self._conn = conn

    def new_subject(self, subject):
        '''Lisää uuden aiheen tietokantaan
        args:
            subject: Aihe luokka
        '''
        cur = self._conn.cursor()

        cur.execute('INSERT INTO subjects (subject, username) VALUES (?,?)',
                    (subject.subject, subject.username))

        self._conn.commit()

        return subject

    def get_all(self):
        'Hakee kaikki aiheet tietokannasta'

        cur = self._conn.cursor()

        cur.execute('SELECT * FROM subjects')

        rows = cur.fetchall()

        return list(map(get_subjects_by_row, rows))

    def get_all_for_user(self, username):
        '''Hakee kaikki yhden käyttäjän aiheet tietokannasta
        args:
            username: Käyttäjänimi
        '''
        cur = self._conn.cursor()

        cur.execute(
            '''SELECT * FROM subjects WHERE username = 'all' OR username = ?''',
            (username, )
        )

        rows = cur.fetchall()

        return list(map(get_subjects_by_row, rows))

    def delete_all(self):
        'Poistaa kaikki aiheet tietokannasta'
        cur = self._conn.cursor()

        cur.execute(
            'DELETE FROM subjects'
        )

        self._conn.commit()

    def delete_subject(self, subject):
        '''Poistaa yhden aiheen tietokannasta
        args:
            subject: Aihe luokka
        '''
        cur = self._conn.cursor()

        cur.execute(
            'DELETE FROM subjects WHERE subject = ? AND username = ?',
            (subject.subject, subject.username)
        )

        self._conn.commit()

        return subject


subject_repo = SubjectRepo(get_db_connection())
