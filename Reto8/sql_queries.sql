
--- 1.1

select nombre from articulos;

--- 1.2

select nombre,precio from articulos;

--- 1.3

select nombre,precio from articulos where precio >= 200;

--- 1.4

select nombre,precio from articulos where precio between 60 and 120;

--- 1.5

select nombre as "Nombre",precio*166.386 as "Precio pts" from articulos;

--- 1.6

select avg(precio) as "Precio medio" from articulos;

--- 1.7

select avg(precio) as "Precio Medio Fabricante 2" from articulos where fabricante = 2;

--- 1.8

select count(*) from articulos where precio >= 180;

--- 1.9

select nombre,precio from articulos where precio >= 180 order by precio desc, nombre asc;

--- 1.10

select a.codigo,a.nombre,a.precio,a.fabricante,f.nombre from articulos a full outer join fabricantes f on a.fabricante = f.codigo;

--- 1.11

select a.codigo,a.nombre,a.precio,a.fabricante,f.nombre from articulos a full outer join fabricantes f on a.fabricante = f.codigo;

--- 1.12

select fabricante,avg(precio) as "Precio Medio" from articulos group by fabricante order by fabricante;

--- 1.13

select f.nombre,avg(a.precio) as "Precio Medio" from articulos a full outer join fabricantes f on a.fabricante = f.codigo group by f.nombre order by f.nombre;

--- 1.14

select f.nombre,avg(a.precio) as "Precio Medio" from articulos a full outer join fabricantes f on a.fabricante = f.codigo group by f.nombre having avg(a.precio) >= 150 order by f.nombre;

--- 1.15

select nombre,precio from articulos where precio = (select min(precio) from articulos);

--- 1.16

select f.nombre,max(a.precio) from articulos a full outer join fabricantes f on a.fabricante = f.codigo group by a.fabricante,f.nombre order by f.nombre;

--- 1.17

-- insert into articulos(codigo, nombre, precio, fabricante) values (21,'Altavoces', 70, 2);
insert into articulos(codigo, nombre, precio, fabricante) select max(codigo)+1,'Altavoces', 70, 2 from articulos;

--- 1.18

update articulos set nombre = 'Impresora Laser' where codigo = 8;

--- 1.19

update articulos set precio = precio*0.9;

--- 1.20

update articulos set precio = precio - 10 where precio >= 120;

