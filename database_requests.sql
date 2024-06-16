--Отримати всі завдання певного користувача.
SELECT * FROM users WHERE id = 32;

--Вибрати завдання за певним статусом.
SELECT * FROM tasks WHERE status_id=1;
SELECT * FROM tasks INNER JOIN status on tasks.status_id=status.id WHERE status.name='new';

--Оновити статус конкретного завдання.
UPDATE tasks SET status_id=2 WHERE id=5;

--Отримати список користувачів, які не мають жодного завдання.
SELECT * FROM users where id NOT IN (SELECT tasks.user_id FROM tasks);

--Додати нове завдання для конкретного користувача.
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New task for user','Do some work',1,22);

--Отримати всі завдання, які ще не завершено.
SELECT * FROM tasks WHERE status_id <> 3;

--Видалити конкретне завдання.
DELETE FROM tasks WHERE id=6;

--Знайти користувачів з певною електронною поштою.
SELECT * FROM users WHERE email LIKE 'example@test.com';

--Оновити ім'я користувача.
UPDATE users set fullname = 'John Doe' WHERE id=1;

--Отримати кількість завдань для кожного статусу.
SELECT name as Status,COUNT(t.id) as Number_of_tasks from status s
    LEFT join tasks t on s.id = t.status_id  GROUP  by t.status_id,s.id ORDER by s.id;

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
SELECT t.* FROM tasks t INNER JOIN users u ON t.user_id = u.id WHERE u.email LIKE '%example.org';

--Отримати список завдань, що не мають опису.
SELECT * FROM tasks WHERE description IS NULL;

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
SELECT * FROM users u INNER JOIN tasks t ON u.id = t.user_id WHERE t.status_id = 2 ORDER BY u.id;

--Отримати користувачів та кількість їхніх завдань.
SELECT u.*,COUNT(t.id) AS Number_of_tasks FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY t.user_id;