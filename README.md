# Test_task-2_Bewise
Тестовое задание №2 Bewise.ai

Задание:
 - С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.
 - Реализовать веб-сервис со следующими REST методами:
    - Создание пользователя, POST:
      - Принимает на вход запросы с именем пользователя;
      - Создаёт в базе данных пользователя заданным именем, так же генерирует уникальный идентификатор пользователя и UUID токен доступа (в виде строки) для данного пользователя;
      - Возвращает сгенерированные идентификатор пользователя и токен.
    - Добавление аудиозаписи, POST:
      - Принимает на вход запросы, содержащие уникальный идентификатор пользователя, токен доступа и аудиозапись в формате wav;
      - Преобразует аудиозапись в формат mp3, генерирует для неё уникальный UUID идентификатор и сохраняет их в базе данных;
      - Возвращает URL для скачивания записи вида http://host:port/record?id=id_записи&user=id_пользователя.
    - Доступ к аудиозаписи, GET:
      - Предоставляет возможность скачать аудиозапись по ссылке из п 2.2.3.
 - Для всех сервисов метода должна быть предусмотрена предусмотрена обработка различных ошибок, возникающих при выполнении запроса, с возвращением соответствующего HTTP статуса.
 - Модель данных (таблицы, поля) для каждого из заданий можно выбрать по своему усмотрению.
 - В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисами из пп. 2. и 3., их настройке и запуску. А также пример запросов к методам сервиса.
 - Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAlchemy,  пользоваться аннотацией типов.  

 ### Технологии
[![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi%20-%2313988a.svg?&style=for-the-badge&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIgogICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgaWQ9InN2ZzgiCiAgIHZlcnNpb249IjEuMSIKICAgdmlld0JveD0iMCAwIDYuMzQ5OTk5OSA2LjM0OTk5OTkiCiAgIGhlaWdodD0iNi4zNDk5OTk5bW0iCiAgIHdpZHRoPSI2LjM0OTk5OTltbSI+CiAgPGRlZnMKICAgICBpZD0iZGVmczIiIC8+CiAgPG1ldGFkYXRhCiAgICAgaWQ9Im1ldGFkYXRhNSI+CiAgICA8cmRmOlJERj4KICAgICAgPGNjOldvcmsKICAgICAgICAgcmRmOmFib3V0PSIiPgogICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2Uvc3ZnK3htbDwvZGM6Zm9ybWF0PgogICAgICAgIDxkYzp0eXBlCiAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vcHVybC5vcmcvZGMvZGNtaXR5cGUvU3RpbGxJbWFnZSIgLz4KICAgICAgICA8ZGM6dGl0bGU+PC9kYzp0aXRsZT4KICAgICAgPC9jYzpXb3JrPgogICAgPC9yZGY6UkRGPgogIDwvbWV0YWRhdGE+CiAgPGcKICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtODcuNTM5Mjg2LC04NC40MjYxOTEpIgogICAgIGlkPSJsYXllcjEiPgogICAgPHBhdGgKICAgICAgIGlkPSJwYXRoODE1IgogICAgICAgZD0ibSA4Ny41MzkyODYsODQuNDI2MTkxIGggNi4zNSB2IDYuMzUgaCAtNi4zNSB6IgogICAgICAgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6MC4yNjQ1ODMzMiIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0ic3Ryb2tlLXdpZHRoOjAuMjY0NTgzMzI7ZmlsbDojZmZmZmZmIgogICAgICAgaWQ9InBhdGg4MTciCiAgICAgICBkPSJtIDkwLjcxNDI4Niw4NC45NjA2NDkgYyAtMS40NTc4NTQsMCAtMi42NDA1NDIsMS4xODI2ODggLTIuNjQwNTQyLDIuNjQwNTQyIDAsMS40NTc4NTQgMS4xODI2ODgsMi42NDA1NDIgMi42NDA1NDIsMi42NDA1NDIgMS40NTc4NTQsMCAyLjY0MDU0MiwtMS4xODI2ODggMi42NDA1NDIsLTIuNjQwNTQyIDAsLTEuNDU3ODU0IC0xLjE4MjY4OCwtMi42NDA1NDIgLTIuNjQwNTQyLC0yLjY0MDU0MiB6IG0gLTAuMTM3NTgzLDQuNzU3MjA5IHYgLTEuNjU2MjkyIGggLTAuOTIwNzUgbCAxLjMyMjkxNiwtMi41NzcwNDIgdiAxLjY1NjI5MiBoIDAuODg2MzU0IHoiIC8+CiAgPC9nPgo8L3N2Zz4K)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?&style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/docker%20-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)  

### Запуск проекта
- Скачать и установить [Docker](https://docs.docker.com/get-docker/)
- Клонировать репозиторий ```git clone https://github.com/Pash1et/Test_task-2_Bewise.git``` 
- В корне директории test_task-2_bewise создать файл .env и заполнить его по примеру .env.example
- В папке infra выполнить команду ```docker compose up -d```
- Перейти по адресу ```http://127.0.0.1:8000/docs```  

### Примеры запросов
![1](https://github.com/Pash1et/Test_task-2_Bewise/assets/64920375/06273489-4125-482b-993e-749c89291fc1)
![2](https://github.com/Pash1et/Test_task-2_Bewise/assets/64920375/b0baa53e-481e-4f41-9fc8-de05fc66bc65)
![3](https://github.com/Pash1et/Test_task-2_Bewise/assets/64920375/01cff986-8631-4e8d-be51-0697f656ed45)
![4](https://github.com/Pash1et/Test_task-2_Bewise/assets/64920375/61c40120-4e05-40ba-8dc1-8a6d23ce18fd)
![5](https://github.com/Pash1et/Test_task-2_Bewise/assets/64920375/cb6b0a91-d300-45d9-b660-5625fe989077)
![6](https://github.com/Pash1et/Test_task-2_Bewise/assets/64920375/f4df37d2-a914-4d4f-aed8-d8577b6936ee)
![7](https://github.com/Pash1et/Test_task-2_Bewise/assets/64920375/ca236279-3ec5-4da0-ade3-136f35fe9f6e)


