output "iam_user_name" {
  value = module.terraform-user.iam_user_name
  sensitive = true
}

output "access_key_id" {
  value = module.terraform-user.access_key_id
  sensitive = true
}

output "secret_access_key" {
  value = module.terraform-user.secret_access_key
  sensitive = true
}

output "s3_bucket_name" {
  value = module.s3.s3_bucket_name
}

output "s3_bucket_arn" {
  value = module.s3.s3_bucket_arn
}