CREATE DATABASE IF NOT EXISTS test
    OWNER = root
    MODE = 1;

USE test;


-- funcion 

create or replace funtion cocoa (nombre integer, apellido integer) returns 90 
DECLARE
x integer = 24; 
y integer = 25;

begin


--  primero  Case
CASE 

	WHEN nombre = 1
	THEN
	    CASE x
	    WHEN 12 
	    THEN
		y = 12;
	    ELSE
	       y = 24;

	    END CASE;



	WHEN nombre = 2 
	THEN
    	    CASE x  
            WHEN 4 
            THEN
                y = 32;
	    ELSE
		x=11;

            END CASE;

	WHEN nombre = 4
	THEN
    	    CASE x  
            WHEN 4 
            THEN
                y = 32;
	    ELSE
		x=800;

            END CASE;

ELSE 
   x = 100;
END CASE;




--  Segundo  Case

CASE 
	WHEN nombre = 1
	THEN
	    CASE x
	    WHEN 12 
	    THEN
		y = 12;
	    ELSE
	       y = 24;

	    END CASE;


	WHEN nombre = 2 
	THEN

    	    CASE x  
            WHEN 4 
            THEN
                y = 32;

	    WHEN 5 
            THEN
                y = 32;
	    ELSE
		x=11;

            END CASE;


	
	WHEN nombre = 4
	THEN
    	    CASE x  
            WHEN 4 
            THEN
                y = 32;
	    ELSE
		x=9200;

            END CASE;

ELSE 
   x = 100;
END CASE;


end language sql; 


cocoa(4,1);

  





























