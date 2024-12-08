BEGIN;

UPDATE departments SET name = 'Электроника' WHERE name = 'Электротехника';

UPDATE departments SET name = 'Разработка программного обеспечения' WHERE name = 'Информатика';

UPDATE departments SET name = 'Современные биоматериалы' WHERE name = 'Биотехнологии';

UPDATE employees SET last_name = 'Иванов', first_name = 'Сергей', middle_name = 'Николаевич' WHERE last_name = 'Иванов' AND first_name = 'Пётр';

UPDATE employees SET department = 2 WHERE last_name = 'Петров' AND first_name = 'Александр';

UPDATE employees SET middle_name = 'Анатольевич' WHERE last_name = 'Сидоров' AND first_name = 'Алексей';

UPDATE researches SET funding_amount = 175000.00 WHERE topic = 'Исследование новых материалов';

UPDATE researches SET duration = 20 WHERE topic = 'Разработка методов лечения заболеваний';

UPDATE researches SET source_funding = 5 WHERE topic = 'Новые подходы в биотехнологии';

COMMIT;