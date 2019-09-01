# Exercise-14

Welcome to exercise-14. In this exercise we want to create our first Kubernetes operator and show the capabilities of CRD and operators

## Jenkins Operator

The project repository is available at: (https://github.com/jenkinsci/kubernetes-operator)[https://github.com/jenkinsci/kubernetes-operator]

The aim of this project is to create managed jenkins instance build natively in the Kubernetes.

## Operator Installation

1. Check what api-resources are currently available in our minikube cluster

```bash
kubectl api-resources
```

2. Configure Custom Resource Definition

```bash
kubectl apply -f https://raw.githubusercontent.com/jenkinsci/kubernetes-operator/master/deploy/crds/jenkins_v1alpha2_jenkins_crd.yaml
```

3. Check api-resources again

```bash
kubectl api-resources |grep -i jenkins
```

4. Install Jenkins Operator together with all dependencies (RBAC, ServiceAccount)

```bash
kubectl apply -f https://raw.githubusercontent.com/jenkinsci/kubernetes-operator/master/deploy/all-in-one-v1alpha2.yaml
```

5. Watch the pod to see if the operator is already installed

```bash
kubectl get pods -w
```
## Configure the Jeknins instance

When operator is up and running, we can start to provision the targer jenkins instance.

1. Review carefully the jenkins.yaml file and apply it

```bash
cat jenkins.yaml
kubectl create -f jenkins.yaml
```

2. Get the credentials to newly provisioned instance of jenkins

```bash
kubectl get secret jenkins-operator-credentials-training -o 'jsonpath={.data.user}' | base64 -d
kubectl get secret jenkins-operator-credentials-training -o 'jsonpath={.data.password}' | base64 -d
```

3. Access the instance 

```bash
minikube service jenkins-operator-http-training --url
```

