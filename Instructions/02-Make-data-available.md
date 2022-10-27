---
lab:
    title: 'Make data available in Azure Machine Learning'
---

# Make data available in Azure Machine Learning

Although it's fairly common to work with data on their local file system, in an enterprise environment it can be more effective to store the data in a central location where multiple data scientists and machine learning engineers can access it.

In this exercise, you'll explore *datastores* and *data assets*, which are the primary objects used to abstract data access in Azure Machine Learning.


## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free) in which you have administrative-level access.

## Provision an Azure Machine Learning workspace

An Azure Machine Learning *workspace* provides a central place for managing all resources and assets you need to train and manage your models. You can interact with the Azure Machine Learning workspace through the Studio, Python SDK, and Azure CLI. 

You'll use a Shell script which uses the Azure CLI to provision the workspace and necessary resources. Next, you'll use the Designer in the Azure Machine Learning Studio to train and compare models.

### Create the workspace and compute resources

To create the Azure Machine Learning workspace and compute resources, you'll use the Azure CLI. All necessary commands are grouped in a Shell script for you to execute.
1. In a browser, open the Azure portal at [http://portal.azure.com](https://portal.azure.com/?azure-portal=true), signing in with your Microsoft account.
1. Select the [>_] (*Cloud Shell*) button at the top of the page to the right of the search box. This opens a Cloud Shell pane at the bottom of the portal.
1. The first time you open the cloud shell, you will be asked to choose the type of shell you want to use (*Bash* or *PowerShell*). Select **Bash**.
1. If you are asked to create storage for your cloud shell, check that the correct subscription is specified and select **Create storage**. Wait for the storage to be created.
1. In the terminal, enter the following commands to clone this repo:
    ```bash
    rm -r azure-ml-labs -f
    git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git azure-ml-labs
    ```
1. After the repo has been cloned, enter the following commands to change to the folder for this lab and run the `setup.sh` script it contains:
    ```bash
    cd azure-ml-labs/Labs/04
    ./setup.sh
    ```
1. Wait for the script to complete - this typically takes around 5-10 minutes. 

## Explore the default datastores

When you create an Azure Machine Learning workspace, a Storage Account is automatically created and connected to your workspace. You'll explore how the Storage Account is connected.

1. In the Azure portal, navigate to the new resource group named `rg-dp100-labs`.
1. Select the Storage Account in the resource group. The name often starts with the name you provided for the workspace (without hyphens).
1. Review the **Overview** page of the Storage Account. Note that the Storage Account has several options for **Data storage** as shown in the Overview pane, and in the left menu.
1. Select **Containers** to explore the Blob storage part of the Storage Account. 
1. Note the **azureml-blobstore-...** container. The default datastore for data assets uses this container to store data. 
1. Using the &#43; **Container** button at the top of the screen, create a new container and name it `training-data`. 
1. Select **File shares** from the left menu to explore the File share part of the Storage Account.
1. Note the **code-...** file share. Any notebooks in the workspace are stored here. After cloning the lab materials, you can find the files in this file share, in the **code-.../Users/*your-user-name*/azure-ml-labs** folder.

## Copy the access key

To create a datastore in the Azure Machine Learning workspace, you need to provide some credentials. An easy way to provide the workspace with access to a Blob storage is to use the account key.

1. In the Storage Account, select the **Access keys** tab from the left menu.
1. Note that two keys are provided: key1 and key2. Each key has the same functionality. 
1. Select **Show** for the **Key** field under **key1**.
1. Copy the value of the **Key** field to a notepad. You'll need to paste this value into the notebook later. 

> **Note**:
> Copy the account key to a notepad to avoid automatic capitalization (which happens in Word). The key is case-sensitive.

## Clone the lab materials

To create a datastore and data assets with the Python SDK, you'll need to clone the lab materials into the workspace.

1. In the Azure portal, navigate to the Azure Machine Learning workspace named `mlw-dp100-labs`.
1. Select the Azure Machine Learning workspace, and in its **Overview** page, select **Launch studio**. Another tab will open in your browser to open the Azure Machine Learning Studio.
1. Within the Azure Machine Learning Studio, navigate to the **Compute** page and verify that the compute instance and cluster you created in the previous section exist. The compute instance should be running, the cluster should be idle and have 0 nodes running.
1. In the **Compute instances** tab, find your compute instance, and select the **Terminal** application.
1. In the terminal, install the Python SDK on the compute instance by running the following commands in the terminal:
    
    ```
    pip uninstall azure-ai-ml
    pip install azure-ai-ml
    ```

1. Run the following command to clone a Git repository containing a notebook, data, and other files to your workspace:
    
    ```
    git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git azure-ml-labs
    ```
 
1. When the command has completed, in the **Files** pane, click **&#8635;** to refresh the view and verify that a new **/users/*your-user-name*/azure-ml-labs** folder has been created. 

**Optionally**, in another browser tab, navigate back to the [Azure portal](https://portal.azure.com). Explore the file share **code-...** in the Storage account again to find the cloned lab materials in the newly created **azure-ml-labs** folder.

## Create a datastore and data assets

The code to create a datastore and data assets with the Python SDK is provided in a notebook.

1. Open the **Labs/02/Work with data.ipynb** notebook.
1. Run all cells in the notebook.

**Optionally**, navigate to the **Data** tab in the Azure Machine Learning Studio to explore the data assets. Select the `diabetes-local` data asset name to explore its details. Under **Data sources** for the `diabetes-local` data asset, you'll find where the file has been uploaded to. The path starting with **LocalUpload/...** shows the path within the Storage Account container **azureml-blobstore-...**. You can verify the file exists by navigating to that path in the Azure portal.

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should delete the resources you've created to avoid unnecessary Azure costs.

1. Close the Azure Machine Learning Studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-labs** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**. 
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
