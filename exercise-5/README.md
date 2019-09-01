# Exercise-5

Welcome to exercise-5. Here we will try to configure and modify ReplicaSet object.

## Sample commands

List all of the ReplicaSets in the cluster:

```bash
kubectl get replicaset --all-namespaces

or

kubectl get rs --all-namespaces
```

Describe the replicaset object:

```bash
kubectl describe rs <name>
```

Edit the repolicaset object:

```bash
kubectl edit rs <name>
```

Scale the repolicaset:

```bash
kubectl scale --replicas=3 rs/<name>

or based on config file

kubectl scale --replicas=3 -f <replicaset-file>.yaml
```

## Tasks

1. Create the ReplicaSet and Service from provided .yaml files
2. Check the number of running replicas
3. Use **kubectl port-forward** command to access the service and hit into endpoint **/info**
4. Destroy the pod displayed in previous command, re-run the **kubectl port-forward** and hit again the endpoint
5. Scale the ReplicaSet to 5 replicas
6. Destroy the objects created in this exercise
