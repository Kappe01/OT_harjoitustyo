from entities.questions import Question
from db import get_db_connection

def get_question_by_row(row):
    return Question(row['question'], row['subject'], 
                    row['answer'], row['q_type'], 
                    row['username']) if row else None

class QuestionRepo:
    def __init__(self, conn):
        self._conn = conn

    def create(self, question):
        cur = self._conn.cursor()
        cur.execute(
            'INSERT INTO questions (question, subject, answer, q_type, username) VALUES (?, ?, ?, ?, ?)',
            (question.question, question.subject, question.answer, question.q_type, question.username)
        )

        self._conn.commit()

        return question

    def delete_one_question(self, question):
        cur = self._conn.cursor()
        cur.execute(
            'DELETE FROM questions WHERE question = ?',
            (question)
        )
        self._conn.commit()

        return question

    def delete_all(self):
        cur = self._conn.cursor()

        cur.execute('DELETE FROM questions')

        self._conn.commit()

    

question_repo = QuestionRepo(get_db_connection())