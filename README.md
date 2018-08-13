# Python 3 Flask Docker

Пример Docker-контейнера c веб-приложением на базе Flask для Python 3.

Построен на стандартном образе Python 3 Docker image с использованием Alpine Linux, подробнее https://hub.docker.com/_/python/

## Создания образа Docker

Сборка образа:

`make build`

## Запуск контейнера

Запуск контейнера на основе подготовленного образа:

`make run`

Теперь вы можете открыть в браузере ссылку http://0.0.0.0:5000 и посмотреть демонстрационное веб-приложения на Flask.

Если вы используете docker machine (на Mac OS X или Windows) пожалуйста используйте команду docker inspect чтобы узнать IP-адрес (используете `make inspect`)