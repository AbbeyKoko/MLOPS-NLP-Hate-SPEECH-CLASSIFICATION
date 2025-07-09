resource "aws_iam_group" "this" {
  name = var.iam_group_name
}

resource "aws_iam_user" "this" {
  name = var.iam_user_name
  force_destroy = true
}

resource "aws_iam_access_key" "access_key" {
  user = aws_iam_user.this.name
}

resource "aws_iam_policy" "this" {
  name = var.iam_policy_name
  policy = file("${path.module}/policy.json")
}

resource "aws_iam_group_policy_attachment" "this" {
  group = aws_iam_group.this.name
  policy_arn = aws_iam_policy.this.arn
}


resource "aws_iam_group_membership" "this" {
  name = "${var.iam_group_name}-group-membership"
  group = aws_iam_group.this.name
  users = [
    aws_iam_user.this.name
  ]
}