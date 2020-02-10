# Exercise-17

Welcome to exercise-17. In this exercise we want provision the Argo CD and take a look on GitOps operations based on that application.

## Installation

Official project github page is:

[https://argoproj.github.io/argo-cd/](https://argoproj.github.io/argo-cd/)

List of official helm chart:

[https://github.com/argoproj/argo-helm/tree/master/charts/argo-cd](https://github.com/argoproj/argo-helm/tree/master/charts/argo-cd)

## Installation

1. Make sure you're using the latest HELM v3.

```bash
asdf plugin add helm
asdf install helm latest
asdf global helm 3.0.3
asdf current
```

2. Add official Argo CD repository to HELM:

```bash
helm repo add argo https://argoproj.github.io/argo-helm
```

3. List currently added repositories and the content of them:

```bash
helm repo list
helm search repo argo
```

4. Create **argocd** namespace:

```bash
kubectl create namespace argocd
```

5. Install Argo CD using Helm

```bash
helm install argocd -n argocd --version 1.7.3 argo/argo-cd --values values.yaml
```

6. Based on the output, get the credential to argocd and write it down.

7. Add entry to your local /etc/hosts

```bash
kubectl get ingress -n argocd

sudo vim /etc/hosts

192.168.99.103 argocd.minikube.local
```

8. Access the Argo CD website using URL: **https://argocd.minikube.local** and login using credential fetched in point 6.

## Create your first ArgoCD APP

1. Create new repository in Github.com or Gitlab.com.

2. Copy there files from this repository and commit the changes. Below steps are just an examples from mycloudfun repository.

```bash
git clone git@github.com:mycloudfun/myapp.git ~/myapp

cp deployment.yaml service.yaml ingress.yaml kustomization.yaml ~/myapp

cd ~/myapp

git add .
git commit -m "Initial commit"
git push
```

3. Create new Argo CD application by applying the CRD from this directory.

```bash
kubectl apply -f argo-app.yaml
```

4. View the CRD in K9S or kubectl as well as newly created objects in the clusters.

```bash
kubectl get application -n argocd
kubectl get all
```

5. Visit the Argo CD Website and watch the created objects.

## Task

1. Do small change in your git repository pointed in CRD and observe how Argo CD applies these changes to the cluster


