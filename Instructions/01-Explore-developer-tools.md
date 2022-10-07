---
lab:
    title: 'Explore developer tools for workspace interaction
'
---

# Explore developer tools for workspace interaction

You can use various tools to interact with the Azure Machine Learning workspace. Depending on what task you need to perform and your preference for developer tool, you can choose which tool to use when. This lab is designed as an introduction to the developer tools commonly used for workspace interaction. If you want to learn how to use a specific tool in more depth, there are other labs to explore.

This lab will take approximately **30** minutes to complete.

## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free) in which you have administrative-level access.

The commonly used developer tools for interacting with the Azure Machine Learning workspace are:
- **Azure CLI** with the Azure Machine Learning extension: This command-line approach is ideal for the automation of infrastructure.
- **Azure Machine Learning Studio**: Use the user-friendly UI to explore the workspace and all of its capabilities.
- **Python SDK** for Azure Machine Learning: Use to submit jobs and manage models from a Jupyter notebook, ideal for data scientists.

You'll explore each of these tools for tasks that are commonly done with that tool.

## Provision the infrastructure with the Azure CLI

For a data scientist to train a machine learning model with Azure Machine Learning, you'll need to set up the necessary infrastructure. You can use the Azure CLI with the Azure Machine Learning extension to create an Azure Machine Learning workspace and resources like a compute instance. 

To start, open the Azure Cloud Shell, install the Azure Machine Learning extension and clone the Git repo.

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

<br>
<details>
<summary>Click to troubleshoot the error: Failed to connect to MSI.</summary>
If the following message appears in the Azure Cloud Shell:

<code>
Failed to connect to MSI. Please make sure MSI is configured correctly.
Get Token request returned: &lt;Response [400]&gt;
</code>

Sign in to Azure again using:
<code>
az login
</code>

And follow the instructions for interactive login.
</details>

## Create a compute instance with the Azure CLI

Another important part of the infrastructure needed to train a machine learning model is compute. Though you can train models locally, it's more scalable and cost efficient to use cloud compute. 

When data scientists are developing a machine learning model in the Azure Machine Learning workspace, they want to use a virtual machine on which they can run Jupyter notebooks. For development, a compute instance is an ideal fit. 

After creating an Azure Machine Learning workspace, you can also create a compute instance using the Azure CLI. 

In this exercise, you'll create a compute instance with the following settings:
- **Compute name**: *Name of compute instance. Has to be unique and fewer than 24 characters.*
- **Virtual machine size**: STANDARD_DS11_V2
- **Compute type** (instance or cluster): ComputeInstance
- **Azure Machine Learning workspace name**: mlw-dp100-labs
- **Resource group**: rg-dp100-labs

1. Replace "XX" with your initials in the command below. Then, use the command to create a compute instance in your workspace.
    ```azurecli
    az ml compute create --name "vm-dev-XX" --size STANDARD_DS11_V2 --type ComputeInstance -w mlw-dp100-labs -g rg-dp100-labs
    ```

<br>
<details>
<summary>Click to troubleshoot the error: <b>A compute instance with this name already exists.</b></summary>

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

And rerun the command to create a compute instance with a different name for your compute.
</details>


## Create a compute cluster with the Azure CLI

Though a compute instance is ideal for development, a compute cluster is better suited when we want to train machine learning models. Only when a job is submitted to use the compute cluster, will it resize to more than 0 nodes and run the job. Once the compute cluster is no longer needed, it will automatically resize back to 0 nodes to minimize costs. 

To create a compute cluster, you can use the Azure CLI, similar to creating a compute instance. 

You'll create a compute cluster with the following settings:
- **Compute name**: *Name of compute cluster. Has to be unique and fewer than 24 characters.*
- **Virtual machine size**: STANDARD_DS11_V2
- **Compute type**: AmlCompute *(Creates a compute cluster)*
- **Maximum instances**: *Maximum number of nodes*
- **Azure Machine Learning workspace name**: mlw-dp100-labs
- **Resource group**: rg-dp100-labs

1. Replace "XX" with your initials in the command below. Then, use the command to create a compute cluster in your workspace.
    ```azurecli
    az ml compute create --name "vm-cluster-XX" --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute -w mlw-dp100-labs -g rg-dp100-labs
    ```

## Configure your work station with the Azure Machine Learning Studio

Though the Azure CLI is ideal for automation, you may want to review the output of the commands you executed. You can use the Azure Machine Learning Studio to check whether resources and assets have been created, and to check whether jobs ran successfully or review why a job failed. 

1. In the Azure portal, navigate to the Azure Machine Learning workspace named `mlw-dp100-labs`.
1. Select the Azure Machine Learning workspace, and in its **Overview** page, select **Launch studio**. Another tab will open in your browser to open the Azure Machine Learning Studio.
1. Within the Azure Machine Learning Studio, navigate to the **Compute** page and verify that the compute instance and cluster you created in the previous section exist. The compute instance should be running, the cluster should be idle and have 0 nodes running.

## Use the Python SDK to train a model

Now that you've verified that the necessary compute has been created, you can use the Python SDK to run a training script. You'll install and use the Python SDK on the compute instance and train the machine learning model on the compute cluster.

1. Select the **Terminal** application for your **compute instance** to launch the terminal.
1. In the terminal, install the Python SDK on the compute instance by running the following commands in the terminal:
    ```
    pip uninstall azure-ai-ml
    pip install azure-ai-ml
    ```
1. Run the following command to clone a Git repository containing a notebook, data, and other files to your workspace:
    ```
    git clone https://github.com/MicrosoftLearning/dp100-explore-workspace.git dp100-explore-workspace
    ``` 
1. When the command has completed, in the **Files** pane, click **&#8635;** to refresh the view and verify that a new **/users/*your-user-name*/dp100-explore-workspace** folder has been created. 
1. Expand the folder to find a notebook, a YAML file which defines the environment, and a folder containing the training script and a dataset. Explore all these files to 
1. Open the **Labs/Run-training-script.ipynb** notebook.
1. Run all cells in the notebook. 

A new job will be created in the Azure Machine Learning workspace. The job tracks the inputs defined in the job configuration, the code used, and the outputs like metrics to evaluate the model.

## Review your job history in the Azure Machine Learning Studio

When you submit a job to the Azure Machine Learning workspace, you can review its status in the Azure Machine Learning Studio.

1. Either select the job URL provided as output in the notebook, or navigate to the **Jobs** page in the Azure Machine Learning Studio.
1. A new experiment is listed named **diabetes-training**. Select the latest job **diabetes-pythonv2-train**.
1. Review the job's **Properties**. Note the job **Status**: 
    - **Queued**: The job is waiting for compute to become available.
    - **Preparing**: The compute cluster is resizing or the environment is being installed on the compute target.
    - **Running**: The training script is being executed. 
    - **Finalizing**: The training script ran and the job is being updated with all final information.
    - **Completed**: The job successfully completed and is terminated.
    - **Failed**: The job failed and is terminated.
1. When the job is completed, you can find the *AUC* and *Accuracy* of the model under **Metrics**. 
1. Under **Outputs + logs**, you'll find:
    - The model pickle file in the folder **outputs**. 
    - The output of the script in **user_logs/std_log.txt**. Output from `print` statements in the script will show here. If there's an error because of a problem with your script, you'll find the error message here too.
1. Under **Code**, you'll find the folder you specified in the job configuration. This folder includes the training script and dataset.

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