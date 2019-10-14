dict(comments= "IQ DEV<>PROD DMBalance StageID counts diff", 
	source=dict(
		IQ_DEV= """

SELECT StageID, count(1) cnt_DEV
  FROM CIGActgS11.DMBalance 
 WHERE StageID in (184990,184991) 
 GROUP BY StageID

 
		""",
		IQ_PROD= """

SELECT StageID, count(1) cnt_PROD
  FROM CIGActgS11.DMBalance 
 WHERE StageID in (184990,184991) 
 GROUP BY StageID

		"""
	), 
	compare=dict( #full outer join hack
		IQ_diff=""" 
SELECT d.StageID,
 d.cnt_DEV, c.cnt_PROD, c.cnt_PROD-d.cnt_DEV diff
FROM {IQ_DEV} d
LEFT JOIN {IQ_PROD} c USING(StageID)
UNION ALL
SELECT c.StageID,
 c.cnt_PROD, d.cnt_DEV, d.cnt_DEV -c.cnt_PROD diff
FROM {IQ_PROD} c
LEFT JOIN {IQ_DEV} d USING(StageID)
WHERE d.StageID IS NULL
		"""
	)
)