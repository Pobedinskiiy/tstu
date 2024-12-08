BEGIN;

CREATE TABLE logs
(
    log_id serial not null unique,
    user_type varchar(255) not null,
    page_id serial not null,
    duration interval not null,
    visit_date timestamp not null
);

END;

CREATE INDEX idx_logs_optimized ON logs (page_id, user_type, duration, visit_date);