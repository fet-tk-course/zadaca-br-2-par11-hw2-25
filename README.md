[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)

# Zadaća 2 - REST API aplikacija

## O projektu

Ova aplikacija predstavlja digitalni sistem za upravljanje procesom udomljavanja životinja. Cilj projekta je omogućiti azilima za životinje efikasnu evidenciju dostupnih ljubimaca i potencijalnih udomitelja. Aplikacija služi kao centralizovana platforma koja povezuje životinje koje traže dom sa ljudima koji ispunjavaju uslove za udomljavanje, čime se ubrzava i olakšava cijeli proces.

Aplikacija je razvijena kao REST API koristeći Python ekosistem, odnosno FastAPI, SQLModel i SQLite bazu podataka. Sistem omogućava osnovne CRUD operacije nad dva povezana resursa: životinjama dostupnim za udomljavanje i potencijalnim udomiteljima.

## Tim

- **Student A**: Džana Dugonjić - resurs: `/animals`
- **Student B**: Danijela Mihajlović - resurs: `/adopters`

## Korištene tehnologije

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Git i GitHub

## Struktura projekta

```text
project/
|-- main.py
|-- database.py
|-- models_a.py
|-- models_b.py
|-- routes_a.py
|-- routes_b.py
|-- README.md
|-- requirements.txt
```

### Opis datoteka

- `main.py` - kreira FastAPI aplikaciju, uključuje routere i pokreće kreiranje tabela pri startu aplikacije.
- `database.py` - sadrži konfiguraciju SQLite baze podataka, engine, funkciju za kreiranje tabela i dependency funkciju `get_session`.
- `models_a.py` - sadrži SQLModel entitet i sheme za resurs `Animal`.
- `routes_a.py` - sadrži CRUD endpoint-e za resurs `/animals`.
- `models_b.py` - sadrži SQLModel entitet i sheme za resurs `Adopter`.
- `routes_b.py` - sadrži CRUD endpoint-e za resurs `/adopters`.
- `README.md` - sadrži opis projekta, upute za pokretanje, pregled endpointa i evidenciju korištenja AI alata.

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip
- Git

### Koraci

1. Klonirajte repozitorij:

```bash
git clone https://github.com/fet-tk-course/zadaca-br-2-par11-hw2-25.git
cd zadaca-br-2-par11-hw2-25
```

2. Kreirajte virtuelno okruženje:

```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje.

Na Windows sistemu:

```bash
venv\Scripts\activate
```

Ako se koristi Git Bash na Windows-u:

```bash
source venv/Scripts/activate
```

Na Linux/Mac sistemu:

```bash
source venv/bin/activate
```

4. Instalirajte zavisnosti:

```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:

```bash
uvicorn main:app --reload
```

6. Otvorite Swagger dokumentaciju u browseru:

```text
http://localhost:8000/docs
```

## API Endpointi

## Resurs A: `/animals`

Resurs `Animal` predstavlja životinju koja se nalazi u azilu i dostupna je za udomljavanje.

### Polja modela Animal

| Polje | Tip | Opis |
|---|---|---|
| id | int | Automatski generisani primarni ključ |
| name | str | Ime životinje |
| species | str | Vrsta životinje, npr. cat, dog, rabbit |
| age | int | Starost životinje |
| vaccinated | bool | Informacija da li je životinja vakcinisana |
| adoption_fee | float | Naknada za udomljavanje |
| description | Optional[str] | Dodatni opis životinje |

### Endpointi za `/animals`

| Metoda | Ruta | Opis |
|---|---|---|
| GET | `/animals/` | Lista svih životinja, uz opcionalni query filter po vrsti |
| GET | `/animals/{animal_id}` | Dohvatanje jedne životinje po ID-u |
| POST | `/animals/` | Kreiranje nove životinje |
| PUT | `/animals/{animal_id}` | Potpuna zamjena podataka za životinju |
| PATCH | `/animals/{animal_id}` | Djelimično ažuriranje podataka za životinju |
| DELETE | `/animals/{animal_id}` | Brisanje životinje |

### Query filter za `/animals`

Endpoint `GET /animals/` podržava opcionalni query parametar `species`.

Primjer:

```text
GET /animals/?species=cat
```

Ovaj zahtjev vraća samo životinje čija je vrijednost polja `species` jednaka `cat`.

### Primjeri zahtjeva za `/animals`

#### Kreiranje nove životinje

