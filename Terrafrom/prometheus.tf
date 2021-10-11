resource "helm_release" "prometheus" {
  chart = "prometheus"
  name = "prometheus"
  namespace = "prometheus"
  repository = "https://prometheus-community.github.io/helm-charts"
}
