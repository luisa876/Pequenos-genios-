from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

    if Usuario.query.count() == 0:
        usuario = Usuario(nome="luisa", email="luisa@email.com")
        db.session.add(usuario)
        db.session.commit()

    usuarios = Usuario.query.all()
    for u in usuarios:
        print(f"{u.id} - {u.nome} - {u.email}")

@app.route("/")
def inicio():
    return "Banco funcionando!"

if __name__ == "__main__":
    app.run(debug=True)