#! /usr/bin/sh

# Create random string
guid=$(cat /proc/sys/kernel/random/uuid)
suffix=${guid//[-]/}
suffix=${suffix:0:18}

# Set the necessary variables
RESOURCE_GROUP="rg-dp100-l${suffix}"
RESOURCE_PROVIDER="Microsoft.MachineLearning"
REGIONS=("eastus" "westus" "centralus" "northeurope" "westeurope" "southeastasia")
RANDOM_REGION=${REGIONS[$RANDOM % ${#REGIONS[@]}]}
WORKSPACE_NAME="mlw-dp100-l${suffix}"
COMPUTE_CLUSTER="aml-cluster"

# Register the Azure Machine Learning resource provider in the subscription
echo "Register the Machine Learning resource provider:"
az provider register --namespace $RESOURCE_PROVIDER

# Create the resource group and workspace and set to default
echo "Create a resource group and set as default:"
az group create --name $RESOURCE_GROUP --location $RANDOM_REGION
az configure --defaults group=$RESOURCE_GROUP

echo "Create an Azure Machine Learning workspace:"
az ml workspace create --name $WORKSPACE_NAME 
az configure --defaults workspace=$WORKSPACE_NAME 

# Create compute cluster
echo "Creating a compute cluster with name: " $COMPUTE_CLUSTER
az ml compute create --name ${COMPUTE_CLUSTER} --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute 

# Create data asset
echo "Creating a data asset with name: diabetes-folder"
az ml data create --name diabetes-folder --path ./data -w mlw-dp100-labs -g rg-dp100-labs

# Create components
echo "Creating components"
az ml component create --file ./fix-missing-data.yml -w mlw-dp100-labs -g rg-dp100-labs
az ml component create --file ./normalize-data.yml -w mlw-dp100-labs -g rg-dp100-labs
az ml component create --file ./train-decision-tree.yml -w mlw-dp100-labs -g rg-dp100-labs
az ml component create --file ./train-logistic-regression.yml -w mlw-dp100-labs -g rg-dp100-labs
