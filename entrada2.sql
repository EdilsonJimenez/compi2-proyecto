CREATE INDEX index1 ON tabla2 (col1);


-- funcion 

create or replace funtion cocoa (nombre integer, apellido integer) returns 90 
DECLARE
x integer = 24; 

begin

CASE nombre

WHEN 24, 12 THEN
x = 2;

WHEN 21, 2 THEN
x = 6;

ELSE 

x = 12;
END CASE;

end language sql; 


cocoa(1,1);

  







