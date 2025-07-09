from hate_classifier.configuration.s3_bucket_ops import S3Operations

s3 = S3Operations()

print(s3.list_objects())

# files = s3.list_objects()

# files[0].get("key")

# s3.upload_file("requirements.in", "main/requirements.in")

# s3.download_file(files[0].get("key"), "main/requirements.in")

# s3.delete_file(files[0].get("key"))

# print(s3.list_objects())