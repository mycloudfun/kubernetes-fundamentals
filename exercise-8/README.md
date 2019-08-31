# Exercise-8

Welcome to exercise-8. It will be about the PersistentVolumes and PersistentVolumeClaims

## PersistentVolume

1. Create the PV from the manifest file

```bash
kubectl create -f pv.yaml
```

2. List the PV

```bash
kubectl get pv
```

3. Get more information about the PV

```bash 
kubectl describe pv <name>
```

## PersistentVolumeClaim

1. Create the PVC from the manifest file

```bash
kubectl create -f pvc.yaml
```

2. List the PVCs

```bash
kubectl get pvc
```

3. Get more informatino about the pvc

```bash
kubectl describe pvc <name>
```

## Tasks

1. Create the **deployment.yaml** and examine the setup
2. Try to access the endpoint **/website** from the application using port-forward
3. Access the minikube and create any file with random content under **/data/website-vol/website.html**
4. Once again hit the endpoint **/website**
5. Destroy all the resources
6. Check the content of **/data/website-vol/** folder in minikube