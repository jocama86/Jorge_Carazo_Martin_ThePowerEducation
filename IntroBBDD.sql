-- EJERCICIO INICIAL BBDD - Máster en Ciberseguridad
-- ALUMNO: Jorge Carazo Martín
--
-- Consulta 1 --
SELECT flight_id, flight_no, status, FROM flights WHERE status = 'On Time';

-- Consulta 2 --
SELECT * FROM bookings WHERE total_amount >= '1000000';

-- Consulta 3 --
SELECT * FROM aircrafts_data;

-- Consulta 4 --
SELECT flight_id, flight_no FROM flights WHERE aircrafts_code = '733';

-- Consulta 5 --
SELECT * FROM tickets WHERE passenger_name LIKE 'IRINA%';


-- NOTA --
-- Para realizar los ejercicios he ido extendiendo la consulta, es decir, primero seleccionaba 
-- todos de una tabla e iba añadiendo restricciones hasta lograr la consulta deseada.
--