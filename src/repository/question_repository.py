from entities.questions import Question
from db import get_db_connection


def get_question_by_row(row):
    'Tapa saada yksittäiset kysymykset listaan'
    return Question(row['question'], row['subject'],
                    row['answer'], row['q_type'],
                    row['username']) if row else None


class QuestionRepo:
    'Kysymys luokan tietokanta funktiot'
    def __init__(self, conn):
        '''
        Luokan konstruktori
        args:
            conn: Tietokantaan yhdistys
        '''
        self._conn = conn

    def create(self, question):
        '''
        Kysymyksen lisäys tietokantaan
        args:
            question: Kysymys luokka
        '''
        cur = self._conn.cursor()
        cur.execute(
            '''INSERT INTO questions (question, subject, answer, q_type, username) 
            VALUES (?, ?, ?, ?, ?)''',
            (question.question, question.subject,
             question.answer, question.q_type, question.username)
        )

        self._conn.commit()

        return question
    
    def get_all_for_one_user(self, user):
        '''Hakee kaikki kysymykset yhdelle käyttäjälle'''
        
        cur = self._conn.cursor()

        cur.execute(
            '''SELECT * FROM questions WHERE username = ? OR username = "All"''',
            (user, )
        )

        rows = cur.fetchall()

        return list(map(get_question_by_row, rows))

    def delete_one_question(self, question):
        '''
        Kysymyksen poisto tietokannasta
        args:
            question: Kysymys joka poistetaan
        '''
        cur = self._conn.cursor()
        cur.execute(
            'DELETE FROM questions WHERE question = ?',
            (question, )
        )
        self._conn.commit()

        return question

    def delete_all(self):
        'Poistaa kaikki kysymykset'
        cur = self._conn.cursor()

        cur.execute('DELETE FROM questions')

        self._conn.commit()

    def get_questions(self, info):
        '''Hakee halutun verran kysymyksiä tietokannasta
        args:
            info: Tietoa halutusta kysymyksestä
            
        returns:
            listan kysymys olioita
        '''
        cur = self._conn.cursor()
        cur.execute(
            f'''SELECT * FROM questions WHERE (username = ? OR username = 'All') 
            AND subject IN ({','.join(['?']*(len(info)-2))}) ORDER BY RANDOM() LIMIT ?''',
            info
        )
        rows = cur.fetchall()

        return list(map(get_question_by_row, rows))

    def get_all(self):
        'Hakee kaikki kysymykset tietokannasta'
        cur = self._conn.cursor()
        cur.execute('SELECT * FROM questions')
        rows = cur.fetchall()
        return list(map(get_question_by_row, rows))


question_repo = QuestionRepo(get_db_connection())
