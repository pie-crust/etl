dict(comments= "DMBalance StageID counts test", 
	source=dict(
		IQ= """

SELECT StageID , count(1) cnt
  FROM CIGActgS11.DMBalance 
 WHERE StageID IN (184990,184991) 
 GROUP BY StageID

		""",
		SQLServer= """

SELECT StageID, count(1) cnt
  FROM Accounting2019.CIGActgH.DMBalance 
 WHERE StageID in (184990,184991) 
 GROUP BY StageID

		"""
	), 
	compare=dict( #full outer join hack
		diff=""" 
SELECT * FROM  (
SELECT d.StageID,
 d.cnt, c.cnt, c.cnt-d.cnt diff
FROM {IQ} d
LEFT JOIN {SQLServer} c USING(StageID)
UNION ALL
SELECT c.StageID,
 c.cnt, d.cnt, d.cnt -c.cnt diff
FROM {SQLServer} c
LEFT JOIN {IQ} d USING(StageID)
WHERE d.StageID IS NULL) t WHERE diff > 0
		""",
		match="""

SELECT a.StageID, a.cnt
FROM {IQ} a, {SQLServer} b
WHERE a.StageID=b.StageID 
  AND a.cnt= b.cnt

		""",
		unmatch="""

SELECT a.StageID, a.cnt, b.cnt, a.cnt-b.cnt diff
FROM {IQ} a, {SQLServer} b
WHERE a.StageID=b.StageID 
  AND a.cnt!= b.cnt

		"""
	)
)