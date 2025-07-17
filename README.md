# Employee Manager App

O aplicație simplă de gestionare a angajaților, construită cu Flask, SQLAlchemy și WTForms.

## Cuprins

* [Descriere](#descriere)
* [Tehnologii](#tehnologii)
* [Structura proiectului](#structura-proiectului)
* [Instalare](#instalare)
* [Utilizare](#utilizare)
* [Configurare mediu virtual](#configurare-mediu-virtual)
* [Rute principale](#rute-principale)
* [Modele și formular](#modele-și-formular)
* [Contribuții](#contribuții)
* [Licență](#licență)

## Descriere

Aplicația permite:

* Adăugarea, listarea, căutarea, editarea și ștergerea angajaților.
* Sortarea angajaților după nume, dată de angajare sau departament.
* Generarea fluturașului salarial cu calcul CAS, CASS și impozit.
* Exportul listei angajaților într-un fișier CSV.

## Tehnologii

* **Python** 3.9+
* **Flask** – micro-framework web
* **Flask-WTF** – integrare WTForms pentru formulare și CSRF
* **WTForms** – validarea câmpurilor de formular
* **Flask-SQLAlchemy** – ORM pentru interacțiunea cu baza SQLite
* **SQLite** – bază de date relațională locală
* **Jinja2** – motor de template-uri HTML

## Structura proiectului

```
employee_manager/
├── run.py              # Punctul de intrare (factory pattern)
├── requirements.txt    # Dependențe proiect
└── app/
    ├── __init__.py     # Inițializarea Flask și SQLAlchemy
    ├── models.py       # Definirea clasei Angajat (tabela angajati)
    ├── forms.py        # Definirea formularului AngajatForm
    ├── routes.py       # Rutele aplicației (CRUD, export CSV, fluturaș)
    └── templates/      # Șabloanele HTML
        ├── base.html
        ├── home.html
        ├── add.html
        ├── lista_angajati.html
        └── ...
```

## Instalare

1. Clonează repository:

   ```bash
   git clone https://github.com/<utilizator>/<repo>.git
   cd <repo>
   ```

2. Creează și activează un mediu virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalează dependențele:

   ```bash
   pip install -r requirements.txt
   ```

4. Pornește aplicația:

   ```bash
   python run.py
   ```

Aplicația va fi accesibilă la `http://127.0.0.1:5000/`.

## Utilizare

* Navighează la **Home** pentru linkuri rapide.
* **Adaugă** un angajat prin meniul `adauga`.
* **Listează** angajații prin `angajati`.
* **Caută** angajați după CNP.
* **Editează**/șterge un angajat din listă.
* Vezi **fluturașul salarial** prin `fluturas/<cnp>`.
* Exportă CSV cu `export_csv`.

## Rute principale

| Rută                                    | Descriere                 |
| --------------------------------------- | ------------------------- |
| `/`                                     | Pagina principală         |
| `/adauga`                               | Formular adăugare angajat |
| `/angajati`                             | Listă angajați            |
| `/cauta?cnp=<CNP>`                      | Caută angajat după CNP    |
| `/editeaza/<cnp>`                       | Editare angajat           |
| `/sterge/<cnp>`                         | Ștergere angajat          |
| `/salarii_total`                        | Sumă brută totală         |
| `/salarii_departament/<nume>`           | Sumă brută pe departament |
| `/fluturas/<cnp>`                       | Fluturaș salarial         |
| `/angajati_sortati?criteriu=<criteriu>` | Sortare angajați          |
| `/export_csv`                           | Export CSV                |

## Modele și formular

* **models.py** definește `class Angajat(db.Model)` cu coloanele: `id`, `nume`, `prenume`, `cnp`, `varsta`, `departament`, `functie`, `data_angajare`, `salariu_brt`.
* **forms.py** definește `class AngajatForm(FlaskForm)` cu câmpuri și validatori pentru fiecare atribut.

## Contribuții

Contribuțiile sunt binevenite! Fork & Pull request.

## Licență

MIT © 2025 Alexandru Marius
