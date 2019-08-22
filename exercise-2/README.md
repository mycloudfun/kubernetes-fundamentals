# Exercise-2

Welcome to exercise-2. Here I'm going to show you how to install the minikube on your local machine as well as show some of the basic commands.

## Prerequisites

1. PC with min 8GB of RAM and 2x vCPU
2. OS (Minikube supports both Windows and Linux)
3. VirtualBox
4. Kubectl

More information at:

(https://kubernetes.io/docs/tasks/tools/install-minikube/)[https://kubernetes.io/docs/tasks/tools/install-minikube/]

## Instalation

1. Download the Latest version of Virtualbox and install it:

(https://www.virtualbox.org/)[https://www.virtualbox.org/]

2. Download the latest version of Kubectl and install it:

(https://kubernetes.io/docs/tasks/tools/install-kubectl/)[https://kubernetes.io/docs/tasks/tools/install-kubectl/]

3. Download and install the minikube

(https://github.com/kubernetes/minikube/releases)[https://github.com/kubernetes/minikube/releases]


## Initial start

In order to start the minikube, is enough to type below command on your shell or CMD:

```bash
minikube start
```

It takes some time for the first time, as the minikube must pull the image and configure new VM on the Virtualbox. So wait a while

Once completed, run the kubectl command to see if the connection works

```bash
kubectl get nodes
```

## Few words about the kubeconfig file

Kubeconfig files is made of 3 sections:
- server
- context
- user

By default, you can find it at:

```bash
~/.kube/config # Linux

%USERPROFILE%/.kube/config # Windows
```

The location can be controller by environment variable **KUBECONFIG**

## Advanced usage

Some advance minikube commands:

```bash
# Print the hep
minikube help

# Start the minikube with bigger Hardware
minikube start --cpus 4 --memory 8192

# Show the status of minikube
minikube status

# SSH into the host
minikube ssh

# Show the IP
minikube ip

# Delete the cluster
minikube delete
```

## Addons

Minikube by default comes with a couple of addons. But you need to enable some of them first. Here are some usefull commands:

```bash
# Show available addons
minikube addons list

# Enable dashboard
minikube addons enable dashboard

# Disable dashboard
minikube addons disable dashboard
```

