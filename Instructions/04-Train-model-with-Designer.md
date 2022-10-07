---
lab:
    title: 'Work with environments in Azure Machine Learning'
---

# Work with environments in Azure Machine Learning

Determining the right algorithm and preprocessing transformations for model training can involve a lot of guesswork and experimentation.

In this exercise, you'll use automated machine learning to determine the optimal algorithm and preprocessing steps for a model by performing multiple training runs in parallel.

## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free) in which you have administrative-level access.

## Provision an Azure Machine Learning workspace

An Azure Machine Learning *workspace* provides a central place for managing all resources and assets you need to train and manage your models. You can interact with the Azure Machine Learning workspace through the Studio, Python SDK, and Azure CLI. 

You'll use the Azure CLI to provision the workspace and necessary compute, and you'll use the Python SDK to train a classification model with Automated Machine Learning.

### Create the workspace

1. In a browser, open the Azure portal at [http://portal.azure.com](https://portal.azure.com/?azure-portal=true), signing in with your Microsoft account.
1. Select the [>_] (*Cloud Shell*) button at the top of the page to the right of the search box. This opens a Cloud Shell pane at the bottom of the portal.
1. The first time you open the cloud shell, you will be asked to choose the type of shell you want to use (*Bash* or *PowerShell*). Select **Bash**.
1. If you are asked to create storage for your cloud shell, check that the correct subscription is specified and select **Create storage**. Wait for the storage to be created.
1. To avoid any conflicts with previous versions, remove any ML CLI extensions (both version 1 and 2) with this command:
    ```
    az extension remove -n azure-cli-ml
    az extension remove -n ml
    ```
1. Install the Azure Machine Learning (v2) extension with the following command:
    ```
    az extension add -n ml -y
    ```
1. Create a resource group. Choose a location close to you.
    ```azurecli
    az group create --name "rg-dp100-labs" --location "eastus"
    ```
1. Create a workspace:
    ```azurecli
    az ml workspace create --name "mlw-dp100-labs" -g "rg-dp100-labs"
    ```
1. Wait for the workspace and its associated resources to be created - this typically takes around 5 minutes. 

### Create a compute instance

You'll use a compute instance to run a Jupyter notebook. From the notebook, you'll submit the automated machine learning job.

1. Replace "XX" with your initials in the command below. Then, use the command to create a compute instance in your workspace.
    ```azurecli
    az ml compute create --name "vm-dev-XX" --size STANDARD_DS11_V2 --type ComputeInstance -w mlw-dp100-labs -g rg-dp100-labs
    ```

<br>
<details>
<summary>Click to troubleshoot the error: <span style="background-color: #FF0000"><font color="white">A compute instance with this name already exists.</span></font></summary>
If the following message appears in the Azure Cloud Shell:

<code>
Failed to connect to MSI. Please make sure MSI is configured correctly.
Get Token request returned: &lt;Response [400]&gt;
</code>
<br>
Delete the (partially) created compute instance using:
<code>
az ml compute delete "&lt;your-compute-instance-name&gt;"
</code>

And rerun the command to create a compute instance with a different name for your compute. Try adding random numbers after your initials for a more unique name.
</details>

### Create a compute cluster

You'll train multiple models with Automated Machine Learning and compare them to decide which is the *best* (according to your primary metric). To train multiple models at the same time, you'll need a compute cluster with multiple nodes.

1. Use the command to create a compute cluster in your workspace.
    ```azurecli
    az ml compute create --name "aml-cluster" --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute -w mlw-dp100-labs -g rg-dp100-labs
    ```

## Clone the lab materials

When you've created the workspace and necessary compute resources, you can open the Azure Machine Learning Studio and clone the lab materials. 

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
    git clone https://github.com/MicrosoftLearning/dp100-auto-ml.git dp100-auto-ml
    ``` 
1. When the command has completed, in the **Files** pane, click **&#8635;** to refresh the view and verify that a new **/users/*your-user-name*/dp100-auto-ml** folder has been created. 

## Train a computer vision model with Automated Machine Learning

INSTRUCTIONS HERE

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should **either**:
- Minimize costs by stopping the compute instance if you want to reuse the workspace for other exercises.
- Delete all Azure resources you created.

### Minimize costs and stop the compute instance
1. In Azure Machine Learning studio, on the **Compute** page, select your compute instance.
2. Click **Stop** to stop your compute instance. When it has shut down, its status will change to **Stopped**.

> **Note**: Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription.

### Delete all Azure resources you created
1. Close the Azure Machine Learning Studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-labs** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**. 
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
