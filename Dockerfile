# Используйте официальный образ Python в качестве базового образа
FROM python:3.9

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файлы вашего приложения в контейнер
COPY . .

# Укажите команду, которая будет запускаться при запуске контейнера
CMD ["python", "app.py"]

