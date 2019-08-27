# Exercise-3

Welcome to exercise-3. Here we will play around with PODs

## Sample commands

By default minikube comes with some sets of pods which are required to run the Kubernetes cluster.

List all the pods in the cluster:

```bash
kubectl get pod --all-namespaces
```

List all the pods in namespace kube-system

```
kubectl get pod -n kube-system
```

List all the pods with label **k8s-app=kube-dns**:

```bash
kubectl get pod --all-namespaces -l k8s-app=kube-dns
```

Show more information about the pods:

```bash
kubectl describe pod <pod_name>
```

Delete pod:
```bash
kubectl delete pod <pod_name>
```

Print the actual pod declaration in YAML:

```bash
kubectl get pod <pod_name> -o yaml
```

Edit the pod (it will not work):

```bash
kubectl edit pod <pod_name>
```

Access the shell of pod

```bash
kubectl exec -it <pod_name> -- /bin/sh
```

## Create new pod

The file **pod.yaml** contain the manifest of our pod with the image we built earlier. Run the pod:

```bash
kubectl apply -f pod.yaml
```

Access the API:

```bash
kubectl port-forward <pod_name> 8080:5000
```

## Tasks

1. Print the information about pod
2. Add liveness probe to the pod
3. Access the pod
4. Create the init container which will download some random webpage and save it under /app/website.html
5. Delete pod

