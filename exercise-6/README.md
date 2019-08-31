# Exercise-6

Welcome to exercise-6. Here we will create the deployment object and try to use its own super powers!

## Sample usage

1. Create new deployment from the CLI

```bash
kubectl run <name_of_deployment> --image=<image> --dry-run -o yaml
```

2. Create new deployment from the manifest

```bash
kubectl create -f deployment.yaml
```

3. Show the deployment and its details

```bash
kubectl get deployment
kubectl describe deployment <deployment_name>
```

4. Change the deployment image

```bash
kubectl set image deployment/training-api training-api=mycloudfun/training-api:2.0
```

5. See the status of rollout 

```bash
kubectl rollout status deployment/training-api
```

## Tasks

1. Using **port-forward** access the deployment and check the content of **/website** endpoint
2. Change the image to **mycloudfun/training-api:3.0**
3. Check the **/website** endpoint again
4. Check the history rollout
5. Using **kubectl rollout undo** revert back to first deployment from the history
6. Check the **/website** endpoint again
7. Destroy all the resources you created in this exercise

