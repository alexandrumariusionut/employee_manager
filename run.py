# run.py
from app import create_app

app = create_app()

from app import db
from app.models import Angajat




if __name__ == "__main__":
    app.run(debug=True)
