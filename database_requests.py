import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tm.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Отримати всі завдання певного користувача.
sql = "SELECT * FROM users WHERE id = 32"
print(execute_query(sql))

#Вибрати завдання за певним статусом.
sql = "SELECT * FROM tasks WHERE status_id=1"
print(execute_query(sql))
sql = "SELECT * FROM tasks INNER JOIN status on tasks.status_id=status.id WHERE status.name='new'"
print(execute_query(sql))

#Оновити статус конкретного завдання.
sql = "UPDATE tasks SET status_id=2 WHERE id=5"
execute_query(sql)

#Отримати список користувачів, які не мають жодного завдання.
sql = "SELECT * FROM users where id NOT IN (SELECT tasks.user_id FROM tasks)"
print(execute_query(sql))

#Додати нове завдання для конкретного користувача.
sql = "INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New task for user','Do some work',1,22)"
execute_query(sql)

#Отримати всі завдання, які ще не завершено.
sql = "SELECT * FROM tasks WHERE status_id <> 3"
print(execute_query(sql))

#Видалити конкретне завдання.
sql = "DELETE FROM tasks WHERE id=6"
execute_query(sql)

#Знайти користувачів з певною електронною поштою.
sql = "SELECT * FROM users WHERE email LIKE 'example@test.com'"
print(execute_query(sql))

#Оновити ім'я користувача.
sql = "UPDATE users set fullname = 'John Doe' WHERE id=1"
execute_query(sql)

#Отримати кількість завдань для кожного статусу.
sql = """SELECT name as Status,COUNT(t.id) as Number_of_tasks from status s
    LEFT join tasks t on s.id = t.status_id  GROUP  by t.status_id,s.id ORDER by s.id"""
print(execute_query(sql))

#Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
sql = "SELECT t.* FROM tasks t INNER JOIN users u ON t.user_id = u.id WHERE u.email LIKE '%example.org'"
print(execute_query(sql))

#Отримати список завдань, що не мають опису.
sql = "SELECT * FROM tasks WHERE description IS NULL"
print(execute_query(sql))

#Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
sql = "SELECT * FROM users u INNER JOIN tasks t ON u.id = t.user_id WHERE t.status_id = 2 ORDER BY u.id"
print(execute_query(sql))

#Отримати користувачів та кількість їхніх завдань.
sql = "SELECT u.*,COUNT(t.id) AS Number_of_tasks FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY t.user_id"
print(execute_query(sql))