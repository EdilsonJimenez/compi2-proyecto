CREATE INDEX test1_id_index 		ON test1 	(id);
CREATE INDEX name 			ON table2 	USING HASH (column2);
CREATE INDEX test2_mm_idx 		ON test2 	(major, minor);
CREATE INDEX test2_info_nulls_low 	ON test2 	(info NULLS FIRST);
CREATE INDEX test3_desc_index 		ON test3 	(id DESC NULLS LAST);
CREATE INDEX mytable_cat_1 		ON mytable 	(data) 		WHERE category = 1;
CREATE INDEX mytable_cat_2 		ON mytable 	(data) 		WHERE category = 2;
