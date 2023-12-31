# Сбор  и отправка ДЗ

## Планирование

- 1 итерация
    - Реализация endpoint заглушек сервиса

- 2 итерация
    - Реализация базы данных, интеграция базы данных с бэкэндом

- 3 итерация
    - Добавление бизнес логики приложения
    - Интеграционное тестирование приложения

- 4 итерация
    - Добавление авторизации и аутентификации пользователей

- 5 итерация
    - Добавление фронтенда

## Требования
- Роли и доступ:
    - Приложение должно поддерживать две роли: преподаватель и студент.
    - Преподаватель должен иметь доступ к функциям проверки и оценки домашних заданий, отправки обратной связи студентам и просмотра таблицы результатов.
    - Студент должен иметь доступ к функции отправки домашних заданий, просмотра полученной обратной связи и таблицы с результатами.
- Отправка файлов:
   - Пользователи (студенты) должны иметь возможность отправлять текстовые файлы с домашними заданиями.
   - Отправленные файлы должны быть доступны преподавателю для проверки.
- Обратная связь:
   - Преподаватель должен иметь возможность оставлять комментарии и оценки для каждого отправленного задания студента.
   - Студент должен получать уведомления о полученных комментариях и оценках.
- Таблица результатов:
   - Приложение должно предоставлять таблицу результатов, где отображается информация о каждом студенте и его оценках за все домашки.
   - Таблица должна быть доступна для преподавателя и студентов.
- Модульные тесты:
   - Приложение должно быть покрыто модульными тестами для проверки корректности работы каждого модуля и функции.
   - Тесты должны включать проверку отправки файлов, обработку оценок, а также отображение результатов.
- Интерфейс:
   - Приложение должно иметь удобный и интуитивно понятный интерфейс для обоих ролей пользователей.

## Планирование 27.11.2023

- Добавление возможности оценки и комментирования домашнего задания преподавателем

- Рефакторинг кода

- Добавление дедлайнов для домашнего задания и возможности исправления

- Добавление новой сущности `Result`. Теперь при загрузке домашнего задания создаётся объект `Homework`. После оценивания домашнего задания создаётся объект `Result` со связью один к одному

- Реализация добавления домашего задания в систему