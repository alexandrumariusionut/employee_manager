# Importăm clasa date pentru a seta data angajării la ziua curentă implicit
from datetime import date

# Importăm obiectul db (SQLAlchemy) din aplicație pentru a defini modelul bazei de date
from app import db

# Definim clasa Angajat care va reprezenta tabela "angajati" în baza de date
class Angajat(db.Model):
    # Numele explicit al tabelei în baza de date
    __tablename__ = "angajati"

    # Coloana ID - cheie primară, incrementată automat
    id = db.Column(db.Integer, primary_key=True)

    # Coloana pentru nume - șir de caractere, obligatoriu (nu poate fi NULL)
    nume = db.Column(db.String(100), nullable=False)

    # Coloana pentru prenume - șir de caractere, obligatoriu
    prenume = db.Column(db.String(100), nullable=False)

    # Coloana pentru CNP - unic și obligatoriu (constrângere UNIQUE)
    cnp = db.Column(db.String(13), unique=True, nullable=False)

    # Coloana pentru vârstă - număr întreg, obligatoriu
    varsta = db.Column(db.Integer, nullable=False)

    # Coloana pentru departament - șir de caractere, obligatoriu
    departament = db.Column(db.String(50), nullable=False)

    # Coloana pentru funcție - șir de caractere, obligatoriu
    functie = db.Column(db.String(100), nullable=False)

    # Coloana pentru data angajării - dată, implicit se setează la data curentă
    data_angajare = db.Column(db.Date, default=date.today)

    # Coloana pentru salariul brut - număr zecimal, obligatoriu
    salariu_brt = db.Column(db.Float, nullable=False)

    
