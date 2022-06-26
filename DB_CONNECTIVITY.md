1. Backend instaluje dodatkową wtyczkę do `flask` integrującą `SQLAlchemy` z `flask`iem

2. przed uruchomieniem aplikacji trzeba ustawić zmienną środowiskową `TAB_DB_URL` zawierający url do połączenia z bazą (tj. postrges LDAP url)

3. W trakcie pracy aplikacji `flask-sqlalchemy` zarządza połączeniami do bazy danych

4. Sesja bazy jest dostępna dla każdego endpointu w postaci zmiennej `db.session` w pliku `src/models/db.py`

5. Każdy request do backendu tworzy nową transakcję dla niego automatycznie, możemy dodawać nowe/usunąć wpisy do/z bazy dodając je do sesji (`db.session.add(model)` lub `db.session.delete(model)`) i zatwierdzać transakcję (`db.session.commit()`). Jeśli sesja nie zostanie zatwierdzona - zostaje z automatu zastosowany rollback.

6. Zawartość bazy danych jest tworzona poprzez zdefiniowanie w aplikacji stosownych modeli (pliki w folderze `src/models`) opisujące jakie tabele i pola z danymi mają tam być.

7. Nowe wiersze które będą dodane/usunięte do/z bazy (`model` w punkcie wyżej) to zwyczajne obiekty pythonowe.

8. Operacje na bazie sprowadzają się do np. `KlasaModelu.query.filter_by(...)` - `SELECT` na tabeli z `KlasaModelu` z klauzulą `WHERE` zależną od `filter_by(...)` itp. Zgodnie z [dokumentacją](https://docs.sqlalchemy.org/en/14/).

9. Aby utworzyć stosowne tabele w bazie z podanych modeli trzeba wygenerować migrację poleceniem `flask db migrate`, które wykorzysta zdefiniowaną zmienną środowiskową `FLASK_APP` aby znaleźć punkt wejściowy aplikacji i znaleźć używane modele oraz url do połączenia z bazą. Utworzona migracja trafia do folderu `migrations/versions` a nazwa pliku jest wypisywana przy `flask db migrate`. W ten sposób można zobaczyć wygenerowane wymagane operacje na bazie.

10. Aby zatwierdzić migracje w bazie trzeba użyć komendy `flask db upgrade`, która sprawdza która migracja była ostatnia wpisana do bazy i wpisuje wszystkie nowsze od niej.

11. Jeśli trzeba zrobić migrację nie tworzącą tabeli, a np. generującą przykładowe/podstawowe dane - `flask db revision` - tworzy pustą migrację do wypełnienia w dowolny sposób (np. [ta rewizja](backend/migrations/versions/6677b1ebfa12_.py))
