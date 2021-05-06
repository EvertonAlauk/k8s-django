# Internet Banking

## Requirements

- Django
- Postgres
- Prometheus
- Grafana
- Github Actions
- Docker & docker-compose
- Kubernetes
- Minikube

## Sumary

- APIs:
    - [User](#api-user)
    - [Auth with JWT](#api-auth)
    - [Bank Account Balance](#api-balance)
    - [Bank Account Credit](#api-credit)
    - [Bank Account Debit](#api-debit)
    - [Bank Account Statement](#api-statement)
- [Prometheus](#prometheus)
- [Grafana](#grafana)
- [Github Actions](https://github.com/EvertonAlauk/flask-microservice-docker/actions)


## Docker-compose

``` shell
docker-compose up -d
```

or

## K8S

### Minikube <a name="minikube">

``` shell
make minikube
```

### Namespace and apps <a name="ns-apps">

``` shell
make kubernetes
```

### Create the databases <a name="tables">

``` shell
make databases
```

### Check your services

``` shell
make kube-services 
```

```
kubectl -n internet-banking get services
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
bank-account-svc   ClusterIP   10.109.219.209   <none>        5002/TCP   18d
postgres-svc       ClusterIP   10.107.25.52     <none>        5432/TCP   18d
user-svc           ClusterIP   10.97.213.50     <none>        5001/TCP   18d
```

## With [httpie](https://httpie.io/):

### Run the user API throught the kubernetes container

Notice that your services with Flask application has avaliable at `5001`, `5002` and `5003` port address. Use `ingress` to acess then.


``` shell
make kube-ingress    
```

```
kubectl -n internet-banking get ingress
NAME      CLASS     HOSTS   ADDRESS        PORTS   AGE
ingress   ingress   *       192.168.49.2   80      15d
```

### User <a name="api-user">


``` shell
http POST 192.168.49.2/user username="user" email="user@teste.com" password="password123" name="user"
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 54
Content-Type: application/json
Date: Sun, 14 Mar 2021 23:38:35 GMT
Server: gunicorn/20.0.4

[
    {
        "active": true,
        "created": "2021-03-15T00:08:14.180200",
        "email": "user@teste.com",
        "id": 1,
        "name": "user",
        "username": "user"
    }
]
```


``` shell
http 192.168.49.2/user
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 54
Content-Type: application/json
Date: Sun, 14 Mar 2021 23:39:01 GMT
Server: gunicorn/20.0.4

[
    {
        "active": true,
        "created": "2021-03-15T00:08:14.180200",
        "email": "user@teste.com",
        "id": 1,
        "name": "user",
        "username": "user"
    }
]
```

### Auth JWT <a name="api-auth">

``` shell
http POST 192.168.49.2/user/auth -a user:password123
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 54
Content-Type: application/json
Date: Sun, 14 Mar 2021 23:39:01 GMT
Server: gunicorn/20.0.4

{
    "expired": 1615813569.092066,
    "token": "token"
}
```

### Bank Account: Balance <a name="api-balance">

It's important, just one time, to include a balance for user.
In this case, use the POST method.

``` shell
http POST 192.168.49.2/bank_account/balance/ value="2500.00" 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 40
Content-Type: application/json
Date: Sun, 21 Mar 2021 13:58:50 GMT
Server: gunicorn/20.0.4

{
    "id": 1,
    "user_id": 1,
    "value": 2500.0
}
```

Otherwise, GET method for check the balance.

``` shell
http 192.168.49.2/bank_account/balance/ 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 40
Content-Type: application/json
Date: Sun, 21 Mar 2021 13:58:50 GMT
Server: gunicorn/20.0.4

{
    "id": 1,
    "user_id": 1,
    "value": 2500.0
}
```

### Bank Account: Credit <a name="api-credit">

``` shell
http POST 192.168.49.2/bank_account/credit value="2.6" 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 38
Content-Type: application/json
Date: Sat, 20 Mar 2021 22:33:03 GMT
Server: gunicorn/20.0.4

{
    "id": 1,
    "user_id": 1,
    "value": 2.6
}
```

### Bank Account: Debit <a name="api-debit">

``` shell
http POST 192.168.49.2/bank_account/debit value="2.6" 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 38
Content-Type: application/json
Date: Sat, 20 Mar 2021 22:33:03 GMT
Server: gunicorn/20.0.4

{
    "id": 1,
    "user_id": 1,
    "value": 2.6
}
```

### Bank Account: Statement <a name="api-statement">

``` shell
http 192.168.49.2/bank_account/statement 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 142
Content-Type: application/json
Date: Sun, 21 Mar 2021 13:57:57 GMT
Server: gunicorn/20.0.4

{
    "credits": [
        {
            "id": 1,
            "user_id": 1,
            "value": 2.6
        },
        {
            "id": 2,
            "user_id": 1,
            "value": 5.1
        }
    ],
    "debits": [
        {
            "id": 1,
            "user_id": 1,
            "value": 4.9
        }
    ]
}
```

## Monitoring and metrics

### Prometheus <a name="prometheus">

``` shell
http://192.168.49.2:30000
```

### Grafana <a name="grafana">

``` shell
http://192.168.49.2:32000
```
