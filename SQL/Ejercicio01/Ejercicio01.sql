/* Ejercicio Jorge Carzo Martín - Máster en Ciberseguridad*/
/* Ejercicio 1 */


/* Crea una tabla llamada "Clientes" con las columnas: id(entero, clave primaria), nombre (texto), email (texto) */

CREATE TABLE IF NOT EXISTS Clientes(
id int PRIMARY KEY,
nombre VARCHAR(255),
email VARCHAR (255)
)

/* Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre = 'Juan' y mail = 'juan@example.com' */
INSERT INTO Clientes (id, nombre, email)
VALUES(1, 'Juan', 'juan@example.com');

/* Actualizar el email del cliente con id=1 a "juan@gmail.com"*/
UPDATE Clientes
SET email = 'juan@gmail.com'
WHERE id= 1;

/* Elimina el cliente con id = 1 de la tabla "Clientes"*/
DELETE FROM Clientes
WHERE id= 1;

/* Crear una tabla llamada "Pedidos" con las columnas id (entero, clave primaria), cliente_id (entero, clave referenciando a la tabla "Clientes"), producto (texto) y cantidad (entero)) */
CREATE TABLE IF NOT EXISTS Pedidos(
  id int PRIMARY KEY,
  client_id INT REFERENCES Clientes(id),
  producto VARCHAR (255),
  cantidad INT
)

/* Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1, producto="Camiseta" y cantidad=2 */
INSERT INTO Pedidos(id, cliente_id, producto, cantidad)
VALUES(1,1,'Camiseta', 2);

/* ¡¡ IMPORTANTE !! --> Nota: si los ejercicios se hacen en el orden indicado, dara un error ya que no hay registro en la tabla clientes. Asegurarse
de que al menos hay un registro */

/* Actualizar la cantidad del pedido con id=1 a 3 */
UPDATE Pedidos
SET cantidad = 3
WHERE id = 1;

/* Eliminar el pedido con id=1 de la tabla "Pedidos" */
DELETE FROM Pedidos
WHERE id = 1;

/* Crear una tabla llamada "Productos" con las columnas: id (entero, clave primaria), nombre (texto) y precio (decimal) */
CREATE TABLE IF NOT EXISTS Productos(
  id INT PRIMARY KEY,
  nombre VARCHAR (255),
  precio FLOAT  
)

/*  Insertar varios productos en la tabla "Productos" con diferentes valores */
INSERT INTO Productos (id, nombre, precio)
VALUES(1, 'Pantalon', 22.5);

INSERT INTO Productos (id, nombre, precio)
VALUES(2, 'Camisa', 19);

INSERT INTO Productos (id, nombre, precio)
VALUES(3, 'Sudadera', 20.5);

INSERT INTO Productos (id, nombre, precio)
VALUES(4, 'Abrigo', 120.5);


/* Consultar todos los clientes de la tabla "Clientes" */
SELECT * FROM Clientes;

/* Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los clientes correspondientes */
SELECT * FROM Pedidos
INNER JOIN Clientes ON Pedidos.client_id = clientes.id

/* Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50 */
SELECT * FROM Productos
WHERE precio > 50;

/* Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o igual a 5 */
SELECT * FROM Pedidos
WHERE cantidad >= 5

/* Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra "A" */
SELECT * FROM Clientes
WHERE nombre LIKE 'A%'

/* Realizar una consulta que muestre el nombre del cliente y el total de pedidos realizados por cada cliente. */
SELECT Clientes.nombre, COUNT(*) AS Pedidos_totales
FROM Clientes 
JOIN Pedidos ON Clientes.id = Pedidos.client_id 
GROUP BY Clientes.nombre;


/* Realizar una consulta que muestre el nombre del producto y la cantidad total de pedidos de ese producto */
SELECT Productos.nombre, COUNT(*) AS Pedidos_totales_producto
FROM Productos
JOIN Pedidos ON Productos.nombre = Pedidos.producto
GROUP BY Productos.nombre;

/* Esta mal seguro este*/



/* Agregar una columna llamada "fecha" a la tabla "Pedidos" de tipo fecha */
ALTER TABLE Pedidos
ADD COLUMN fecha DATE;


/* Agregar una clave externa a la tabla "Pedidos" que haga referencia a la tabla "Productos" en la columna "producto" */



/* Realizar una consulta que muestre los nombres de los clientes, los nombres de los productos y las cantidades de los pedidos donde coincida la clave externa */