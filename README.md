[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Ova aplikacija predstavlja digitalni sistem za upravljanje procesom udomljavanja životinja. Cilj projekta je omogućiti azilima za životinje efikasnu evidenciju dostupnih ljubimaca i potencijalnih udomitelja. Aplikacija služi kao centralizovana platforma koja povezuje životinje koje traže dom sa ljudima koji ispunjavaju uslove za udomljavanje, čime se ubrzava i olakšava cijeli proces.

## Tim

- **Student A**: Džana Dugonjić - resurs: `/resursi_a`
- **Student B**: Danijela Mihajlović - resurs: `/adopters`

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi

### Resurs A: `/resursi_a`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/resursi_a` | Lista svih resursa (sa query filterom) |
| GET | `/resursi_a/{id}` | Dohvatanje resursa po ID-u |
| POST | `/resursi_a` | Kreiranje novog resursa |
| PUT | `/resursi_a/{id}` | Potpuna zamjena resursa |
| PATCH | `/resursi_a/{id}` | Djelimično ažuriranje resursa |
| DELETE | `/resursi_a/{id}` | Brisanje resursa |

**Primjer zahtjeva:**
```bash
# Kreiranje novog resursa
curl -X POST "http://localhost:8000/resursi_a" \
  -H "Content-Type: application/json" \
  -d '{"polje1": "vrijednost", "polje2": 123}'
```

### Resurs B: `/adopters`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/adopters` | Lista svih resursa (sa query filterom) |
| GET | `/adopters/{id}` | Dohvatanje resursa po ID-u |
| POST | `/adopters` | Kreiranje novog resursa |
| PUT | `/adopters/{id}` | Potpuna zamjena resursa |
| PATCH | `/adopters/{id}` | Djelimično ažuriranje resursa |
| DELETE | `/adopters/{id}` | Brisanje resursa |

**Primjeri zahtjeva:**
#Kreiranje novog udomitelja
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

#Dohvatanje udomitelja koji imaju prethodno iskustvo
curl -X 'GET' \
  'http://localhost:8000/adopters?experience=true' \
  -H 'accept: application/json'

#Dohvatanje detalja o udomitelju sa ID-om 1
curl -X 'GET' \
  'http://localhost:8000/adopters/1' \
  -H 'accept: application/json'

#Potpuna zamjena podataka za udomitelja sa ID-om 1
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

#Promjena samo broja telefona za udomitelja sa ID-om 1
curl -X 'PATCH' \
  'http://localhost:8000/adopters/1' \
  -H 'Content-Type: application/json' \
  -d '{
  "phone_number": "062999888"
}'

#Brisanje udomitelja po ID-u
curl -X 'DELETE' \
  'http://localhost:8000/adopters/1' \
  -H 'accept: */*'

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** Gemini

**Primjer 1:**
- **Prompt:** [Npr. "Kreiraj SQLModel klasu za entitet Knjiga sa poljima naslov, autor, godina, isbn"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Da li ste morali prilagoditi generisani kod]

**Primjer 2:**
- **Prompt:** Kako bih mogla implementirati get metodu u kojoj dohvatamo podatke po ID-u?
- **Kako je pomoglo:** AI mi je napisao kod za traženu metodu, te mi je objasnio kako taj kod radi.
- **Prilagodbe:** Generisani kod je bio ispravno napisan tako da ga nisam morala prilagođavati

## Napomene

[Dodatne napomene specifične za vašu implementaciju]