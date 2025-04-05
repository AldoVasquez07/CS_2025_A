# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Autor(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    nacionalidad = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.Date)

    libros = db.relationship('Libro', backref='autor', cascade="all, delete", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad,
            "fecha_nacimiento": self.fecha_nacimiento.isoformat() if self.fecha_nacimiento else None
        }

class Libro(db.Model):
    __tablename__ = 'libro'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    genero = db.Column(db.String(50))
    fecha_publicacion = db.Column(db.Date)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "fecha_publicacion": self.fecha_publicacion.isoformat() if self.fecha_publicacion else None,
            "autor_id": self.autor_id,
            "autor": self.autor.nombre if self.autor else None
        }
