from entities.subjects import Subjects
from db import get_db_connection


def get_subjects_by_row(row):
    return Subjects(row['subject'], row['username']) if row else None


class SubjectRepo:
    def __init__(self, conn):
        self._conn = conn

    def new_subject(self, subject):
        cur = self._conn.cursor()

        cur.execute('INSERT INTO subjects (subject, username) VALUES (?,?)',
                    (subject.subject, subject.username))

        self._conn.commit()

        return subject

    def get_all(self):
        cur = self._conn.cursor()

        cur.execute('SELECT * FROM subjects')

        rows = cur.fetchall()

        return list(map(get_subjects_by_row, rows))

    def get_all_for_user(self, username):
        cur = self._conn.cursor()

        cur.execute(
            'SELECT * FROM subjects WHERE username = ? OR username = all',
            (username, )
        )

        rows = cur.fetchall()

        return list(map(get_subjects_by_row, rows))

    def delete_all(self):
        cur = self._conn.cursor()

        cur.execute(
            'DELETE FROM subjects'
        )

        self._conn.commit()

    def delete_subject(self, subject):
        cur = self._conn.cursor()

        cur.execute(
            'DELETE FROM subjects WHERE subject = ? AND username = ?',
            (subject.subject, subject.username)
        )

        self._conn.commit()

        return subject


subject_repo = SubjectRepo(get_db_connection())
