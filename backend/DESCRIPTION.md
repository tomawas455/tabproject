# plik src/App.py
  jest to plik z konfiguracją całej aplikacji.
  Tutaj ustawiane są takie dane jak url do łączenia z bazą czy secret key.
  W tym pliku są również podpinane do aplikacji wszystkie endpointy
  (innymi słowy jest to plik gdzie każdy po utworzeniu sswojej części
  zadań musiał je dopisać aby były widziane, można było wysyłać zapytania
  do utworzonych endpointów).

# folder src/models
  Tu znajdują się wszystkie modele aplikacji (czyli również tabele z bazy danych).

## plik src/models/db.py
  Zawiera on kalsę bazową dla modeli,
  która implementuje metodę pozwalającą na przekonwertowanie obiektu
  pythonowego na słownik (dict), który to da się prosto zamienić w stringa jsonowego.

## pola w modelach
  `__tablename__` - nazwa tabeli której dany model dotyczny<br/>
  `db.Column(...)` - typ kolumny w danej tabeli, jej ograniczenia itp.<br/>
  `_default_fields` - pola które pojawią się w słowniku po konwersji (i co za tym idzie - w jsonie)

# plik src/access_guards.py
  Zawiera dekoratory dla endpointów które można dodać,
  aby wymusić do danego endpointu dostęp tylko dla osób
  z odpowiednią rolą w systemie, np. `@only_admin` wymusza,
  że do udekorowanego endpointu zapytania może wysłać tylko administrator.

# folder src/routes
  Zawiera on implementacje endpointów do konkretnych funkcjonalności aplikacji.

## plik src/routes/raports.py
  Tu znajdują się endpointy do generowania raportów
  `get_worker_raport` - generuje raport dla pracownika wedle odpowiednich ustawień (przesłanych w zapytaniu).
  `get_user_raport` - generuje raport dla użytkownika,
  np. w jakich kursach brał udział w przedziale czasu, ile go to kosztowało itp.

## plik src/routes/trainings.py
  Zawiera enpointy do pozyskiwania/tworzenia/edytowania edycji kursów, `GET`em można pozyskać stronę kursów lub kurs o konkretnym id,
  `POST`em - utworzyć nową edycję kursu (zakładając odpowiednie uprawnienia i obecność wszystkich danych),
  `PATCH`em - edytować.<br/><br/>

Pozostałe pliki w tym folderze stosują tą konwencję, więc ich struktura będzie podobna.