select * from table(information_schema.copy_history(table_name=>'DY_POSITION_TD', start_time=>dateadd(hours, -5700, current_timestamp())));
