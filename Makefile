namespace=internet-banking

minikube:
	minikube start
	minikube status
	minikube addons enable ingress

kubernetes:
	kubectl apply -f k8s/config
	kubectl -n ${namespace} apply -f k8s/ingress
	kubectl -n ${namespace} apply -f k8s/postgres
	kubectl -n ${namespace} apply -f k8s/user
	kubectl -n ${namespace} apply -f k8s/credit_card
	kubectl -n ${namespace} apply -f k8s/bank_account
	kubectl -n ${namespace} apply -f k8s/prometheus
	kubectl -n ${namespace} apply -f k8s/grafana

databases:
	kubectl -n ${namespace} exec -it services/user-svc python manage.py migrate
	kubectl -n ${namespace} exec -it services/bank-account-svc python manage.py migrate
	kubectl -n ${namespace} exec -it services/credit-card-svc python manage.py migrate

kube-events:
	kubectl -n ${namespace} get events

kube-pods:
	kubectl -n ${namespace} get pods

kube-services:
	kubectl -n ${namespace} get services

kube-ingress:
	kubectl -n ${namespace} get ingress

kube-all:
	kubectl -n ${namespace} get all

start-postgres:
	kubectl -n ${namespace} exec -it services/postgres-svc -- /bin/bash

start-user:
	kubectl -n ${namespace} exec -it services/user-svc -- /bin/bash

start-bank-account:
	kubectl -n ${namespace} exec -it services/bank-account-svc -- /bin/bash

start-credit-card:
	kubectl -n ${namespace} exec -it services/credit-card-svc -- /bin/bash
