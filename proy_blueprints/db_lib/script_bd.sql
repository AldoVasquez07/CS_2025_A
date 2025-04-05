CREATE TABLE autor (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE
);

-- Crear tabla de libros
CREATE TABLE libro (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    genero VARCHAR(50),
    fecha_publicacion DATE,
    autor_id INTEGER NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES autor(id) ON DELETE CASCADE
);

-- Insertar autores
INSERT INTO autor (nombre, nacionalidad, fecha_nacimiento) VALUES
('Gabriel García Márquez', 'Colombiana', '1927-03-06'),
('Mario Vargas Llosa', 'Peruana', '1936-03-28');

-- Insertar libros
INSERT INTO libro (titulo, genero, fecha_publicacion, autor_id) VALUES
('Cien años de soledad', 'Realismo mágico', '1967-05-30', 1),
('El amor en los tiempos del cólera', 'Romance', '1985-09-05', 1),
('La ciudad y los perros', 'Drama', '1963-10-10', 2);
