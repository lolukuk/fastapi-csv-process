# Тестовое задание

### FastAPI File Processing Service

Этот проект представляет собой сервис для обработки файлов, созданный с использованием FastAPI, Celery и Redis. Сервис
позволяет загружать CSV файлы, которые затем обрабатываются асинхронно в фоновом режиме.

### Основные возможности

- **Загрузка файлов**: Пользователи могут загружать файлы с MIME типом `text/csv`.
- **Очередь на обработку**: Файлы добавляются в очередь и обрабатываются асинхронно.
- **Имитация обработки**: В процессе обработки добавляется задержка для имитации длительной работы.
- **Контейнеризация**: Проект упакован с использованием Docker и Docker Compose для лёгкого развёртывания.

### Технологии

- [FastAPI](https://fastapi.tiangolo.com/)
- [Celery](https://docs.celeryproject.org/en/stable/)
- [Redis](https://redis.io/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Установка и запуск

### Предварительные требования

- [Docker](https://www.docker.com/get-started)

### Шаги для запуска

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/fastapi-csv-process/fastapi-csv-process.git
   ```

2. Соберите и запустите Docker контейнеры:
   ```bash
   docker-compose up --build
   ```

3. Сервис будет доступен по адресу `http://localhost:8000` или можешь использовать Swagger UI.

### Тестирование загрузки файла

Вы можете использовать `curl` или любой другой инструмент для отправки POST-запроса с файлом:

```bash
curl -X POST "http://localhost:8000/uploadfile/" -F "file=@path/to/your/file.csv"
```

### Остановка сервиса

Для остановки сервиса используйте команду:

```bash
docker-compose down или ctr + c.
```

## Структура файлов

- `app/temp`: Все файлы которые были преобразованы 
- `app/main.py`: Основной файл приложения FastAPI, где определены маршруты и задачи Celery.
- `app/celeryconfig.py`: Конфигурация Celery.
- `Dockerfile`: Файл для создания Docker образа.
- `docker-compose.yml`: Файл для управления многоконтейнерными Docker приложениями.
- `requirements.txt`: Список Python-зависимостей.

## Дополнительная информация

### Конфигурация Celery

Celery использует Redis как брокер сообщений и для хранения результатов. Конфигурация Celery находится в
файле `app/celeryconfig.py`.

### Обработка файлов

Файлы загружаются через маршрут `/uploadfile/` и сохраняются в директорию `app/temp/`. Затем Celery обрабатывает файл,
добавляя задержку для имитации длительной работы. Обработанный файл сохраняется с добавлением суффикса `_processed`.

### Примечания по безопасности

- Убедитесь, что вы используете безопасные пути для сохранения и обработки файлов.
- Проверьте файлы на безопасность перед их обработкой, чтобы избежать уязвимостей.
- Проверьте все зависимости
