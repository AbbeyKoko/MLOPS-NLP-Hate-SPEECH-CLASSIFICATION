from hate_classifier.configuration.s3_bucket_ops import S3Operations

s3 = S3Operations()

# # print(s3.list_objects())

files = s3.list_objects()

# # files[0].get("key")

s3.upload_file("notebooks/dataset/data.zip", "data/raw/data.zip")

# # s3.download_file(files[0].get("key"), "main/requirements.in")

# s3.delete_file(files[0].get("key")) 

print(s3.list_objects())

# from hate_classifier.configuration.configuration import ConfigurationManager

# ConfigurationManager().get_data_ingestion_config()
# # from pathlib import Path


# from hate_classifier.utils.main_utils import read_yaml
# CONFIG_PATH = Path("config/config.yaml")

# print(read_yaml(CONFIG_PATH))