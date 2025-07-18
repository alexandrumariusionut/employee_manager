from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Angajat
from app.forms import AngajatForm
from datetime import date
import csv
from io import StringIO
from flask import Response

# Inițializăm blueprint-ul pentru gestionarea rutelor
main = Blueprint("main", __name__)

# Ruta principală – afișează pagina de start (home)
@main.route("/")
def home():
    return render_template("home.html")


# Ruta pentru adăugarea unui nou angajat (GET pentru formular, POST pentru trimiterea lui)
@main.route("/adauga", methods=["GET", "POST"])
def adauga_angajat():
    form = AngajatForm()
    if form.validate_on_submit():
        angajat = Angajat(
            nume=form.nume.data,
            prenume=form.prenume.data,
            cnp=form.cnp.data,
            varsta=form.varsta.data,
            departament=form.departament.data,
            functie=form.functie.data,
            salariu_brt=form.salariu_brt.data,
            data_angajare=date.today()
        )
        db.session.add(angajat)
        db.session.commit()
        flash("Angajatul a fost adăugat cu succes!", "success")
        return redirect(url_for("main.home"))
    return render_template("add.html", form=form)


# Ruta care afișează toți angajații din baza de date
@main.route("/angajati")
def lista_angajati():
    angajati = Angajat.query.all()
    return render_template("lista_angajati.html", angajati=angajati)


# Ruta care caută un angajat după CNP (primit prin query string)
@main.route("/cauta")
def cauta_angajat():
    from flask import request
    cnp = request.args.get("cnp")
    angajat = Angajat.query.filter_by(cnp=cnp).first()
    if not angajat:
        flash("Angajatul nu a fost găsit.", "warning")
        return redirect(url_for("main.lista_angajati"))
    return render_template("angajat_detalii.html", angajat=angajat)


# Ruta pentru editarea unui angajat existent (identificat prin CNP)
@main.route("/editeaza/<cnp>", methods=["GET", "POST"])
def editeaza_angajat(cnp):
    angajat = Angajat.query.filter_by(cnp=cnp).first_or_404()
    from app.forms import AngajatForm
    form = AngajatForm(obj=angajat)

    if form.validate_on_submit():
        angajat.nume = form.nume.data
        angajat.prenume = form.prenume.data
        angajat.varsta = form.varsta.data
        angajat.departament = form.departament.data
        angajat.functie = form.functie.data
        angajat.salariu_brt = form.salariu_brt.data
        db.session.commit()
        flash("Datele angajatului au fost actualizate.", "success")
        return redirect(url_for("main.lista_angajati"))

    return render_template("edit_angajat.html", form=form, cnp=cnp)


# Ruta pentru ștergerea unui angajat (prin metoda POST)
@main.route("/sterge/<cnp>", methods=["POST"])
def sterge_angajat(cnp):
    angajat = Angajat.query.filter_by(cnp=cnp).first_or_404()
    db.session.delete(angajat)
    db.session.commit()
    flash("Angajatul a fost șters.", "info")
    return redirect(url_for("main.lista_angajati"))


# Ruta care calculează suma salariilor brute pentru toți angajații
@main.route("/salarii_total")
def salarii_total():
    total = db.session.query(db.func.sum(Angajat.salariu_brt)).scalar() or 0
    return render_template("salarii_total.html", total=total)



# Ruta care generează fluturașul salarial pentru un angajat după CNP
@main.route("/fluturas/<cnp>")
def fluturas_salarial(cnp):
    angajat = Angajat.query.filter_by(cnp=cnp).first_or_404()
    brut = angajat.salariu_brt
    cas = round(brut * 0.10, 2)
    cass = round(brut * 0.25, 2)
    impozit = round((brut - cas - cass) * 0.10, 2)
    net = round(brut - cas - cass - impozit, 2)

    return render_template("fluturas.html", angajat=angajat, cas=cas, cass=cass, impozit=impozit, net=net)




# Ruta care exportă datele tuturor angajaților într-un fișier CSV (inclusiv salariul net calculat)
@main.route("/export_csv")
def export_csv():
    angajati = Angajat.query.all()

    # Funcție internă care calculează salariul net pe baza brutului
    def calculeaza_net(brut: float) -> float:
        cas = brut * 0.10
        cass = brut * 0.25
        impozit = (brut - cas - cass) * 0.10
        return round(brut - cas - cass - impozit, 2)

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Nume", "Prenume", "CNP", "Vârstă", "Funcție", "Departament", "Salariu Brut", "Salariu Net"])

    for angajat in angajati:
        net = calculeaza_net(angajat.salariu_brt)
        writer.writerow([
            angajat.nume,
            angajat.prenume,
            angajat.cnp,
            angajat.varsta,
            angajat.functie,
            angajat.departament,
            angajat.salariu_brt,
            net
        ])

    output.seek(0)
    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=raport_angajati.csv"}
    )
