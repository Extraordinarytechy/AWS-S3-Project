import boto3


 #initialize S3 client
s3_client = boto3.client("s3")



# Define bucket name and file to upload 
 
BUCKET_NAME = "ajay-unique-s3-project" # Replace with your bucket
FILE_NAME = "sample.txt" # The file name you want to upload


def upload_file():

     try:
         s3_client.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
         print(f" File '{FILE_NAME}' uploaded succesfully to bucket '{BUCKET_NAME}'!")
    
     except Exception as e:
          print(f" Error uploading the file: {e}")
 
if __name__ == "__main__":
    
    upload_file()
