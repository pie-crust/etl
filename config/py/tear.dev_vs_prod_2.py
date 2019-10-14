dict(comments= "DMBalance StageID counts test", 
	source=dict(
		SQLServer= """

select s.StageID, count(1) cnt_SQL 
from Accounting2019.CIGActgH.Stage s
JOIN Accounting2019.CIGActgH.DmBalance d 
on s.StageID=d.StageID
Where s.StageDate >= '12/31/2018'
and Stage= 'EOD'
and CLientID = 223906
group by s.StageID
order by s.StageID

		""",

		IQ= """

select s.StageID, count(1) cnt_IQ
from CIGActgS11.Stage s
JOIN CIGActgS11.DmBalance d 
on s.StageID=d.StageID
Where s.StageDate >= '2018-12-31'
and Stage= 'EOD'
and CLientID = 223906
group by s.StageID
order by s.StageID

		""",
	), 	
	compare=dict( #full outer join hack
		SQLServer_diff=""" 
SELECT d.StageID,
 d.cnt_IQ, c.cnt_SQL, c.cnt_SQL-d.cnt_IQ diff
FROM {IQ} d
LEFT JOIN {SQLServer} c USING(StageID)
UNION ALL
SELECT c.StageID,
 c.cnt_SQL, d.cnt_IQ, d.cnt_IQ -c.cnt_SQL diff
FROM {SQLServer} c
LEFT JOIN {IQ} d USING(StageID)
WHERE d.StageID IS NULL
		"""
	)
)