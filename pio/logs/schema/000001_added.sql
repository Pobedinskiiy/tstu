DO $$
    DECLARE
        user_types TEXT[] := ARRAY[
            'Новые пользователи',
            'Регулярные посетители',
            'Подписчики на новости',
            'Покупатели товаров',
            'Потенциальные клиенты',
            'Пользователи мобильных устройств',
            'Пользователи с высокой вовлечённостью',
            'Гости с поисковых систем',
            'Пользователи, пришедшие по ссылкам',
            'Посетители из социальных сетей'];
    BEGIN
        FOR i IN 1..7000000 LOOP
            INSERT INTO logs (user_type, page_id, duration, visit_date)
            VALUES (
                       user_types[1 + floor(random() * array_length(user_types, 1))],
                       1 + floor(random() * 500),
                       (100 + floor(random() * 501)) * interval '1 second',
                       NOW() - (random() * interval '3 years')
                   );
        END LOOP;
    END $$;

DO $$
    DECLARE
        user_types TEXT[] := ARRAY[
            'Новые пользователи',
            'Регулярные посетители',
            'Подписчики на новости',
            'Покупатели товаров',
            'Потенциальные клиенты',
            'Пользователи мобильных устройств',
            'Пользователи с высокой вовлечённостью',
            'Гости с поисковых систем',
            'Пользователи, пришедшие по ссылкам',
            'Посетители из социальных сетей'];
    BEGIN
        INSERT INTO logs (user_type, page_id, duration, visit_date)
        SELECT
            user_types[1 + floor(random() * array_length(user_types, 1))],
            1 + floor(random() * 500),
            (100 + floor(random() * 501)) * interval '1 second',
            NOW() - (random() * interval '3 years')
        FROM generate_series(1, 7000000);
    END $$;