variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud Region where the Cloud Run service will be deployed"
  type        = string
}

variable "container_image" {
  description = "Container image URL in Google Container Registry (GCR)"
  type        = string
}

variable "GCR_SERVICE_ACCOUNT_KEY" {
  type        = string
  description = "GCP Service Account key in JSON format"
}

variable "spacelift_commit_sha" {
  type = string
}
