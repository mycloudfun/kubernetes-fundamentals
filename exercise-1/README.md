# Kubernetes API

In this excercise we will walkthrough the kubernetes API objects

## Use an HTTP Proxy to Access the Kubernetes API

Before you begin, make sure you have an access to running K8s cluster and your **kubectl** is configured to access it.

Make an HTTP Proxy

```bash
kubectl proxy --port=8080
```

## Exploring the Kubernetes API

Open another console and run below set of commands to explore the API:

```bash
# Get the API versions
curl http://localhost:8080/api

# Get a list of pods in kube-system namespace
curl http://localhost:8443/api/v1/namespaces/kube-system/pods

# Get a list of nodes
curl http://localhost:8443/api/v1/nodes

# Get a list of available objects from apps/v1 apis
curl http://localhost:8443/apis/apps/v1/

# Create new namespace
curl http://localhost:8443/api/v1/namespaces/ -k -H "Content-Type: application/json" -XPOST -d '
{
    "apiVersion": "v1",
    "kind": "Namespace",
    "metadata": {
        "name": "kubernetes-training"
    }
}'
```
