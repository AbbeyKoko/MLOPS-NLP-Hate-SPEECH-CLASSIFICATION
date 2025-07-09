import os
from pathlib import Path

from hate_classifier.utils.main_utils import read_yaml, create_directories

from hate_classifier.exception import CustomException
from hate_classifier.logger import LoggerManager
from hate_classifier.constants import *

from hate_classifier.entity.config_entity import (DataIngestionConfig)


class ConfigurationManager:
  def __init__(self, CONFIG_PATH=CONFIG_PATH, PARAMS_PATH=PARAMS_PATH):

    self.config = read_yaml(CONFIG_PATH)
    # self.params = read_yaml(PARAMS_PATH)
    self.artifacts = self.config.artifacts_root
    create_directories([self.artifacts])
    
  def get_data_ingestion_config(self) -> DataIngestionConfig:
    config = self.config.data_ingestion
    
    data_ingestion_root = os.path.join(self.artifacts, config.root_dir)
    create_directories([data_ingestion_root])
    
    data_ingestion_config = DataIngestionConfig(
      root_dir=data_ingestion_root,
      bucket_file_path=config.bucket_file_path,
      unzip_data_dir=os.path.join(data_ingestion_root, config.zip_file_dir),
      imbalance_data_dir=os.path.join(data_ingestion_root,"data", config.imbalance_data_dir),
      raw_data_dir=os.path.join(data_ingestion_root,"data", config.raw_data_dir)
    )
    
    return data_ingestion_config