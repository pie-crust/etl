dict(comments= "DMBalance StageID counts test", 
	source=dict(
		SQLServer_DEV= """

SELECT StageID, count(1) cnt_DEV
  FROM Accounting2019.CIGActgH.DMBalance 
 WHERE StageID in (184990,184991) 
 GROUP BY StageID
		""",
		SQLServer_PROD= """

SELECT StageID, count(1) cnt_PROD
  FROM Accounting2019.CIGActgH.DMBalance 
 WHERE StageID in (184990,184991) 
 GROUP BY StageID

		"""
	), 
	compare=dict( #full outer join hack
		SQLServer_diff=""" 
SELECT d.StageID,
 d.cnt_DEV, c.cnt_PROD, c.cnt_PROD-d.cnt_DEV diff
FROM {SQLServer_DEV} d
LEFT JOIN {SQLServer_PROD} c USING(StageID)
UNION ALL
SELECT c.StageID,
 c.cnt_PROD, d.cnt_DEV, d.cnt_DEV -c.cnt_PROD diff
FROM {SQLServer_PROD} c
LEFT JOIN {SQLServer_DEV} d USING(StageID)
WHERE d.StageID IS NULL
		"""
	)
)