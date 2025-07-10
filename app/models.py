# app/models.py
from datetime import date
from app import db

class Angajat(db.Model):
    __tablename__ = "angajati"

    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    prenume = db.Column(db.String(100), nullable=False)
    cnp = db.Column(db.String(13), unique=True, nullable=False)
    varsta = db.Column(db.Integer, nullable=False)
    departament = db.Column(db.String(50), nullable=False)
    functie = db.Column(db.String(100), nullable=False)
    data_angajare = db.Column(db.Date, default=date.today)
    salariu_brt = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"<Angajat {self.nume} {self.prenume} - {self.functie}>"
