#! /bin/sh

# Create workspace
echo "Remove any ML CLI extensions to avoid conflicts:"
az extension remove -n azure-cli-ml
az extension remove -n ml

echo "Install the Azure Machine Learning extension:"
az extension add -n ml -y

echo "Create a resource group:"
az group create --name "rg-dp100-labs" --location "eastus"

echo "Create an Azure Machine Learning workspace:"
az ml workspace create --name "mlw-dp100-labs" -g "rg-dp100-labs"

# Create compute instance
RANDOM=$$

echo "Enter your initials (or a random string of letters):"
read compute1

ComputeName="ci-${compute1}${RANDOM}"

echo "Creating a compute instance with name: " $ComputeName
az ml compute create --name ${ComputeName} --size STANDARD_DS11_V2 --type ComputeInstance -w mlw-dp100-labs -g rg-dp100-labs

# Create compute cluster
echo "Creating a compute cluster with name: aml-cluster"
az ml compute create --name "aml-cluster" --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute -w mlw-dp100-labs -g rg-dp100-labs