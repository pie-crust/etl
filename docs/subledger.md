
Back to [README](../README.md)


# Workflow (Dir->S3->Snowflake)

 * Cli reads all file names from directory and defines skip/start read positions for each file chunk.
 * Compresses and uploads chunks to S3
 * Loads files in 1000s into Snowflake
 
 
 ```
1. Grab all files from directory
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



### Example.
```

time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_s3_snow/journalline.json --proc_params  \
  /auto/dbdumps_PMT_Snow/load_test_2/
  
```


### Lame duck load.

Use option `-ld 100` to load only first 100 rows from the file


### Parallelism
To control number of processes set -dop (degree_of_parallelism)
Note: 
	`-dop 1`  will set num of processes to number of cores
	`-dop 4`  will set num of processes to number of cores multiplied by 4 (max setting)




