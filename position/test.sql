select count(*) from DY_FinancingPosition;
ME_FinancingPosition, ME_13F

#//1
select M.mon, ISNULL( dyfp.AccountingDate,mefp.AccountingDate,me13.AccountingDate) AccountingDate,  
dyfp.cnt DY_FinancingPosition ,  mefp.cnt ME_FinancingPosition, me13.cnt ME_13F  from 
(select  AccountingDate, count(*) cnt 
FROM Position.DY_FinancingPosition 
GROUP BY AccountingDate) dyfp, 
(select  AccountingDate, count(*) cnt 
FROM Position.ME_FinancingPosition 
GROUP BY AccountingDate) mefp,
(select  AccountingDate, count(*) cnt 
FROM Position.ME_13F 
GROUP BY AccountingDate) me13,
(select row_num mon   FROM sa_rowgenerator( 1, 12, 1 )) M
where M.mon *= DATEPART( MONTH, mefp.AccountingDate)
and M.mon *= DATEPART( MONTH, dyfp.AccountingDate)
and M.mon *= DATEPART( MONTH, me13.AccountingDate)
order by 1 
 
 select  client, AccountingDate, count(*) cnt 
FROM Position.DY_FinancingPosition 
GROUP BY client, AccountingDate

select  M.mon, ISNULL( dyfp.client,mefp.client,me13.client) clt, 
ISNULL( dyfp.AccountingDate,mefp.AccountingDate,me13.AccountingDate) AccountingDate,  
dyfp.cnt DY_FinancingPosition ,  mefp.cnt ME_FinancingPosition, me13.cnt ME_13F  from 
(select client, AccountingDate, count(*) cnt 
FROM Position.DY_FinancingPosition 
GROUP BY client,AccountingDate) dyfp, 
(select client, AccountingDate, count(*) cnt 
FROM Position.ME_FinancingPosition 
GROUP BY client,AccountingDate) mefp,
(select client, AccountingDate, count(*) cnt 
FROM Position.ME_13F 
GROUP BY client,AccountingDate) me13,
(select row_num mon , 223906 client  FROM sa_rowgenerator( 1, 12, 1 )) M
where M.mon *= DATEPART( MONTH, mefp.AccountingDate)
and M.mon *= DATEPART( MONTH, dyfp.AccountingDate)
and M.mon *= DATEPART( MONTH, me13.AccountingDate)
and M.client *= DATEPART( MONTH, me13.client)
order by 2, 1

select M.mon,  M.client, ISNULL( dyfp.AccountingDate,mefp.AccountingDate,me13.AccountingDate) AccountingDate,  
dyfp.cnt DY_FinancingPosition ,  mefp.cnt ME_FinancingPosition, me13.cnt ME_13F  from 
(select  client,AccountingDate, count(*) cnt 
FROM Position.DY_FinancingPosition 
GROUP BY client, AccountingDate) dyfp, 
(select client,  AccountingDate, count(*) cnt 
FROM Position.ME_FinancingPosition 
GROUP BY client, AccountingDate) mefp,
(select  AccountingDate, count(*) cnt 
FROM Position.ME_13F 
GROUP BY AccountingDate) me13,
(select row_num mon , 223906 client  FROM sa_rowgenerator( 1, 12, 1 )) M
where M.mon *= DATEPART( MONTH, mefp.AccountingDate)
and M.mon *= DATEPART( MONTH, dyfp.AccountingDate)
and M.mon *= DATEPART( MONTH, me13.AccountingDate)
and M.client *=  dyfp.client
and M.client *=  mefp.client
order by 1 


