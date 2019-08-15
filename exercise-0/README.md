# Exercise-0

Welcome to exercise-0. Here I'm going to show you some of the basics of Docker and Linux containers.

## Prerequisites

1. Linux OS
2. Docker engine
   - Installation:

```bash
$ curl -fsSL https://get.docker.com/ | sh
``` 

In case you have minikube on your PC, run below command to get into the minikube VM and start using docker.

```bash
$ minikube ssh
```

## Sample usage

1. Display help and version

```bash
docker help
docker version
```

2. Display locally stored images

```bash
docker image ls
```

3. Display all running and stopped containers

```bash
docker container ls -a
```

4. Docker build a sample image and tag it

```bash
docker build -t k8s-training/api:1.0 .
```

5. Run locally built image

bash
```
docker run -p 5000:5000 --name my-api -dt k8s-training/api:1.0
```

6. Get into the shell of started container

```bash
docker exec -it my-api /bin/sh
```

7. More examples at official Docker Cheat Sheet

[https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf)

## Minikube examples

1. Login to minikube

```bash
minikube ssh
```

2. Run the toolbox

[https://github.com/coreos/toolbox](https://github.com/coreos/toolbox)

```bash
toolbox
```

3. Start sample python webapp

```bash
pip3 install flask==1.1.1

cat << EOF > app.py
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
EOF

python3 app.py 
```

4. Check if the application is running:

```bash
curl $(minikube ip):5000

curl $(minikube ip):5000/andrzej
```
