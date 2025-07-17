# Importăm clasele necesare din Flask-WTF și WTForms pentru a crea și valida formulare
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

# Funcție personalizată de validare pentru câmpul CNP
def valid_cnp(form, field):
    # Obținem valoarea, înlocuim None cu șir gol
    valoare = field.data or ""
    # Îndepărtăm spațiile albe în exces
    valoare = valoare.strip()
    # Verificăm dacă sunt doar cifre și lungimea e exact 13
    if not valoare.isdigit() or len(valoare) != 13:
        raise ValidationError("CNP-ul trebuie să conțină exact 13 cifre.")


# Definim clasa formularului pentru adăugarea unui angajat
class AngajatForm(FlaskForm):
    # Câmp pentru numele angajatului – obligatoriu, lungime între 2 și 100 caractere
    nume = StringField("Nume", validators=[DataRequired(), Length(min=2, max=100)])
    
    # Câmp pentru prenume – obligatoriu, lungime între 2 și 100 caractere
    prenume = StringField("Prenume", validators=[DataRequired(), Length(min=2, max=100)])
    
    # Câmp pentru CNP – validare personalizată pentru 13 cifre
    cnp = StringField("CNP", validators=[DataRequired(), valid_cnp])
    
    # Câmp pentru vârstă – obligatoriu, minim 18 ani
    varsta = IntegerField("Vârstă", validators=[DataRequired(), NumberRange(min=18, message="Vârsta minimă este 18 ani.")])
    
    # Câmp pentru departament – obligatoriu
    departament = StringField("Departament", validators=[DataRequired()])
    
    # Câmp pentru funcție – obligatoriu
    functie = StringField("Funcție", validators=[DataRequired()])
    
    # Câmp pentru salariul brut – obligatoriu, minim 4050 RON
    salariu_brt = FloatField("Salariu Brut", validators=[DataRequired(), NumberRange(min=4050, message="Salariul minim este 4050 RON.")])
    
    # Buton pentru trimiterea formularului
    submit = SubmitField("Adaugă angajat")
