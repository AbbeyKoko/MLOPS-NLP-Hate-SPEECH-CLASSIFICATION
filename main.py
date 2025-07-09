from hate_classifier.logger import LoggerManager

from hate_classifier.pipeline.stage_01_data_ingestion_train_pipeline import DataIngestionTrainingPipeline



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