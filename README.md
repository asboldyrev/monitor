# Установка

- скачайте последню версию скриптов [release-v1.0.0.zip](https://github.com/asboldyrev/monitor/releases)
- распакуйте в папку, где будут находиться файлы проекта.
- находясь в папке выполните следующие команды:
    - `sudo apt install python3-pip`
    - `python3 -m venv env`
    - `source env/bin/activate`
    - `pip install docker psutil`
    - `nohup python3 ./stat.py`
- при необходимости поправьте файл docker-compose.yml
- выполните команду `docker-compose up -d`
