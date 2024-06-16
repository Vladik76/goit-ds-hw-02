from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 50
NUMBER_TASKS = 300
STATUSES = [('new',), ('in progress',), ('completed',)]


def generate_unique_email(emails):
    while True:
        email = faker.Faker().email()
        if email not in emails:
            return email


def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []
    fake_tasks = []
    fake_emails = []

    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append(fake_data.name())

    for _ in range(number_users):
        fake_emails.append(generate_unique_email(fake_emails))  #Faker may generate duplicates !!!

    for _ in range(number_tasks):
        fake_tasks.append(fake_data.sentence(nb_words=4))

    return fake_users, fake_emails, fake_tasks


def prepare_data(users, emails, tasks) -> tuple():
    for_users = []

    for user in users:
        for_users.append((user, emails[len(for_users)]))

    for_tasks = []
    for task in tasks:
        for_tasks.append((task, task + " Description", randint(1, 3), randint(1, NUMBER_USERS)))

    return for_users, for_tasks


def insert_data_to_db(users, tasks) -> None:
    with sqlite3.connect('tm.db') as con:
        cur = con.cursor()

        sql_to_status = """
        INSERT INTO status (name) VALUES (?)
        """
        cur.executemany(sql_to_status, STATUSES)

        sql_to_user = """
        INSERT INTO users (fullname,email) VALUES (?,?)
        """
        cur.executemany(sql_to_user, users)

        sql_to_task = """
        INSERT INTO tasks (title, description, status_id,user_id) VALUES(?,?,?,?)
        """

        cur.executemany(sql_to_task, tasks)
        con.commit()


insert_data_to_db(*prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS)))
