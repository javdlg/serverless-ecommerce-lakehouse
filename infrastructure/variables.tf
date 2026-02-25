variable "aws_region" {
  description = "The AWS region where the infrastructure will be deployed"
  type        = string
  default     = "us-east-1" 
}

variable "project_name" {
  description = "Base name for the project's resources"
  type        = string
  default     = "ecommerce-lakehouse"
}