from flask import Blueprint, request, jsonify
from entity.models import db, Autor

autor_bp = Blueprint('autor_bp', __name__)

@autor_bp.route("/", methods=["GET"])
def get_autores():
    autores = Autor.query.all()
    return jsonify([a.to_dict() for a in autores])

@autor_bp.route("/<int:id>", methods=["GET"])
def get_autor(id):
    autor = Autor.query.get_or_404(id)
    return jsonify(autor.to_dict())

@autor_bp.route("/", methods=["POST"])
def crear_autor():
    data = request.get_json()
    nuevo = Autor(
        nombre=data['nombre'],
        nacionalidad=data.get('nacionalidad'),
        fecha_nacimiento=data.get('fecha_nacimiento')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

@autor_bp.route("/<int:id>", methods=["PUT"])
def actualizar_autor(id):
    autor = Autor.query.get_or_404(id)
    data = request.get_json()
    autor.nombre = data.get('nombre', autor.nombre)
    autor.nacionalidad = data.get('nacionalidad', autor.nacionalidad)
    autor.fecha_nacimiento = data.get('fecha_nacimiento', autor.fecha_nacimiento)
    db.session.commit()
    return jsonify(autor.to_dict())

@autor_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_autor(id):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return jsonify({"mensaje": "Autor eliminado"})
