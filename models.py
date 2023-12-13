from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    numero_cuenta = db.Column(db.String(20), unique=True, nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(60), nullable=False)
    facultad = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Usuario('{self.nombres}', '{self.apellidos}', '{self.correo}')"
