# Установка

- скачайте последню версию [скриптов](https://github.com/asboldyrev/monitor/releases).
- распакуйте в папку, где будут находиться файлы проекта.
- находясь в папке выполните следующие команды:
    - `python3 -m venv env`
    - `source env/bin/activate`
    - `pip install docker psutil`
    - `nohup python3 ./stat.py`
- при необходимости поправьте файл docker-compose.yml
- выполните команду `docker-compose up -d`
