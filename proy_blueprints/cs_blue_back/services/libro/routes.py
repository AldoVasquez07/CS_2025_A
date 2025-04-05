from flask import Blueprint, request, jsonify
from entity.models import db, Libro

libro_bp = Blueprint('libro_bp', __name__)

@libro_bp.route("/", methods=["GET"])
def get_libros():
    libros = Libro.query.all()
    return jsonify([l.to_dict() for l in libros])

@libro_bp.route("/<int:id>", methods=["GET"])
def get_libro(id):
    libro = Libro.query.get_or_404(id)
    return jsonify(libro.to_dict())

@libro_bp.route("/", methods=["POST"])
def crear_libro():
    data = request.get_json()
    nuevo = Libro(
        titulo=data['titulo'],
        genero=data.get('genero'),
        fecha_publicacion=data.get('fecha_publicacion'),
        autor_id=data['autor_id']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

@libro_bp.route("/<int:id>", methods=["PUT"])
def actualizar_libro(id):
    libro = Libro.query.get_or_404(id)
    data = request.get_json()
    libro.titulo = data.get('titulo', libro.titulo)
    libro.genero = data.get('genero', libro.genero)
    libro.fecha_publicacion = data.get('fecha_publicacion', libro.fecha_publicacion)
    libro.autor_id = data.get('autor_id', libro.autor_id)
    db.session.commit()
    return jsonify(libro.to_dict())

@libro_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({"mensaje": "Libro eliminado"})
