data "template_file" "grafana_values" {
	template = file("./templates/grafana-values.yml")

  	vars = {
	  GRAFANA_SERVICE_ACCOUNT = "grafana"
	  GRAFANA_ADMIN_USER = "admin"
	  GRAFANA_ADMIN_PASSWORD = 5028
	  PROMETHEUS_SVC = "${helm_release.prometheus.name}-server"
	  NAMESPACE = "grafana"
	}
}

resource "helm_release" "grafana" {
  chart = "grafana"
  name = "grafana"
  repository = "https://grafana.github.io/helm-charts"
  namespace = "grafana"

}
