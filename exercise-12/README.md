# Exercise-12

Welcome to exercise-12. It will be about the Ingress and IngressControllers

## Sample usage

1. Make sure the Ingress Controller is enabled in minikube:

```bash
minikube addons list
kubectl get pod -n kube-system
```

2. Create the deployment, service and ingress:

```bash
kubectl create -f .
```

3. Get information about the ingress:

```bash
kubectl get ingress
kubectl describe ingress <ingress_name>
```

4. Configure your local machine to access the deployment via ingress:

```bash
# edit /etc/hosts or %SystemRoot%\system32\drivers\etc\hosts in Windows

# add entry like (replace $minikubeip with the actual value of command 'minikube ip')
$minikubeip training-api.pl
```

5. Check if you can access the deployment

```bash
curl training-api.pl/info
```

## Tasks

1. Add another URL **website.info** and try to access it
2. Destroy created resources