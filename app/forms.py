# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp, ValidationError

def valid_cnp(form, field):
    if not field.data.isdigit() or len(field.data) != 13:
        raise ValidationError("CNP-ul trebuie să conțină exact 13 cifre.")

class AngajatForm(FlaskForm):
    nume = StringField("Nume", validators=[DataRequired(), Length(min=2, max=100)])
    prenume = StringField("Prenume", validators=[DataRequired(), Length(min=2, max=100)])
    cnp = StringField("CNP", validators=[DataRequired(), valid_cnp])
    varsta = IntegerField("Vârstă", validators=[DataRequired(), NumberRange(min=18, message="Vârsta minimă este 18 ani.")])
    departament = StringField("Departament", validators=[DataRequired()])
    functie = StringField("Funcție", validators=[DataRequired()])
    salariu_brt = FloatField("Salariu Brut", validators=[DataRequired(), NumberRange(min=4050, message="Salariul minim este 4050 RON.")])
    submit = SubmitField("Adaugă angajat")
