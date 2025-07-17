# Importăm clasa Flask și SQLAlchemy pentru a crea aplicația și a gestiona baza de date
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inițializăm obiectul global de tip SQLAlchemy (fără a-l lega de o aplicație Flask încă)
db = SQLAlchemy()

# Funcție care creează și configurează aplicația Flask
def create_app():
    # Creăm o instanță a aplicației Flask
    app = Flask(__name__)

    # Setăm o cheie secretă pentru securizarea sesiunilor și a formularului CSRF
    app.config['SECRET_KEY'] = 'supersecret123'

    # Specificăm calea către baza de date SQLite (fișier local numit angajati.db)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///angajati.db'

    # Dezactivăm urmărirea modificărilor obiectelor (pentru optimizare)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Legăm baza de date de aplicația Flask
    db.init_app(app)

    # Importăm și înregistrăm blueprint-ul pentru rutele aplicației
    from .routes import main
    app.register_blueprint(main)

    # Returnăm aplicația configurată
    return app
