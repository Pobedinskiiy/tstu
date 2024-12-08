SELECT * FROM logs
WHERE page_id = 256
  AND user_type IN ('Новые пользователи', 'Пользователи, пришедшие по ссылкам')
  AND duration >= interval '300 seconds'
ORDER BY visit_date;