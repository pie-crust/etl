select 'PK' tab, count(*) cnt from  PK UNION ALL
select 'Tx' tab, count(*) cnt from  Tx UNION ALL
select 'TxConfirm' tab, count(*) cnt from  TxConfirm UNION ALL
select 'TxExtendedAttributes' tab, count(*) cnt from  TxExtendedAttributes UNION ALL
select 'TxFee' tab, count(*) cnt from  TxFee UNION ALL
select 'TxFinancingAttributes' tab, count(*) cnt from  TxFinancingAttributes UNION ALL
select 'TxFinancingHistoryRate' tab, count(*) cnt from  TxFinancingHistoryRate UNION ALL
select 'TxFinancingRate' tab, count(*) cnt from  TxFinancingRate UNION ALL
select 'TxFinancingRateHist' tab, count(*) cnt from  TxFinancingRateHist UNION ALL
select 'TxPositionBlockAllocation' tab, count(*) cnt from  TxPositionBlockAllocation UNION ALL
select 'TxSide' tab, count(*) cnt from  TxSide UNION ALL
select 'TxStatus' tab, count(*) cnt from  TxStatus 


create view v_desc as select distinct t.table_schema,t.table_name, c.ordinal_position, c.column_name, c.data_type, c.is_nullable , c.is_identity, con.constraint_name,con.constraint_type  
from  columns c   left join tables t on t.table_schema = c.table_schema and t.table_name = 'Tx'  left join 
constraint_columns con on t.table_name = con.table_name and c.column_name = con.column_name and constraint_type='p'  
where c.table_schema = 'CIGRpt' and c.table_name = 'Tx'  order by ordinal_position

