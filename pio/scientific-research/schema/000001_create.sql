BEGIN;

CREATE TABLE sources_funding
(
    id serial not null unique,
    name varchar(255) not null
);

CREATE TABLE researches
(
    id serial not null unique,
    topic varchar(255) not null,
    source_funding integer references sources_funding (id),
    start_date date not null,
    duration integer not null,
    funding_amount numeric(15, 2) not null
);

CREATE TABLE departments
(
    id serial not null unique,
    name varchar(255)
);

CREATE TABLE employees
(
    id serial not null unique,
    last_name varchar(255) not null,
    first_name varchar(255) not null,
    middle_name varchar(255) not null,
    department integer references  departments (id)
);

CREATE TABLE employee_researches
(
    id serial not null unique,
    research integer references researches (id),
    employee integer references employees (id)
);

CREATE INDEX idx_sources_funding on sources_funding (name);
CREATE INDEX idx_researches on researches (topic);
CREATE INDEX idx_departments on  departments (name);
CREATE INDEX idx_employees on employees (first_name);
CREATE INDEX idx_employee_researches on employee_researches (employee);

END;