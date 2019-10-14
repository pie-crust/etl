import io
import zipfile
import boto3
import sys

session = boto3.Session(
	aws_access_key_id="AKIAYCS5P5BHX2UNCL22", 
	aws_secret_access_key="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",
)

s3 = boto3.client(
    's3',
)



def stream_zip_file():
    count = 0
    obj = s3.Object(
        bucket_name='home-pmt-accounting-dev',
        key='racct/DY_Position_SD/file_0_100.2019-06-17.13_39_12.IQ.csv.gz test.csv.gz'
    )
    buffer = io.BytesIO(obj.get()["Body"].read())
    print (buffer)
    z = zipfile.ZipFile(buffer)
    foo2 = z.open(z.infolist()[0])
    print(sys.getsizeof(foo2))
    line_counter = 0
    for _ in foo2:
        line_counter += 1
    print (line_counter)
    z.close()


if __name__ == '__main__':
    stream_zip_file()