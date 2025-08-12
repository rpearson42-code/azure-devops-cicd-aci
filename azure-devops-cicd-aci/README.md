# Azure DevOps CI/CD with Azure Containers (ACI)
Demo of CI/CD using Azure Pipelines to build, test, and deploy a Dockerized Flask API to Azure Container Instances. Includes Bicep IaC for deployment.

## Local
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py

## Docker
docker build -t azure-devops-cicd-aci:local .
docker run -p 8080:8080 -e APP_ENV=local -e APP_VERSION=dev azure-devops-cicd-aci:local

## Pipeline setup
- Edit placeholders in azure-pipelines.yml
- Create pipeline secrets: ACR_USERNAME, ACR_PASSWORD
- Create service connection: YOUR_AZURE_SERVICE_CONNECTION

## IaC
iac/main.bicep provisions an ACI with public IP and env vars.
