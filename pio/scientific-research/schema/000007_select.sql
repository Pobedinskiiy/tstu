BEGIN;

SELECT * FROM sources_funding;

SELECT
    d.name AS department_name,
    r.topic AS research_topic,
    r.funding_amount AS funding_amount
FROM
    departments d
        JOIN
    employees e ON d.id = e.department
        JOIN
    employee_researches er ON e.id = er.employee
        JOIN
    researches r ON er.research = r.id
ORDER BY
    d.name, r.topic;

SELECT
    sf.name AS funding_source,
    r.funding_amount AS research_count
FROM
    sources_funding sf
        JOIN
    researches r ON sf.id = r.source_funding
ORDER BY
    sf.name, r.funding_amount;

SELECT * FROM researches WHERE start_date > '2024-01-01' AND funding_amount > 100000;

SELECT
    sf.name AS funding_source,
    COUNT(r.id) AS research_count
FROM
    sources_funding sf
        LEFT JOIN
    researches r ON sf.id = r.source_funding
GROUP BY
    sf.id, sf.name
ORDER BY
    sf.name;

SELECT
    sf.name AS funding_source,
    ROUND(AVG(r.funding_amount), 2) AS average_funding
FROM
    sources_funding sf
        JOIN
    researches r ON sf.id = r.source_funding
GROUP BY
    sf.id, sf.name
HAVING
    AVG(r.funding_amount) > 50000
ORDER BY
    average_funding DESC;

COMMIT;