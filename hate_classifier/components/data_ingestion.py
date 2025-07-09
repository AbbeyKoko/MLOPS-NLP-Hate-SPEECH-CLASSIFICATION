import os
import sys
import zipfile

from hate_classifier.exception import CustomException
from hate_classifier.logger import LoggerManager

from hate_classifier.entity.config_entity import DataIngestionConfig

from hate_classifier.configuration.s3_bucket_ops import S3Operations

class DataIngestion:
  def __init__(self, config: DataIngestionConfig):
    self.logger = LoggerManager(self.__class__.__name__).get_logger()
    self.config = config
    
  def download_file(self) -> str:
    """ 
    Fetch data from S3 bucket
    """
    self.logger.info(f"Entered the download_file method of DataIngestion class")
    try:
      from_here = self.config.bucket_file_path
      to_here = self.config.unzip_data_dir
      
      self.logger.info(f"Downloading data from {from_here} to {to_here}")
      s3 = S3Operations()
      s3.download_file(from_here=from_here, to_here=to_here)
      self.logger.info(f"Downloaded data from {from_here} to {to_here}")
      
      self.logger.info(f"Exited the download_file method of DataIngestion class")
    except Exception as e:
      self.logger.error(f"Could not download data from {from_here}")
      raise CustomException(e, sys) from e
    
    
  def extract_zip_file(self) -> None:
    """ 
    Extract data from zipfile
    """
    self.logger.info(f"Entered the extract_zip_file method of DataIngestion class")
    try:
      unzip_file_path = self.config.unzip_data_dir
      unzip_dir = os.path.dirname(self.config.imbalance_data_dir)
      os.makedirs(unzip_dir, exist_ok=True)
      
      self.logger.info(f"Unzipping data from {unzip_file_path}")
      with zipfile.ZipFile(unzip_file_path, "r") as zip_ref:
        for member in zip_ref.namelist():
          if "__MACOSX" in member or member.endswith("/"):
            continue
          zip_ref.extract(member=member, path=unzip_dir)
      self.logger.info(f"Unzipped data from {unzip_file_path}")
            
      self.logger.info(f"Exited the extract_zip_file method of DataIngestion class")
      
    except Exception as e:
      self.logger.error(f"Could not unzip file")
      raise CustomException(e, sys) from e