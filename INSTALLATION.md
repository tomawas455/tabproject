# Preferowana droga - docker

1. zainstalować dockera i docker-compose<br/>
    [windows](https://docs.docker.com/desktop/windows/install/)<br/>
    [linux](https://docs.docker.com/desktop/linux/install/)<br/>
    [mac](https://docs.docker.com/desktop/mac/install/)

2. sklonuj repozytorium<br/>
    `git clone https://github.com/tomawas455/tabproject.git`

3. przejść do folderu z projektem<br/>
    `cd tabproject`

4. odpalić projekt<br/>
    windows - `docker-compose up`<br/>
    linux - `sudo docker-compose up`<br/>
    mac - `docker-compose up`

5. sprawdzić projekt<br/>
    `localhost:3000` - strona<br/>
    `localhost:5000` - backend<br/>
    `localhost:2137` - baza danych

6. troubleshooting
    jeśli na windowsie nie chce ruszyć - `git config --global core.autocrlf input`, sklonować repozytorium, `git config --global core.autocrlf false` (albo jak wartość była wcześniej, domyślna to `false`)

# Nieprzyjemna droga - bare metal
1. zainstalować pythona, node/npm i postgresql<br/>
    [python](https://www.python.org/downloads/)<br/>
    [node](https://nodejs.org/en/)<br/>
    [postgresql](https://www.postgresql.org/download/)

2. skonfigurować postgresql<br/>
    tak żeby istniała baza doi projektu (np. `psql` -> `CREATE DATABASE tabproject;`);<br/>
    i postgres był uruchomiony<br/>

3. sklonować repozytorium<br/>
    `git clone https://github.com/tomawas455/tabproject.git`

4. przejść do folderu z projektem<br/>
    `cd tabproject`

5. (opcjonalne) stworzyć wirtualne środowisko dla pythona<br/>
    dzięki temu projekt nie będzie zainstalowany w systemie - nie będzie zaśmiecał systemu.<br/>
    `python -m venv ../venv`<br/>
    `../venv` jest ścieżką dla środowiska, może być inna.<br/>
    w kolejnych krokach w przypadku komendy `pip`, `python` czy `flask` trzeba pisać `../venv/bin/pip`, `..venv/bin/python` i `../venv/bin/flask`.

6. zainstalować zależności backendowe<br/>
    `pip install -e .`

7. skonfigurować środowisko<br/>
    stworzyć zmienną środowiskową `FLASK_APP=src/app.py` lub `FLASK_APP=full/tabproject/path/tabproject/backend/src/app.py` oraz `FLASK_ENV=production`.<br/>
    ustawić zmienne środowiskowe `TAB_DB_URL` oraz `TAB_SECRET_KEY`.<br/>
    pierwsza powinna zawierać url do połączenia z bazą danych, a druga secret key dla aplikacji.
    
8. odpalić postgres<br/>
    windows - wejść do folderu z zainstalowanym postgresem i uruchomić `pg_cli start`<br/>
    linux - prawdopodobnie sam się uruchomił po instalacji, jeśli nie - `systemctl start postgres`

9. odpalić backend<br/>
    `cd backend` i `flask run`

10. odpalić frontend<br/>
    otworzyć drugie okno lini komend, wejść do folderu `tabproject/frontend` i uruchomić `npm start`
