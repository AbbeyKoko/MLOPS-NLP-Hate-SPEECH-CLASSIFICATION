variable "region" {
  type = string
  default = "eu-north-1"
}

variable "availability_zone" {
  type = string
  default = "eu-north-1a"
}

variable "profile" {
  type = string
}

variable "iam_user_name" {
  type = string
}

variable "iam_group_name" {
  type = string
}

variable "iam_policy_name" {
  type = string
}

variable "s3_bucket" {
  type = string
}