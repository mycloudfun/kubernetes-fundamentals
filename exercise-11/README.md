# Exercise-11

Welcome to exercise-11. It will be about the DNS

## Sample usage

1. List the deployment, which provides the CoreDNS service

```bash
kubectl get deployment -n kube-system
```

2. List the pods of DNS

```bash
kubectl get pod -n kube-system -l k8s-app=kube-dns
```

## Tasks

1. Check the current configuration of DNS
2. Change to configuration to enable the logging (https://github.com/coredns/coredns/tree/master/plugin/log)[https://github.com/coredns/coredns/tree/master/plugin/log]
3. Using **kubetail** try to see the logs
4. Revert back the change