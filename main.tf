provider "google" {
  credentials = var.GCR_SERVICE_ACCOUNT_KEY
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_service" "starter-go-app" {
  name     = "starter-go-app"
  location = var.region

  template {
    spec {
      containers {
        image = "${var.container_image}:${substr(var.spacelift_commit_sha, 0, 8)}"

        resources {
          limits = {
            "memory" = "1024Mi"
            "cpu"    = "1"
          }
        }

        # Environment variables
        env {
          name  = "ENV"
          value = "development"
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  lifecycle {
    create_before_destroy = false
  }
}
