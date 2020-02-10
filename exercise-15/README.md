# Exercise-15

Welcome to exercise-15. In this exercise we want to take a look at the official deploy the Prometheus Operator using official helm chart.

## Helm

Official project github page is:

[https://github.com/helm/helm](https://github.com/helm/helm)

List of official helm charts and its repo is:

[https://github.com/helm/charts](https://github.com/helm/charts)

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

3. List currently added repositories and the content of them:

```bash
helm repo list
helm search repo stable
```

## Create HELM chart

1. Run below command to create your first helm chart template

```bash
helm create myapp
```

2. List created files and discover their values

```bash
tree
```

3. Modify the deployment values and service/ingress if needed to match your needs.

4. Overwrite default values to start deployment with 3 replicas and show the dry run output:

```bash
helm install myapp --dry-run --debug ./myapp
```

5. Validate the chart using linter to make sure you're following best practices

```bash
helm lint ./myapp
```

## HELM available options

1. List all installed charts

```bash
helm list --all-namespaces
```

2. Show information about the Chart

```bash
helm show all ./myapp
```

3. Get information about already installed charts

```bash
helm get all <chart>
```

4. Render the templates locally

```bash
helm template <name> <chart>
```

5. Uninstall the package

```bash
helm uninstall <name>
```

6. Create the package to share with others

```bash
helm package ./myapp
# it will produce the package with metadata as stated in Chart.yaml file
```

7. Create the helm repo

```bash
helm repo index my-repo/ --url https://github.com/<some_repository>

# copy the index.yaml file together with previously created chart archive *.tgz to your git repository

helm repo add my-repo https://github.com/<some_repository>

# install from your newly created repo

helm install my-repo/myapp --name=myapp
```
