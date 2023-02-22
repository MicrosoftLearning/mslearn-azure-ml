#! /usr/bin/sh

# Create workspace
echo "Create a resource group:"
az group create --name "rg-dp100-labs" --location "eastus"

echo "Create an Azure Machine Learning workspace:"
az ml workspace create --name "mlw-dp100-labs" -g "rg-dp100-labs"

# Create compute cluster
echo "Creating a compute cluster with name: aml-cluster"
az ml compute create --name "aml-cluster" --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute -w mlw-dp100-labs -g rg-dp100-labs

# Create data asset
echo "Creating a data asset with name: diabetes-folder"
az ml data create --name diabetes-folder --path ./data -w mlw-dp100-labs -g rg-dp100-labs

# Create components
echo "Creating components"
az ml component create --file ./fix-missing-data.yml -w mlw-dp100-labs -g rg-dp100-labs
az ml component create --file ./normalize-data.yml -w mlw-dp100-labs -g rg-dp100-labs
az ml component create --file ./train-decision-tree.yml -w mlw-dp100-labs -g rg-dp100-labs
az ml component create --file ./train-logistic-regression.yml -w mlw-dp100-labs -g rg-dp100-labs
