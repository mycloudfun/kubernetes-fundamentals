# Exercise-16

Welcome to exercise-16. In this exercise we want to deploy the Prometheus Operator using official helm chart.

## Prometheus Operator

Official project github page is:

[https://github.com/coreos/prometheus-operator](https://github.com/coreos/prometheus-operator

Official helm chart and its repo is:

[https://github.com/helm/charts/tree/master/stable/prometheus-operator](https://github.com/helm/charts/tree/master/stable/prometheus-operator)

## Installation

1. Make sure you're using the latest HELM v3.

```bash
asdf plugin add helm
asdf install helm latest
asdf global helm 3.0.3
asdf current
```

2. Add official stable repository to HELM:

```bash
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
```

3. Create namespace "monitoring"

```bash
kubectl create namespace monitoring
```

4. Install Prometheus Operator in desired version, with default values in namespace monitoring:

```bash
helm install prometheus -n monitoring --version 8.7.0 stable/prometheus-operator
```

5. List installed objects in namespace monitoring as well as helm chart

```bash
kubectl get all -n monitoring
helm list -n monitoring
```

6. Create the port-forward to prometheus and visit the main dashboard:

```bash
kubectl port-forward service/prometheus-prometheus-oper-prometheus -n monitoring 9090:9090

http://localhost:9090
```

## Helm modification

1. Upgrade the helm chart by overwriting the default vaules using vaules.yaml from this repo:

```bash
helm upgrade prometheus -n monitoring --version 8.7.0 --values=values.yaml stable/prometheus-operator
```

2. Visit the prometheus dashboard again to see what has been changed.

## Modify Helm to create ingress for Prometheus

1. Upgrade the helm chart by overwriting the default vaules using vaules-ingress.yaml from this repo:

```bash
helm upgrade prometheus -n monitoring --version 8.7.0 --values=values-ingress.yaml stable/prometheus-operator
```

2. List ingress objects from namespace monitoring

```bash
kubectl get ingress -n monitoring
```

3. Create entries in your local /etc/hosts which points to the IP of minikube and matches hosts of created resources. Example:

```bash
sudo vim /etc/hosts

192.168.99.103 alertmanager.minikube.local
192.168.99.103 p8s.minikube.local
192.168.99.103 grafana.minikube.local
```

4. Try to access all of the three services using your browser

### Exercise

Please modify the chart to overwrite the default grafana dashboard password and rebuild it

## Create ServiceMonitor

1. Create sample microservice using config provided in this directory **microservice-example.yaml**

```bash
kubectl apply -f microservice-example.yaml
```

2. Add necessary entry to /etc/hosts based on ingress configuration

```bash
kubectl get ingress

sudo vim /etc/hosts

192.168.99.103 app.minikube.local
```

3. Query the microservice to get metrics informations

```bash
curl app.minikube.local/metrics
```

4. Review and create the ServiceMonitor object from this directory

```bash
kubectl apply -f serviceMonitor-example.yaml
```

5. Open the prometheus webpage. Go to status -> targets and see if you object has been registered.

6. Go back to main page and using PromQL query check if metrics are available

```bash
http_requests_total{job="prometheus-example"}
```

## Create custom dashboards

1. Visit the webpage: [https://grafana.com/grafana/dashboards](https://grafana.com/grafana/dashboards)

2. Go to Grafana and create new folder named: **MyDashboards**

3. Import custom dashboard number **11074** and save it under MyDashboards folder

4. Import custom dashboard to nginx and save it under MyDashboards folder