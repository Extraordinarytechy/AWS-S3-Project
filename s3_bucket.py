import boto3
import sys

def create_s3_bucket(bucket_name,region="ap-south-1"):
         """
         creates S3 bucket in the specified AWS region.
         
         :param bucket_name: Name of the S3 bucket ( must be globally unique)
         :param region: AWS region where the bucket will be created ( default: ap-south-1)
         :return: Response from AWS S3
         """
         s3_client =  boto3.client("s3",region_name=region)

         try:
             response = s3_client.create_bucket(Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region})
             print(f"Bucket '{bucket_name}' created successfully in {region}!")
             return response
         except Exception as e:
           print(f" Error Creating bucket: {str(e)}")
           sys.exit(1)
if __name__ == "__main__":
           BUCKET_NAME = "ajay-unique-s3-project" #change this to globally unique name
           print(f"Creating S3 bucket: {BUCKET_NAME} in ap-south-1...")
           create_s3_bucket(BUCKET_NAME)
