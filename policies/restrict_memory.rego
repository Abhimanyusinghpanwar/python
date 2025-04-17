package spacelift

deny contains msg if {
  input.resource_type == "google_cloud_run_service"
  input.change.after.template.spec.containers[_].resources.limits.memory > "1Gi"
  msg := "Memory limit cannot exceed 1Gi"
}
