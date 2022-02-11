provider "aws" {
  version = ">= 3.7.0"
  region  = "ap-south-1" #update the region
  assume_role {
    role_arn = "arn:aws:iam::${var.accountid}:role/LambdaExecutionRoleForConfig"
  }
}

resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}