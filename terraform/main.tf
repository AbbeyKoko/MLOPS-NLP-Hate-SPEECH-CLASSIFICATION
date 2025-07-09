provider "aws" {
  region = var.region
  profile = var.profile
}
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}

module "terraform-user" {
  source = "./modules/terrraform_user"
  iam_user_name = var.iam_user_name
  iam_group_name = var.iam_group_name
  iam_policy_name = var.iam_policy_name
}

module "s3" {
  source = "./modules/s3"
  s3_bucket = var.s3_bucket
}