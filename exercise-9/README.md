# Exercise-9

Welcome to exercise-8. It will be about StatefulSet

## Sample usage

1. Create the Headless Service

```bash
kubectl create -f service.yaml
kubectl get svc
kubectl describe svc training-api
```

2. Create a StorageClass to Enable Dynamic Provisioning of PersistentVolumes for the Statefulset

```bash
kubectl create -f sc.yaml
kubectl get sc
```

3. Create a StatefulSet

```bash
kubectl create -f statefulset.yaml

## Watch how the pods are deployed
kubectl get pods -w -l app=training-api

kubectl describe ss training-api
```

## Tasks

1. Access the single pod and create some file under /data directory
2. Check if the same file exist in other pod
3. Delete the pod and check if the file is still there
4. Check the content of **/mnt/sda1/hostpath-provisioner/** folder inside the minikube
5. Check using nslookup entries for 3 of created pods. You can do it from one of the pods from Statefulset. E.g. **nslookup training-api-0.api-svc**
6. Delete create resources