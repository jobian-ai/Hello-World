SELECT *, MAX(LOA) FROM tmp GROUP BY ECI
HAVING COUNT(ECI) >1

SELECT * FROM tmp INNER JOIN 
(
SELECT * FROM tmp GROUP BY ECI
HAVING COUNT(ECI) >1 AND LOA < 202206
) z
ON tmp.ECI = z.ECI

DELETE FROM tmp INNER JOIN 
(
SELECT * FROM tmp GROUP BY ECI
HAVING COUNT(ECI) >1 AND LOA < 202206
) z
ON tmp.ECI = z.ECI


	 
		