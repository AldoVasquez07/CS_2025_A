from flask import Flask
from entity.models import db
from services.autor.routes import autor_bp
from services.libro.routes import libro_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin_lib:123456@localhost/db_library_cs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registrar Blueprints
app.register_blueprint(autor_bp, url_prefix="/api/autores")
app.register_blueprint(libro_bp, url_prefix="/api/libros")

if __name__ == "__main__":
    app.run(debug=True)
