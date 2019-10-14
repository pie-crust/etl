SELECT StageID, count(1) cnt 
FROM  CIGActgS11.DMBalance 
WHERE StageID in (184990,184991) 
GROUP BY StageID
