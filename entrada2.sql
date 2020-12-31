-- funcion 

create or replace funtion cocoa (nombre integer, apellido integer) returns 90 
DECLARE
x integer = 24; 
y integer = 25;

begin

CASE 
WHEN nombre = 1 THEN
CASE x

WHEN 12 THEN

y = 12;
ELSE

y = 24;

END CASE;

WHEN nombre = 2 THEN


CASE x 

WHEN 4 THEN

y = 32;

END CASE;

ELSE 

x = 100;

END CASE;

end language sql; 


cocoa(1,1);

  

















