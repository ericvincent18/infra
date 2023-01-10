#!/bin/bash

kind create cluster
kind get kubectl
kubectl cluster-info --context kind-kind
kubectl create namespace rabbitmq-mysql