select M.mon,  M.client, ISNULL( dyfp.AccountingDate,mefp.AccountingDate,me13.AccountingDate) AccountingDate,  
dyfp.cnt DY_FinancingPosition ,  mefp.cnt ME_FinancingPosition, me13.cnt ME_13F  from 
(select  client,AccountingDate, count(*) cnt 
FROM Position.DY_FinancingPosition 
GROUP BY client, AccountingDate) dyfp, 
(select client,  AccountingDate, count(*) cnt 
FROM Position.ME_FinancingPosition 
GROUP BY client, AccountingDate) mefp,
(select  AccountingDate, count(*) cnt 
FROM Position.ME_13F 
GROUP BY AccountingDate) me13,
(select row_num mon , 223907 client  FROM sa_rowgenerator( 1, 12, 1 )) M
where M.mon *= DATEPART( MONTH, mefp.AccountingDate)
and M.mon *= DATEPART( MONTH, dyfp.AccountingDate)
and M.mon *= DATEPART( MONTH, me13.AccountingDate)
and M.client *=  dyfp.client
and M.client *=  mefp.client
order by 1 

select mon, client, AccountingDate, DY_FinancingPosition, ME_FinancingPosition, ME_13F from (
select M.mon, M.cid, M.client, ISNULL( dyfp.AccountingDate,mefp.AccountingDate,me13.AccountingDate) AccountingDate,  
dyfp.cnt DY_FinancingPosition ,  mefp.cnt ME_FinancingPosition, me13.cnt ME_13F  from 
(select  client,AccountingDate, count(*) cnt 
FROM Position.DY_FinancingPosition 
GROUP BY client, AccountingDate) dyfp, 
(select client,  AccountingDate, count(*) cnt 
FROM Position.ME_FinancingPosition 
GROUP BY client, AccountingDate) mefp,
(select  0 client, AccountingDate, count(*) cnt 
FROM Position.ME_13F 
GROUP BY 0, AccountingDate) me13,
(select 6 cid, row_num mon , 223906 client  FROM sa_rowgenerator( 1, 8, 1 )
union all
select 7 cid,row_num mon , 223907 client  FROM sa_rowgenerator( 1, 8, 1 )
) M
where M.mon *= DATEPART( MONTH, mefp.AccountingDate)
and M.mon *= DATEPART( MONTH, dyfp.AccountingDate)
and M.mon *= DATEPART( MONTH, me13.AccountingDate)
and M.client *=  dyfp.client
and M.client *=  mefp.client
and M.client *=  me13.client
union all
select M.mon, M.cid,  M.client, ISNULL( dyfp.AccountingDate,mefp.AccountingDate,me13.AccountingDate) AccountingDate,  
dyfp.cnt DY_FinancingPosition ,  mefp.cnt ME_FinancingPosition, me13.cnt ME_13F  from 
(select  AccountingDate, count(*) cnt 
FROM Position.DY_FinancingPosition 
GROUP BY  AccountingDate) dyfp, 
(select   AccountingDate, count(*) cnt 
FROM Position.ME_FinancingPosition 
GROUP BY  AccountingDate) mefp,
(select   AccountingDate, count(*) cnt 
FROM Position.ME_13F 
GROUP BY 0, AccountingDate) me13,
(select 0 cid, 0 client, row_num mon FROM sa_rowgenerator( 1, 8, 1 )
) M
where M.mon *= DATEPART( MONTH, mefp.AccountingDate)
and M.mon *= DATEPART( MONTH, dyfp.AccountingDate)
and M.mon *= DATEPART( MONTH, me13.AccountingDate)
) t
order by cid, mon



select M.mon,  M.client, ISNULL( dyfp.AccountingDate,mefp.AccountingDate,me13.AccountingDate) AccountingDate,  
dyfp.cnt DY_FinancingPosition ,  mefp.cnt ME_FinancingPosition, me13.cnt ME_13F  from 
(select  client,AccountingDate, count(*) cnt 
FROM Position.DY_FinancingPosition 
GROUP BY client, AccountingDate) dyfp, 
(select client,  AccountingDate, count(*) cnt 
FROM Position.ME_FinancingPosition 
GROUP BY client, AccountingDate) mefp,
(select  AccountingDate, count(*) cnt 
FROM Position.ME_13F 
GROUP BY AccountingDate) me13,
(select 6 cid, row_num mon , 223906 client  FROM sa_rowgenerator( 1, 7, 1 )
union all
select 7 cid,row_num mon , 223907 client  FROM sa_rowgenerator( 1, 7, 1 )
) M
where M.mon *= DATEPART( MONTH, mefp.AccountingDate)
and M.mon *= DATEPART( MONTH, dyfp.AccountingDate)
and M.mon *= DATEPART( MONTH, me13.AccountingDate)
and M.client *=  dyfp.client
and M.client *=  mefp.client
order by M.cid, 1



 
 select M.mon,M.PosType, M.client,ISNULL( dy_1.AccountingDate, me_1.AccountingDate,dy_2.AccountingDate, me_2.AccountingDate) AccountingDate,  
