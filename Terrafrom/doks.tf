
resource "digitalocean_kubernetes_cluster" "my_cluster" {
  name = "my-cluster"
  region = "blr1"
  version = "1.21.3-do.0"

  node_pool {
      name = "my-pool"
      size = "s-2vcpu-4gb"
      node_count = 3
  }
}

resource "kubernetes_namespace" "istio_system" {
  metadata {
    name = "istio-system"
  }
}

resource "kubernetes_namespace" "prometheus" {
  metadata {
    name = "prometheus"
  }
}

resource "kubernetes_namespace" "grafana" {
  metadata {
    name = "grafana"
  }
}
