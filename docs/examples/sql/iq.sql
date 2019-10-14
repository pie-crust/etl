LOAD TABLE Position.DY_Position_SD
FROM './dump/delta_dumps/20190723_140517/IQ_DEV_20190723_140517.csv' 




LOAD TABLE Position.DY_Position_SD (Account,PSLocalCurrencyCode,Subaccount,FinancialType,Instrument,InstrumentDesc,TradeFactor,SDQty,SDCurrentQty,LongShort_E,SDMV,Fx,BaseSDMV,PositionID,BusinessUnitID,TRSInstrument,TRSInstrumentDesc,NotionalFlag_E,SwapType_E,Price,PriceSource,LastID,LastModified,AccountingDate,PosType,Stage,AsOfDateTime,Client)
FROM './dump/delta_dumps/20190723_140517/IQ_DEV_20190723_140517.csv' 
ESCAPES OFF


LOAD TABLE Position.DY_Position_SD (Account,PSLocalCurrencyCode,Subaccount,FinancialType,Instrument,InstrumentDesc,TradeFactor,SDQty,SDCurrentQty,LongShort_E,SDMV,Fx,BaseSDMV,PositionID,BusinessUnitID,TRSInstrument,TRSInstrumentDesc,NotionalFlag_E,SwapType_E,Price,PriceSource,LastID,LastModified,AccountingDate,PosType,Stage,AsOfDateTime,Client)
FROM '/auto/fina-datadev/share/PositionModel/test4k.csv' 
quotes off
escapes off
format ascii
delimited by '|'
row delimited by '\n'






 /auto/fina-datadev/share/PositionModel

select * from CIGActgH.HydraClients

SELECT syscolumns.name, systypes.name FROM sysobjects 
JOIN syscolumns ON sysobjects.id = syscolumns.id
JOIN systypes ON systypes.type = syscolumns.type AND systypes.usertype = syscolumns.usertype
WHERE sysobjects.name LIKE 'DY_Position_SD' 

Select * from systabcol
key join systab
 where table_name = 'HydraPNLEntries'
 order by column_id

 
 
Select user_name(creator) as 'owner_name' , column_id, column_name from systabcol
key join systab
 where table_name = 'DY_Position_SD'
 order by column_id
 
 
 Select  column_name from systabcol
key join systab
 where table_name = 'DY_Position_SD'
 order by column_id
 
Select user_name(systabcol.object_id)  as 'owner_name' from systabcol
key join systab
 where table_name = 'HydraPNLEntries'
 order by column_id
 
 
 
 SELECT
DB_NAME() TABLE_CATALOG,
NULL TABLE_SCHEMA,
sc.column_id ORDINAL_POSITION,
NULL COLUMN_DEFAULT,
NULL CHARACTER_SET_CATALOG,
NULL CHARACTER_SET_SCHEMA,
NULL COLLATION_CATALOG,
NULL COLLATION_SCHEMA,
NULL DOMAIN_CATALOG,
NULL DOMAIN_SCHEMA,
NULL DOMAIN_NAME
FROM 
sysobjects so
INNER JOIN 
systabcol sc
ON sc.column_id = so.id
WHERE so.name = 'DY_Position_SD'

SELECT SCHEMA_NAME('Position');
 

select u.name as 'owner_name', 
       o.name as 'table_name'
from   sysobjects o,
       sysusers u
where  o.uid  = u.uid
and    o.name = 'DY_Position_SD'
and    o.type = 'U'


select user_name(o.uid), o.uid as 'owner_name', 
       o.name as 'table_name'
from   sysobjects o
where  o.name = 'HydraPNLEntries'
and    o.type = 'U'