```bash
curl -X POST "http://localhost:8000/animals/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Luna",
    "species": "cat",
    "age": 2,
    "vaccinated": true,
    "adoption_fee": 25.5,
    "description": "Friendly cat ready for adoption"
  }'
```

#### Dohvatanje svih životinja

```bash
curl -X GET "http://localhost:8000/animals/" \
  -H "accept: application/json"
```

#### Dohvatanje životinja po vrsti

```bash
curl -X GET "http://localhost:8000/animals/?species=cat" \
  -H "accept: application/json"
```

#### Dohvatanje životinje po ID-u

```bash
curl -X GET "http://localhost:8000/animals/1" \
  -H "accept: application/json"
```

#### Potpuna zamjena podataka za životinju

```bash
curl -X PUT "http://localhost:8000/animals/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Luna",
    "species": "cat",
    "age": 3,
    "vaccinated": true,
    "adoption_fee": 30.0,
    "description": "Updated full animal record"
  }'
```

#### Djelimično ažuriranje životinje

```bash
curl -X PATCH "http://localhost:8000/animals/1" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 4
  }'
```

#### Brisanje životinje

```bash
curl -X DELETE "http://localhost:8000/animals/1" \
  -H "accept: */*"
```

## Resurs B: `/adopters`

Resurs `Adopter` predstavlja osobu koja je zainteresovana za udomljavanje životinje.

### Polja modela Adopter

| Polje | Tip | Opis |
|---|---|---|
| id | int | Automatski generisani primarni ključ |
| first_name | str | Ime udomitelja |
| last_name | str | Prezime udomitelja |
| age | int | Starost udomitelja |
| email | str | Email adresa |
| phone_number | str | Broj telefona |
| has_experience | bool | Informacija da li udomitelj ima prethodno iskustvo sa životinjama |

### Endpointi za `/adopters`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/adopters` | Lista svih resursa, uz opcionalni query filter |
| GET | `/adopters/{id}` | Dohvatanje udomitelja po ID-u |
| POST | `/adopters` | Kreiranje novog udomitelja |
| PUT | `/adopters/{id}` | Potpuna zamjena podataka za udomitelja |
| PATCH | `/adopters/{id}` | Djelimično ažuriranje podataka za udomitelja |
| DELETE | `/adopters/{id}` | Brisanje udomitelja |

### Query filter za `/adopters`

Endpoint `GET /adopters` podržava opcionalni query parametar `experience`.

Primjer:

```text
GET /adopters?experience=true
```

Ovaj zahtjev vraća udomitelje koji imaju prethodno iskustvo sa životinjama.

### Primjeri zahtjeva za `/adopters`

#### Kreiranje novog udomitelja

```bash
curl -X 'POST' \
  'http://localhost:8000/adopters' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "Mujo",
  "last_name": "Mujić",
  "age": 28,
  "email": "mujo.mujic@email.com",
  "phone_number": "061123456",
  "has_experience": true
}'
```

#### Dohvatanje udomitelja koji imaju prethodno iskustvo

```bash
curl -X 'GET' \
  'http://localhost:8000/adopters?experience=true' \
  -H 'accept: application/json'
```

#### Dohvatanje detalja o udomitelju sa ID-om 1

```bash
curl -X 'GET' \
  'http://localhost:8000/adopters/1' \
  -H 'accept: application/json'
```

#### Potpuna zamjena podataka za udomitelja sa ID-om 1

```bash
curl -X 'PUT' \
  'http://localhost:8000/adopters/1' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "Mujo",
  "last_name": "Nova-Prezime",
  "age": 30,
  "email": "mujo.novi@email.com",
  "phone_number": "061999888",
  "has_experience": false
}'
```

#### Promjena samo broja telefona za udomitelja sa ID-om 1

```bash
curl -X 'PATCH' \
  'http://localhost:8000/adopters/1' \
  -H 'Content-Type: application/json' \
  -d '{
  "phone_number": "062999888"
}'
```

#### Brisanje udomitelja po ID-u

```bash
curl -X 'DELETE' \
  'http://localhost:8000/adopters/1' \
  -H 'accept: */*'
```

## Napomene o implementaciji

