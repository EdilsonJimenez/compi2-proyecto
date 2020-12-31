CREATE INDEX test1_id_index 		ON test1 	(id);
CREATE INDEX name 			ON table2 	USING HASH (column2);
CREATE INDEX test2_mm_idx 		ON test2 	(major, minor);
CREATE INDEX test2_info_nulls_low 	ON test2 	(info NULLS FIRST);
CREATE INDEX test3_desc_index 		ON test3 	(id DESC NULLS LAST);
CREATE INDEX mytable_cat_1 		ON mytable 	(data) 		WHERE category = 1;
CREATE INDEX mytable_cat_2 		ON mytable 	(data) 		WHERE category = 2;




-- funcion 
create or replace procedure cocoa () 

DECLARE
	x integer =24; 
begin
case x 
    when 10 then x=20;
end case;

end language sql; 



# -------------------------------   Funciones 

create or replace funtion cocoa (parametro1 integer, parametro2 integer,parametro3 integer ) returns 34 

DECLARE
	x integer =24; 
begin

ID = Dbbu(8989,7878);

Ejecucion(parametro1,parametro2,parametro3,parametro4);

case x 
    when 10 then x=20;
end case;

end language sql;







Ejecucion(parametro1,parametro2,parametro3,parametro4);






-- Procedimiento 
create or replace procedure cocoa () 
as dato 

select * from tabla1; 

DECLARE
	x integer =24; 
begin

for noonos in  67 
    loop 

    select * from tabla1; 
		
    end loop;  
case x 
    when 10 then x=20;
end case;

exit ;

exit cola;

exit fifo when id=10;

continue ;
continue cola;

continue fifo when id=10;

loop 
 x integer =24; 
end loop;

end language sql; 







-- Procedimiento 2 
create or replace procedure cocoa () 
as FF 
DECLARE
	x integer =24; 

begin

for elemento in 1,2,3,4,5,6 
    loop 

    select * from tabla1; 
	
		
    end loop;  

end language sql; 






-- Procedimiento 3
create or replace procedure cocoa () language sql 

begin
end language sql; 




