dy_1.cnt DY_Position_SD ,  me_1.cnt ME_Position_SD, dy_2.cnt DY_Position_TD, me_2.cnt ME_Position_TD from 
(select  client,PosType, AccountingDate, count(*) cnt 
FROM Position.DY_Position_SD 
GROUP BY client,PosType, AccountingDate) dy_1, 
(select  client,PosType, AccountingDate, count(*) cnt 
FROM Position.ME_Position_SD 
GROUP BY client,PosType, AccountingDate) me_1,
(select client,PosType,  AccountingDate, count(*) cnt 
FROM Position.DY_Position_TD 
GROUP BY client,PosType, AccountingDate) dy_2,
(select client, PosType, AccountingDate, count(*) cnt 
FROM Position.ME_Position_TD 
GROUP BY client,PosType, AccountingDate) me_2,
(select row_num mon, 223906 client, 'ACCT' PosType    FROM sa_rowgenerator( 1, 7, 1 )
union all
select row_num mon, 223907 client , 'ACCT' PosType   FROM sa_rowgenerator( 1, 7, 1 )
union all
select row_num mon, 223906 client, 'DESK' PosType    FROM sa_rowgenerator( 1, 7, 1 )
union all
select row_num mon, 223907 client , 'DESK' PosType   FROM sa_rowgenerator( 1, 7, 1 )) M
where M.mon *= DATEPART( MONTH, dy_1.AccountingDate)
and M.mon *= DATEPART( MONTH, me_1.AccountingDate)
and M.mon *= DATEPART( MONTH, dy_2.AccountingDate)
and M.mon *= DATEPART( MONTH, me_2.AccountingDate)
and CAST(M.client AS VARCHAR) +M.PosType *=  CAST(dy_1.client AS VARCHAR) + dy_1.PosType
and CAST(M.client AS VARCHAR) +M.PosType *=  CAST(me_1.client AS VARCHAR) + me_1.PosType
and CAST(M.client AS VARCHAR) +M.PosType *=  CAST(dy_2.client AS VARCHAR) + dy_2.PosType
and CAST(M.client AS VARCHAR) +M.PosType *=  CAST(me_2.client AS VARCHAR) + me_2.PosType
order by M.PosType, M.client, 1 


 select M.mon, ISNULL( dy_1.AccountingDate, me_1.AccountingDate,dy_2.AccountingDate, me_2.AccountingDate) AccountingDate,  
dy_1.cnt DY_Position_SD ,  me_1.cnt ME_Position_SD, dy_2.cnt DY_Position_TD, me_2.cnt ME_Position_TD from 
(select  AccountingDate, count(*) cnt 
FROM Position.DY_Position_SD 
GROUP BY AccountingDate) dy_1, 
(select  AccountingDate, count(*) cnt 
FROM Position.ME_Position_SD 
GROUP BY AccountingDate) me_1,
(select  AccountingDate, count(*) cnt 
FROM Position.DY_Position_TD 
GROUP BY AccountingDate) dy_2,
(select  AccountingDate, count(*) cnt 
FROM Position.ME_Position_TD 
GROUP BY AccountingDate) me_2,
(select row_num mon   FROM sa_rowgenerator( 1, 12, 1 )) M
where M.mon *= DATEPART( MONTH, dy_1.AccountingDate)
and M.mon *= DATEPART( MONTH, me_1.AccountingDate)
and M.mon *= DATEPART( MONTH, dy_2.AccountingDate)
and M.mon *= DATEPART( MONTH, me_2.AccountingDate)
order by 1 


