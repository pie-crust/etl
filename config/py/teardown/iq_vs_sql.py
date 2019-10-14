dict(comments= "DMBalance StageID counts test", 
	source=dict(
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
		"""
	), 
	compare=dict( #full outer join hack
		IQ_vs_SQLServer=""" 
SELECT 	StageID,cnt_IQ, cnt_SQL, diff  FROM (	
SELECT d.StageID,
ifnull(d.cnt_IQ,0) cnt_IQ , ifnull(c.cnt_SQL,0) cnt_SQL , ifnull(d.cnt_IQ,0) - ifnull(c.cnt_SQL,0) diff
FROM {IQ} d
LEFT JOIN {SQLServer} c USING(StageID)
UNION ALL
SELECT c.StageID,
ifnull(d.cnt_IQ,0) cnt_IQ, ifnull(c.cnt_SQL,0) cnt_SQL, ifnull(d.cnt_IQ,0) - ifnull(c.cnt_SQL,0) diff
FROM {SQLServer} c
LEFT JOIN {IQ} d USING(StageID)
WHERE d.StageID IS NULL) t WHERE  diff!=0
		""",
		_match="""

SELECT a.StageID, a.cnt
FROM {IQ} a, {SQLServer} b
WHERE a.StageID=b.StageID 
  AND a.cnt= b.cnt

		""",
		_unmatch="""

SELECT a.StageID, a.cnt, b.cnt, a.cnt-b.cnt diff
FROM {IQ} a, {SQLServer} b
WHERE a.StageID=b.StageID 
  AND a.cnt!= b.cnt

		"""
	)
)