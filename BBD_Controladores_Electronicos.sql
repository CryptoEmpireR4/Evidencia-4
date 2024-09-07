CREATE DATABASE articulos_electronicos;
CREATE TABLE marcas (
    id_marca INT PRIMARY KEY,
    marca VARCHAR(50),
    importadora VARCHAR(50)
);
CREATE TABLE ControladoresDJ(
	id INT PRIMARY KEY,
    nombre VARCHAR(50),
    id_marca INT,
    modelo VARCHAR(50),
    velocidad_play_canal_1 INT,
    velocidad_play_canal_2 INT,
    salida_canal_1 VARCHAR(50),
    salida_canal_2 VARCHAR(50),
	graves_vol_canal_1 FLOAT,
    medios_vol_canal_1 FLOAT,
    agudos_vol_canal_1 FLOAT,
	graves_vol_canal_2 FLOAT,
    medios_vol_canal_2 FLOAT,
    agudos_vol_canal_2 FLOAT
    );
INSERT INTO marcas VALUES (1,"CASIO","CASIO ARGENTINA SA");
INSERT INTO marcas VALUES (2,"PIONNER","PIONNER ARG SRL");
INSERT INTO marcas VALUES (3,"NUMARK","CONTROLADORES SA");
INSERT INTO marcas VALUES (4,"HERCULES","PIONNER ARG SRL");
INSERT INTO controladoresDJ(id,nombre,id_marca,modelo) VALUES (1,"PionnerDJ",2,"DJMixer");
INSERT INTO controladoresDJ(id,nombre,id_marca,modelo) VALUES (2,"Numark Party",3,"Party Mix LI");
INSERT INTO controladoresDJ(id,nombre,id_marca,modelo) VALUES (3,"DJ Hercules",4,"Comtrol Impulse 200");
INSERT INTO controladoresDJ(id,nombre,id_marca,modelo) VALUES (4,"Pionner2000",2,"DJMixer2000");
INSERT INTO controladoresDJ(id,nombre,id_marca,modelo) VALUES (5,"GShockDJ",1,"GSHOCK2024");
INSERT INTO controladoresDJ(id,nombre,id_marca,modelo) VALUES (6,"EdifficeDJ",1,"CasioEdiffice");
SELECT nombre FROM controladoresDJ LEFT JOIN marca ON controladoresDJ.id_marca=id_marca;
SELECT marca FROM marcas;
SELECT modelo FROM controladoresDJ LEFT JOIN marca ON controladoresDJ.id_marca=id_marca;
SELECT*FROM controladoresDJ WHERE id_marca=1;
SELECT*FROM marcas WHERE importadora="PIONNER ARG SRL"; 