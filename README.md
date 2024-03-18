# Загрузка изображений из космоса и пост их в тг канал
## Описание
Данный скрипт позволяет скачивать изображения из космоса и постить их в телеграм канал. Программа также способна сортировать изображения по директориям в зависимости откуда было загружено изображение
## Пример запуска
### Для того что бы запустить скрипты, необходимо скачать python3.
___
Загрузить изображения можно с помощью данных команд:
```shell
Python apod.py
```
```shell
Python spacex.py
```
```shell
Python epic.py
```
После этого в соответствующих директориях появятся изображения
___
Что бы запостить изображения в телеграм канал необходимо прописать в shell команду ниже
```shell
Python main.py
```
Тогда в телеграм канале будет поститься случайное изображение космоса каждые 4 часа

## Переменные окружения

Данный проект использует переменные окружения с помощью библиотеки python-dotenv.
Для того что бы код работал нужно создать файл `.env` и вписать туда следующие переменные окружения
```dict
SLEEP_TIME= Промежуток времкни через которое будет постится картинка 
NASA_API_KEY= Аpi полученный от Nasa 
TG_CHAT_ID= Айди вашего тг канала
TG_TOKEN= Токен, полученный от Bot_father
```