CREATE OR REPLACE FUNCTION total_funding_by_source(funding_source_id INTEGER)
    RETURNS numeric AS $$
DECLARE
    total_funding numeric(15, 2);
BEGIN

    SELECT SUM(funding_amount) INTO total_funding FROM researches WHERE source_funding = funding_source_id;

    IF total_funding IS NULL THEN
        total_funding := 0;
    END IF;

    RETURN total_funding;
END;
$$ LANGUAGE plpgsql;

SELECT total_funding_by_source(1);

SELECT
    sf.name AS funding_source,
    r.funding_amount AS research_count
FROM
    sources_funding sf
        JOIN
    researches r ON sf.id = r.source_funding
ORDER BY
    sf.id;

--/------------------------------------------------------------------------------------------------------------------/--

CREATE OR REPLACE FUNCTION count_researches_by_employee(employee_id INTEGER)
    RETURNS INTEGER AS $$
DECLARE
    research_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO research_count FROM employee_researches WHERE employee = employee_id;

    RETURN research_count;
END;
$$ LANGUAGE plpgsql;

SELECT count_researches_by_employee(1);

SELECT
    e.last_name AS employees,
    r.topic AS research_topic
FROM
    employees e
        JOIN
    employee_researches er ON e.id = er.employee
        JOIN
    researches r ON er.research = r.id
ORDER BY
    e.id;

--/------------------------------------------------------------------------------------------------------------------/--

CREATE OR REPLACE PROCEDURE add_new_research(
    research_name VARCHAR,
    funding_source_id INTEGER,
    start_date DATE,
    duration INTEGER,
    funding_amount NUMERIC
)
    LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO researches (topic, source_funding, start_date, duration, funding_amount)
    VALUES (research_name, funding_source_id, start_date, duration, funding_amount);

    RAISE NOTICE 'Новое исследование добавлено: %, финансирование от источника: %', research_name, funding_source_id;
END;
$$;

CALL add_new_research('Разработка безотказной системы управления', 1, '2024-02-07', 3, 100000.00);

SELECT * FROM research;

--/------------------------------------------------------------------------------------------------------------------/--

ALTER TABLE employees ADD COLUMN academic_degree VARCHAR(255);

CREATE OR REPLACE PROCEDURE update_academic_degree(
    employee_id INTEGER,
    new_academic_degree VARCHAR
)
    LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (SELECT * FROM employees WHERE id = employee_id) THEN
        RAISE NOTICE 'Сотрудник с ID % не существует.', employee_id;
        RETURN;
    END IF;

    UPDATE employees SET academic_degree = new_academic_degree WHERE id = employee_id;

    RAISE NOTICE 'Академическая степень для сотрудника с ID % обновлена на %.', employee_id, new_academic_degree;
END;
$$;

CALL update_academic_degree(1, 'Доктор наук');

SELECT * FROM employees;
