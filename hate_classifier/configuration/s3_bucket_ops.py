import os
import sys
import boto3
import json
import boto3.session
from from_root import from_root

from io import StringIO
from typing import List, Dict

from hate_classifier.exception import CustomException
from hate_classifier.logger import LoggerManager


class S3Operations:
  
  def __init__(self):
    self.logging = LoggerManager(self.__class__.__name__).get_logger()
    self._configure_bucket()

    
  def _configure_bucket(self):
    """
    Method Name :   _configure_bucket
    Description :   This method gets the bucket name from terraform and initialises s3 client

    Output      :   
    On Failure  :   Write an exception log and then raise an exception

    Version     :   1.2
    Revisions   :   moved setup to cloud
    """
    self.logging.info("Entered the _configure_bucket of S3Operations Class")
    try:
      terraform_outputs = os.path.join(from_root(), "terraform/tf_outputs.json")
      with open(terraform_outputs) as f:
        data = json.load(f)
        _access_key_id = data["access_key_id"]["value"]
        _secret_access_key = data["secret_access_key"]["value"]
        self.bucket_name = data["s3_bucket_name"]["value"]
        
      self.logging.info(f"S3 Bucket loaded as: {self.bucket_name}")
      self.s3_client = boto3.client(service_name="s3",
                                      aws_access_key_id=_access_key_id,
                                      aws_secret_access_key=_secret_access_key)
      self.logging.info(f"S3 Bucket initialised as: {self.bucket_name}")
      self.logging.info("Exited the _configure_bucket of S3Operations Class")
    except Exception as e:
      self.logging.error("Failed to load terraform outputs for bucket: s3_bucket_name")
      raise CustomException(e, sys) from e
    
  def list_objects(self, prefix: str = "") -> List[Dict]:
      """
      Method Name :   list_objects
      Description :   This method reads the list all the objects in the bucket

      Output      :   Returns list of dicts with key and size of files
      On Failure  :   Write an exception log and then raise an exception

      Version     :   1.2
      Revisions   :   moved setup to cloud
      """
      self.logging.info("Entered the list_objects of S3Operations Class")
      
      try:
        response = self.s3_client.list_objects_v2(Bucket=self.bucket_name,
                                                  Prefix=prefix)
        contents = response.get("Contents", [])
        
        list_of_objects = []
        
        if not contents:
          self.logging.info("Bucket is empty")
        else:        
          for obj in contents:
            list_of_objects.append(
              {"key": obj["Key"], "size": obj["Size"]}
            )
        
        self.logging.info(f"Found {len(list_of_objects)} objects in bucket")
        
        self.logging.info("Exited the list_objects of S3Operations Class")
        return list_of_objects
          
      except Exception as e:
        self.logging.error(f"Failed to list objects in: {self.bucket_name}")
        raise CustomException(e, sys) from e


  def upload_file(self, from_here: str, to_here: str) -> None:
      """
      Method Name :   upload_file
      Description :   This method uploads the objects from_here to to_here in the bucket

      Output      :   
      On Failure  :   Write an exception log and then raise an exception

      Version     :   1.2
      Revisions   :   moved setup to cloud
      """
      self.logging.info("Entered the upload_file of S3Operations Class")
      
      try:
        self.logging.info(f"Uploading {from_here} to {to_here} in {self.bucket_name} bucket")
        
        self.s3_client.upload_file(
          Filename=from_here,
          Bucket=self.bucket_name,
          Key=to_here
        )
        
        self.logging.info(f"Uploaded {from_here} to {to_here} in {self.bucket_name} bucket")
        self.logging.info("Exited the upload_file of S3Operations Class")
      except Exception as e:
        self.logging.info(f"Could not upload {from_here} to {to_here} in {self.bucket_name} bucket")
        raise CustomException(e,sys) from e
      
      
  def download_file(self, from_here: str, to_here: str) -> None:
      """
      Method Name :   download_file
      Description :   This method downloads the objects from_here in the bucket to to_here on local

      Output      :   
      On Failure  :   Write an exception log and then raise an exception

      Version     :   1.2
      Revisions   :   moved setup to cloud
      """
      self.logging.info("Entered the download_file of S3Operations Class")
      
      try:
        self.logging.info(f"Downloading {from_here} in {self.bucket_name} bucket to {to_here} locally ")
        
        file_dir = os.path.dirname(to_here)
        if file_dir != "":
          os.makedirs(file_dir, exist_ok=True)
        
        self.s3_client.download_file(
          Filename=to_here,
          Bucket=self.bucket_name,
          Key=from_here 
        )
        
        self.logging.info(f"Downloaded {from_here} in {self.bucket_name} bucket to {to_here} locally ")
        self.logging.info("Exited the download_file of S3Operations Class")
      except Exception as e:
        self.logging.info(f"Could not Download {from_here} in {self.bucket_name} bucket to {to_here} locally ")
        raise CustomException(e,sys) from e
      
      
  def delete_file(self, from_here: str) -> None:
      """
      Method Name :   delete_file
      Description :   This method deletes the object from_here in the bucket 

      Output      :   
      On Failure  :   Write an exception log and then raise an exception

      Version     :   1.2
      Revisions   :   moved setup to cloud
      """
      self.logging.info("Entered the delete_file of S3Operations Class")
      
      try:
        self.logging.info(f"Fetch object {from_here} in {self.bucket_name} bucket")
        
        self.s3_client.delete_object(
          Bucket=self.bucket_name,
          Key=from_here 
        )
        
        self.logging.info(f"Deleted {from_here} in {self.bucket_name} bucket")
        self.logging.info("Exited the delete_file of S3Operations Class")
      except Exception as e:
        self.logging.info(f"Could not delete {from_here} in {self.bucket_name} bucket")
        raise CustomException(e,sys) from e
      
      
  def get_file(self, from_here: str, decode: bool = False) -> None:
      """
      Method Name :   get_file
      Description :   This method gets the object from_here in the bucket 

      Output      :   Returns an object in memory
      On Failure  :   Write an exception log and then raise an exception

      Version     :   1.2
      Revisions   :   moved setup to cloud
      """
      self.logging.info("Entered the get_file of S3Operations Class")
      
      try:
        self.logging.info(f"Fetch object {from_here} in {self.bucket_name} bucket")
        
        response = self.s3_client.get_object(
          Bucket=self.bucket_name,
          Key=from_here 
        )
                
        file_object = response["Body"].read()
        if decode:
          file_object = file_object.decode("utf-8")
        
        self.logging.info(f"Fetched object {from_here} in {self.bucket_name} bucket")
        self.logging.info("Exited the get_file of S3Operations Class")
        
        return file_object
      except Exception as e:
        self.logging.info(f"Could not fetch object {from_here} in {self.bucket_name} bucket")
        raise CustomException(e,sys) from e