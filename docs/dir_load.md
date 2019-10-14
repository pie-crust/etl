
Back to [README](../README.md)


# Workflow (Dir->S3->Snowflake)

 * Cli reads all file names from directory and defines skip/start read positions for each file chunk.
 * Compresses and uploads file chunks to S3 in parallel.
 * Loads files in 1000s into Snowflake
  
 
```
-> Grab all files from directory
    - For large files set offset/size positions of each chunk
    -> multiprocessing (num_of_processes=dop)
        - re-cut file chunk edges to the EOL
        - compress and upload to S3
    -> Open transaction (Snowflake)
      -> loop (s3 file group size = 1000 files)
          - COPY INTO each group (Snowflake)
    -> commit (Snowflake)
    -> delete files from S3
```

#### Python workflow
```Python
	Dir.get_files ( out = data_files )
	if 1:
		S3.upload_files ( file_names = data_files, out = s3_data_keys, skip_header=skip_header, rec_delim=rec_delim )
	if 1:
		Snowflake.begin_transaction ( out 	= snow_conn )
		Snowflake.bulk_copy			( trans	= snow_conn, file_names = s3_data_keys, target=cli.tcfg, qname = 'copyStmt' )
		Snowflake.commit_transaction( trans	= snow_conn )
	if 1:
		S3.delete_files ( file_names=s3_data_keys )
```


### Example.
```

time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/file_load/dir_s3_snow/journalline.json --proc_params  \
  /auto/dbdumps_PMT_Snow/load_test_2/
  
```



### Lame duck load.

append option `-ld 100` to load only first 100 rows from the file


### Parallelism
To control number of processes set -dop (degree_of_parallelism)
Note: 
	`-dop 1`  will set num of processes to number of cores
	`-dop 4`  will set num of processes to number of cores multiplied by 4 (max setting)





