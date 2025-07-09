from hate_classifier.logger import LoggerManager

from hate_classifier.configuration.configuration import ConfigurationManager
from hate_classifier.components.data_ingestion import DataIngestion
from hate_classifier.entity.artifact_entity import DataIngestionArtifacts


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
  def __init__(self):
    pass
  
  def main(self):
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
    
    data_ingestion_artifact = DataIngestionArtifacts(
        imbalance_data_dir=data_ingestion_config.imbalance_data_dir,
        raw_data_dir=data_ingestion_config.raw_data_dir
      )
    
    return data_ingestion_artifact
  
  
STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
  logger = LoggerManager("DataIngestionTrainingPipeline").get_logger()
  try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx=====================x")
  except Exception as e:
    logger.exception(e)
    raise e