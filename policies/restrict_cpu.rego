package spacelift

deny contains msg if {
  input.resource_type == "google_cloud_run_service"
  input.change.after.template.spec.containers[_].resources.limits.cpu > "2"
  msg := "CPU limit cannot exceed 2"
}
