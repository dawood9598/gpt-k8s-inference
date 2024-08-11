This repository contains the necessary files and instructions to deploy a GPT-2 language model on Kubernetes using Helm. The setup includes creating a Kubernetes deployment, service, and ingress to expose the model for inference.

# Overview
The project demonstrates how to deploy an LLM (GPT-2) on Kubernetes. The application is containerized and deployed with a Helm chart, allowing for easy management and scalability. The service is exposed via a LoadBalancer, making it accessible for external use.
Features

# Containerized GPT Model: 
- The GPT-2 model is packaged in a Docker container for easy deployment.
- Helm Chart: A Helm chart (llm-inference-svc) is provided to manage Kubernetes resources.

# Prerequisites
1. Kubernetes cluster (Minikube, EKS, GKE, AKS, etc.)
2. Helm 3.x
3. Docker
4. kubectl

# Getting Started
1. Clone the Repository
```
git clone https://github.com/yourusername/gpt2-k8s-setup.git
```
2. Build the Docker Image
```
cd gpt2-k8s-setup
docker build -t yourusername/gpt2-api:latest .
docker push yourusername/gpt2-api:latest
```
3. Deploy with Helm
Install or upgrade the Helm chart to deploy the GPT-2 model on your Kubernetes cluster.
```
helm upgrade --install llm-inference-svc ./helm/llm-inference-svc
```
4. Access the Service
```
curl -X POST "http://<external-ip>:8080/generate-text" -H "Content-Type: application/json" -d '{"prompt": "Once upon a time", "max_length": 50}'
```



