BEGIN;

UPDATE researches SET source_funding = NULL WHERE source_funding IN (2, 7);

UPDATE employees SET department = NULL  WHERE department IN (3, 5);

DELETE FROM sources_funding WHERE id IN (2, 7);

DELETE FROM departments WHERE id IN (3, 5);

COMMIT;