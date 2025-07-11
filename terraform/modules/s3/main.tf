resource "aws_s3_bucket" "s3" {
  bucket = var.s3_bucket
  force_destroy = true

  tags = {
    Name: var.s3_bucket
    Environment: "Dev"
  }
}

resource "aws_s3_bucket_public_access_block" "s3_access_block" {
  bucket = aws_s3_bucket.s3.id

  block_public_acls = true
  block_public_policy = true
  ignore_public_acls = true
  restrict_public_buckets = true
}