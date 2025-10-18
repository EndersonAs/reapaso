CREATE DATABASE economia;
use economia;
select * FROM tabla_pib;
select * FROM tabla_poblacion;

CREATE TABLE tabla_final(
SELECT tabla_pib.*, tabla_poblacion.Poblacion FROM tabla_pib
LEFT JOIN tabla_poblacion
ON tabla_pib.pais = tabla_poblacion.Pais 
);

SELECT * FROM tabla_final;
