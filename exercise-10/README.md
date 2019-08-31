# Exercise-10

Welcome to exercise-10. It will be about the DaemonSet

## Sample usage

1. Create the DaemonSet from the provided manifest:

```bash
kubectl create -f daemonSet.yaml
```

2. Get the pod name

```bash
kubectl get pod -n kube-system
```

3. Investigate the DaemonSet config

```bash
kubectl describe ds -n kube-system
```

## Tasks

1. Delete created resources