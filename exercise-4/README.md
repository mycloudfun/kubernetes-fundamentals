# Exercise-4

Welcome to exercise-4. Here we will work with the Service object.

## Sample commands

List all the services:

```bash
kubectl get services --all-namespaces
```

Create the template of service from the kubectl:

```bash
kubectl expose <pod,deployment> --port=8080 --dry-run -o yaml
```

Describe the service:

```bash
kubectl describe svc <name>
```

## Tasks

1. Create the service and pod from provided .yaml files
2. Access the service using **kubectl proxy-forward** command
3. Change the type of service to NodePort
4. Try to access the service from **minikube service <name> --url** command
5. Delete all created resources
