# Kubernetes API

In this exercise we will walkthrough the Kubernetes API objects

## ASDF Installation

Before we begin the actual work, it necessary to set up the computer environment. I strongly recommend using **asdf** tool to manage the stack of cloud native best applications.

[https://github.com/asdf-vm/asdf](https://github.com/asdf-vm/asdf)

Here are some of examples of usage:

```bash
# Installation:
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.7.6

# Install dependencies
sudo apt install \
  automake autoconf libreadline-dev \
  libncurses-dev libssl-dev libyaml-dev \
  libxslt-dev libffi-dev libtool unixodbc-dev \
  unzip curl -y

# Bash configuration
echo -e '\n. $HOME/.asdf/asdf.sh' >> ~/.bashrc
echo -e '\n. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc

# List available packages
asdf plugin list all

# Enable example plugin and install with desired version
asdf plugin add kubectl
asdf install kubectl latest

# List installed packages
asdf list

# List all available versions of given package
asdf list all kubectl

# Set the version globally or locally 
# Global writes to $HOME/.tool-version
asdf global kubectl 1.17.2

# Local writes to $PWD/.tool-versions
asdf local kubectl 1.17.2

# List current versions
asdf current
```

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
