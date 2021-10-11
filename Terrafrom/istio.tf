resource "helm_release" "istio_base" {
  name  = "istio-base"
  chart = "istio-1.11.3/manifests/charts/base"

  timeout = 120
  cleanup_on_fail = true
  force_update    = true
  namespace       = "istio-system"


  depends_on = [digitalocean_kubernetes_cluster.my_cluster, kubernetes_namespace.istio_system]
}

resource "helm_release" "istiod" {
  name  = "istiod"
  chart = "istio-1.11.3/manifests/charts/istio-control/istio-discovery"

  timeout = 120
  cleanup_on_fail = true
  force_update    = true
  namespace       = "istio-system"

  depends_on = [digitalocean_kubernetes_cluster.my_cluster, kubernetes_namespace.istio_system, helm_release.istio_base]
}

resource "helm_release" "istio_ingress" {
  name  = "istio-ingress"
  chart = "istio-1.11.3/manifests/charts/gateways/istio-ingress"

  timeout = 120
  cleanup_on_fail = true
  force_update    = true
  namespace       = "istio-system"

  depends_on = [digitalocean_kubernetes_cluster.my_cluster, kubernetes_namespace.istio_system, helm_release.istiod]
}

resource "helm_release" "istio_egress" {
  name  = "istio-egress"
  chart = "istio-1.11.3/manifests/charts/gateways/istio-egress"

  timeout = 120
  cleanup_on_fail = true
  force_update    = true
  namespace       = "istio-system"

  depends_on = [digitalocean_kubernetes_cluster.my_cluster, kubernetes_namespace.istio_system, helm_release.istiod]
}
