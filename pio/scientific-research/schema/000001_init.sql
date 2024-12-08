CREATE DATABASE scientific_research_database
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'ru_RU.UTF-8'
    LC_CTYPE = 'ru_RU.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

GRANT TEMPORARY, CONNECT ON DATABASE scientific_research_database TO PUBLIC;

GRANT ALL ON DATABASE scientific_research_database TO pobedimka;

GRANT ALL ON DATABASE scientific_research_database TO postgres;