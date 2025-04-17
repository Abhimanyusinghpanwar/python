package spacelift

allowed_regions = {
  "us-central1",
  "us-east1",
  "us-east4",
  "us-west1",
  "us-west2",
  "us-west3",
  "us-west4",
  "northamerica-northeast1",
  "northamerica-northeast2"
}

deny contains msg if {
  input.resource_type == "google_cloud_run_service"
  not input.change.after.location in allowed_regions
  msg := "Region must be within USA or Canada"
}