- Aplikacija koristi SQLite bazu podataka.
- Tabele se kreiraju automatski prilikom pokretanja aplikacije.
- Za rad sa bazom koristi se SQLModel `Session`.
- Sesija baze podataka se prosljeđuje endpointima pomoću FastAPI dependency injection mehanizma i funkcije `Depends(get_session)`.
- Endpointi koji primaju ID vraćaju HTTP 404 grešku ako traženi resurs ne postoji.
- `POST` endpointi vraćaju statusni kod 201 nakon uspješnog kreiranja resursa.
- `DELETE` endpointi vraćaju statusni kod 204 nakon uspješnog brisanja resursa.
- `PATCH` endpointi koriste `exclude_unset=True`, tako da se ažuriraju samo ona polja koja su eksplicitno poslana u zahtjevu.
- API se može testirati kroz automatski generisanu Swagger dokumentaciju na adresi `http://localhost:8000/docs`.

## Git workflow

Rad na projektu je organizovan kroz Git grane.

- Svaki student je radio na posebnoj grani.
- Svaka funkcionalnost je commitovana jasnim i opisnim commit porukama.
- Izmjene su pushane na GitHub.
- Spajanje grana u `main` treba se izvršiti pomoću komande:

```bash
git merge --no-ff naziv-grane
```

Fast-forward merge se ne koristi.

## Korištenje AI alata

### Student A

**Alat:** ChatGPT  
**Model:** GPT-5.5  

**Primjer 1:**

- **Prompt:** "Pomozi mi implementirati CRUD endpoint-e za Animal resurs koristeći FastAPI i SQLModel."
- **Kako je pomoglo:** AI je pomogao u pisanju i razumijevanju endpointa za kreiranje, dohvat, potpunu zamjenu, djelimično ažuriranje i brisanje životinja.
- **Prilagodbe:** Kod je prilagođen strukturi projekta, nazivima fajlova, domeni aplikacije i zahtjevima zadaće.

**Primjer 2:**

- **Prompt:** "Objasni mi kako testirati POST, GET, PUT, PATCH i DELETE endpoint-e u Swagger dokumentaciji."
- **Kako je pomoglo:** AI je objasnio redoslijed testiranja endpointa kroz `http://localhost:8000/docs`, uključujući primjere JSON zahtjeva.
- **Prilagodbe:** Primjeri su prilagođeni domeni aplikacije i `Animal` modelu.

### Student B

**Alat:** Gemini  

**Primjer 1:**

- **Prompt:** "Kako bih mogla implementirati GET metodu u kojoj dohvatamo podatke po ID-u?"
- **Kako je pomoglo:** AI je napisao kod za traženu metodu, te objasnio kako taj kod radi.
- **Prilagodbe:** Generisani kod je bio ispravno napisan i nije ga bilo potrebno dodatno prilagođavati.

**Primjer 2:**

- **Prompt:** "Kako implementirati REST API endpoint-e za resurs udomitelja?"
- **Kako je pomoglo:** AI je pomogao pri razumijevanju strukture CRUD endpointa i načina rada sa FastAPI rutama.
- **Prilagodbe:** Kod je prilagođen odabranoj domeni aplikacije i strukturi projekta.

## Zaključak

Ova REST API aplikacija omogućava osnovno upravljanje podacima u sistemu za udomljavanje životinja. Kroz implementaciju dva povezana resursa, `animals` i `adopters`, aplikacija demonstrira rad sa FastAPI rutama, SQLModel modelima, SQLite bazom podataka, dependency injection pristupom i osnovnim Git workflow-om za timski rad.



### Provjera zadace Student B

**Z1a**: Obzirom na to da sam vec imala @field_valiodator za provjeru email adrese (da mora sadrzavati @), implementirala sam jos jedan @field_validator za provjeru da li ime i prezime udomitelja pocinju velikim slovom.
**Z1b**: Dodala sam provjeru u POST metodu koja provjerava da li vec postoji udomitelj sa istim emailom.
**Z2**: Metod POST prima ime i vraca bool vrijednost u zavisnosti da li u bazi postoji korisnik sa tim imenom ili ne postoji.
Primjer zahtjeva je da posaljemo da li u bazi postoji udomitelj sa imenom Danijela, a odgovor nam je true ili false.
**Z1**: Porvjeravamo da li u emailu postoji znak @ i da li ime i prezime pocinju velikim slovom. Ukoliko prvo nije tacno vraca se HTTP greska sa porukom "Email adresa mora sadržavati znak '@'", a ukoliko drugo validacijsko pravilo nije ispunjeno vrati se HTTP greska sa porukom: "Naziv mora pocinjati velikim slovom".
u Z1b se jedinstvenost provjerava u polju email, te ukoliko udomitelj sa tim emailom vec postoji vraca se HTTP_409_CONFLICT i poruka "Korisnik sa ovim emailom već postoji."