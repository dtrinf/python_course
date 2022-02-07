create database reto7;
\c reto7

CREATE TABLE IF NOT EXISTS Libro(
    ClaveLibro      INT PRIMARY KEY NOT NULL,
    Titulo          VARCHAR(100) NOT NULL,
    Idioma          VARCHAR(30),
    Formato         VARCHAR(50),
    ClaveEditorial  INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Tema(
    ClaveTema   INT PRIMARY KEY NOT NULL,
    Nombre      VARCHAR(50)
);
    
CREATE TABLE IF NOT EXISTS Autor(
    ClaveAutor  INT PRIMARY KEY NOT NULL,
    Nombre      VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Editorial(
    ClaveEditorial  INT PRIMARY KEY NOT NULL,
    Nombre          VARCHAR(50),
    Direccion       VARCHAR(200),
    Telefono        INT
);

CREATE TABLE IF NOT EXISTS Ejemplar(
    ClaveEjemplar   INT PRIMARY KEY NOT NULL,
    ClaveLibro      INT,
    NumeroOrden     VARCHAR(30),
    Edicion         VARCHAR(10),
    Ubicacion       VARCHAR(100),
    Categoria       VARCHAR(100),
    CONSTRAINT FK_ClaveLibro FOREIGN KEY (ClaveLibro) REFERENCES Libro(ClaveLibro)
);

CREATE TABLE IF NOT EXISTS Socio(
    ClaveSocio  INT PRIMARY KEY,
    Nombre      VARCHAR(50),
    Direccion   VARCHAR(100),
    Telefono    INT,
    Categoria   VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Prestamo(
    ClaveSocio          INT,
    ClaveEjemplar       INT,
    NumeroOrden         INT,
    Fecha_prestamo      DATE NOT NULL, 
    Fecha_devolucion    DATE NOT NULL,
    Notas               VARCHAR(500),
    CONSTRAINT PK_Prestamo PRIMARY KEY (ClaveSocio, ClaveEjemplar, NumeroOrden),
    CONSTRAINT FK_ClaveSocio FOREIGN KEY (ClaveSocio) REFERENCES Socio(ClaveSocio),
    CONSTRAINT FK_ClaveEjemplar FOREIGN KEY (ClaveEjemplar) REFERENCES Ejemplar(ClaveEjemplar)
);

CREATE TABLE IF NOT EXISTS Trata_sobre(
    ClaveLibro  INT,
    ClaveTema   INT,
    CONSTRAINT PK_Trata_sobre PRIMARY KEY (ClaveLibro, ClaveTema),
    CONSTRAINT FK_ClaveLibro FOREIGN KEY (ClaveLibro) REFERENCES Libro(ClaveLibro),
    CONSTRAINT FK_ClaveTema FOREIGN KEY (ClaveTema) REFERENCES Tema(ClaveTema)
);

CREATE TABLE IF NOT EXISTS Escrito_por(
    ClaveLibro  INT,
    ClaveAutor  INT,
    CONSTRAINT PK_Escrito_por PRIMARY KEY (ClaveLibro, ClaveAutor),
    CONSTRAINT FK_ClaveLibro FOREIGN KEY (ClaveLibro) REFERENCES Libro(ClaveLibro),
    CONSTRAINT FK_ClaveAutor FOREIGN KEY (ClaveAutor) REFERENCES Autor(ClaveAutor)
);

\dt

