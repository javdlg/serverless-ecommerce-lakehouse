output "s3_bucket_name" {
  description = "The exact name of the created bucket"
  value       = aws_s3_bucket.data_lake.bucket
}

output "s3_bucket_arn" {
  description = "The Amazon Resource Name of the bucket"
  value       = aws_s3_bucket.data_lake.arn
}