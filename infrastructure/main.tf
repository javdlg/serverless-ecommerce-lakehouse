# 1. Provider configuration
provider "aws" {
  region = var.aws_region
  
  # Best practices: Tag everything you create
  default_tags {
    tags = {
      Project     = var.project_name
      Environment = "Dev"
    }
  }
}

# 2. Bucket S3 creation (Data Lake)
resource "aws_s3_bucket" "data_lake" {
 # IMPORTANT: The bucket name must be UNIQUE worldwide across all of AWS
 # Change "your-name" to your real name or a random number
  bucket = "${var.project_name}-data-tu-nombre"
  
 # This allows us to delete the bucket completely from Terraform at the end of the project,
 # even if it has files inside (useful to avoid leaving resources running and incurring costs).
  force_destroy = true 
}

# 3. Security: Public Access Block
resource "aws_s3_bucket_public_access_block" "data_lake_security" {
  bucket = aws_s3_bucket.data_lake.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}