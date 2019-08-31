# Exercise-7

Welcome to exercise-7. It will be about the ConfigMaps and Secrets

## ConfigMap

1. Create the configMap from the literal

```bash
kubectl create configmap app-config-1 --from-literal=APP_PORT=8888 --from-literal=APP_NAME=test_app
```

2. Create the configMap from the file

```bash
kubectl create configmap app-config-2 --from-file=config.ini
```

3. Create the configMap from the Manifest

```bash
kubectl create -f configMap.yaml
```

4. Display the configMaps

```bash
kubectl get configmaps <configmap> -o yaml
kubectl describe configmap <configmap>
```

5. Apply the example deployment which uses the ConfigMap and check the logs

```bash
kubectl create -f deployment.yaml

kubectl get pod

# Take a note of pod name from above and use here
kubectl logs <pod_name> -f
```

## Secrets

1. Create the secrets from the manifest

```bash
kubectl create -f secret.yaml
```

2. Get the value of secret

```bash
kubectl get secret
kubectl get secret mysecret -o yaml
```

3. Decode the secret

```bash
echo '<value>' | base64 -d
```

## Tasks

1. Configure deployment to use the environment APP_PORT value from the secret
2. Check if you your setup is working
3. Destroy all the resources