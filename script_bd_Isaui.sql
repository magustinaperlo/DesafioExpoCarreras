DROP DATABASE IF EXISTS `isaui`;
CREATE DATABASE `isaui`;
USE isaui;

///Crea la tabla "carreras"
  
DROP TABLE IF EXISTS `carreras`;
CREATE TABLE `carreras`(
  `id_carreras` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_carreras`)
  );

//Crea la tabla "personas"
DROP TABLE IF EXISTS `personas` ;
CREATE TABLE `personas` (
  `id_persona` INT NOT NULL AUTO_INCREMENT,
  `apellido` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `dni` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(45) NOT NULL,
  `domicilio` VARCHAR(45) NOT NULL,
  `ciudad` VARCHAR(45) NOT NULL,
  `instagram` VARCHAR(45) NOT NULL,
  `id_carreras` INT NOT NULL,
  PRIMARY KEY (`id_persona`),
  FOREIGN KEY (`id_carreras`) references carreras(`id_carreras`)
  );

-------------------------------------------------------------------------------------------------------
//Ingresa las carreras en la tabla carreras
USE isaui;
INSERT INTO carreras (nombre) VALUES ("Software"), ("Enfermeria"), ("Diseño de Espacios"), ("Guia de Trekking"), ("Guia de Turismo"), ("Turismo y Hoteleria");
INSERT INTO personas (apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram, id_carreras) 
VALUES ("Perez", "Jorge", "123", "3451", "ASD@", "peru", "hola", "lechuga", 2),
("Juarez", "Jorgelina", "33546788", "345156787", "ASD@gmail.com", "peru 89", "VCP", "lechugaOk", 1),
("Aper", "Claudia", "33546788", "345156787", "ASD@gmail.com", "peru 89", "VCP", "lechugaOk", 6),
("Maschio", "Evelina", "33546788", "345156787", "ASD@gmail.com", "peru 89", "VCP", "lechugaOk", 4),
("Suarez", "Julieta", "33546788", "345156787", "ASD@gmail.com", "peru 89", "VCP", "lechugaOk", 3),
("Moreno", "Nehuen", "33546788", "345156787", "ASD@gmail.com", "peru 89", "VCP", "lechugaOk", 1),
("Murua", "Luz", "33546788", "345156787", "ASD@gmail.com", "peru 89", "VCP", "lechugaOk", 5);


SELECT * FROM carreras;