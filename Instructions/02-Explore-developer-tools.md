---
lab:
    title: 'Explore developer tools for workspace interaction'
---

# Explore developer tools for workspace interaction

You can use various tools to interact with the Azure Machine Learning workspace. Depending on what task you need to perform and your preference for developer tool, you can choose which tool to use when. This lab is designed as an introduction to the developer tools commonly used for workspace interaction. If you want to learn how to use a specific tool in more depth, there are other labs to explore.

## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free?azure-portal=true) in which you have administrative-level access.

The commonly used developer tools for interacting with the Azure Machine Learning workspace are:

- **Azure CLI** with the Azure Machine Learning extension: This command-line approach is ideal for the automation of infrastructure.
- **Azure Machine Learning studio**: Use the user-friendly UI to explore the workspace and all of its capabilities.
- **Python SDK** for Azure Machine Learning: Use to submit jobs and manage models from a Jupyter notebook, ideal for data scientists.

You'll explore each of these tools for tasks that are commonly done with that tool.

## Provision the infrastructure with the Azure CLI

For a data scientist to train a machine learning model with Azure Machine Learning, you'll need to set up the necessary infrastructure. You can use the Azure CLI with the Azure Machine Learning extension to create an Azure Machine Learning workspace and resources like a compute instance.

To start, open the Azure Cloud Shell, install the Azure Machine Learning extension and clone the Git repo.

1. In a browser, open the Azure portal at `https://portal.azure.com/`, signing in with your Microsoft account.
1. Select the \[>_] (*Cloud Shell*) button at the top of the page to the right of the search box. This opens a Cloud Shell pane at the bottom of the portal.
1. Select **Bash** if asked. The first time you open the cloud shell, you will be asked to choose the type of shell you want to use (*Bash* or *PowerShell*).
1. Check that the correct subscription is specified and that **No storage account required** is selected. Select **Apply**.
1. Remove any ML CLI extensions (both version 1 and 2) to avoid any conflicts with previous versions with this command:
    
    ```azurecli
    az extension remove -n azure-cli-ml
    az extension remove -n ml
    ```

    > Use `SHIFT + INSERT` to paste your copied code into the Cloud Shell.

    > Ignore any (error) messages that say that the extensions were not installed.

1. Install the Azure Machine Learning (v2) extension with the following command:
    
    ```azurecli
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

    <details>  
    <summary><b>Troubleshooting tip</b>: Workspace creation error</summary><br>
    <p>If you receive an error when creating a workspace through the CLI, you need to provision the resource manually:</p>
    <ol>
        <li>In the Azure portal home page, select <b>+ Create a resource</b>.</li>
        <li>Search for <i>machine learning</i> and then select <b>Azure Machine Learning</b>. Select <b>Create</b>.</li>
        <li>Create a new Azure Machine Learning resource with the following settings:
            <ul>
                <li><b>Subscription</b>: <i>Your Azure subscription</i></li>
                <li><b>Resource group</b>: rg-dp100-labs</li>
                <li><b>Workspace name</b>: mlw-dp100-labs</li>
                <li><b>Region</b>: <i>Select the geographical region closest to you</i></li>
                <li><b>Storage account</b>: <i>Note the default new storage account that will be created for your workspace</i></li>
                <li><b>Key vault</b>: <i>Note the default new key vault that will be created for your workspace</i></li>
                <li><b>Application insights</b>: <i>Note the default new application insights resource that will be created for your workspace</i></li>
                <li><b>Container registry</b>: None (<i>one will be created automatically the first time you deploy a model to a container</i>)</li>
            </ul>
        <li>Select <b>Review + create</b> and wait for the workspace and its associated resources to be created - this typically takes around 5 minutes.</li>
    </ol>
    </details>

## Create a compute instance with the Azure CLI

Another important part of the infrastructure needed to train a machine learning model is **compute**. Though you can train models locally, it's more scalable and cost efficient to use cloud compute.

When data scientists are developing a machine learning model in the Azure Machine Learning workspace, they want to use a virtual machine on which they can run Jupyter notebooks. For development, a **compute instance** is an ideal fit.

After creating an Azure Machine Learning workspace, you can also create a compute instance using the Azure CLI.

In this exercise, you'll create a compute instance with the following settings:

- **Compute name**: *Name of compute instance. Has to be unique and fewer than 24 characters.*
- **Virtual machine size**: STANDARD_DS11_V2
- **Compute type** (instance or cluster): ComputeInstance
- **Azure Machine Learning workspace name**: mlw-dp100-labs
- **Resource group**: rg-dp100-labs

1. Use the following command to create a compute instance in your workspace. If the compute instance name contains "XXXX", replace it with random numbers to create a unique name.

    ```azurecli
    az ml compute create --name "ciXXXX" --size STANDARD_DS11_V2 --type ComputeInstance -w mlw-dp100-labs -g rg-dp100-labs
    ```

    If you get an error message that a compute instance with the name already exists, change the name and retry the command.

    <details>  
    <summary><b>Troubleshooting tip</b>: Compute creation error</summary><br>
    <p>If you receive an error when creating a compute instance through the CLI, you need to provision the resource manually:</p>
    <ol>
        <li>In the Azure portal, navigate to the Azure Machine Learning workspace named <b>mlw-dp100-labs</b>.</li>
        <li>Select the Azure Machine Learning workspace, and in its <b>Overview</b> page, select <b>Launch studio</b>. Another tab will open in your browser to open the Azure Machine Learning studio.</li>
        <li>Close any pop-ups that appear in the studio.</li>
        <li>Within the Azure Machine Learning studio, navigate to the <b>Compute</b> page and select <b>+ New</b> under the <b>Compute instances</b> tab.</li>
        <li>Give the compute instance a unique name and then select <b>Standard_DS11_v2</b> as the virtual machine size.</li>
        <li>Select <b>Review + create</b> and then select <b>Create</b>.</li>
    </ol>
    </details>

## Create a compute cluster with the Azure CLI

Though a compute instance is ideal for development, a compute cluster is better suited when we want to train machine learning models. Only when a job is submitted to use the compute cluster, will it resize to more than 0 nodes and run the job. Once the compute cluster is no longer needed, it will automatically resize back to 0 nodes to minimize costs. 

To create a compute cluster, you can use the Azure CLI, similar to creating a compute instance.

You'll create a compute cluster with the following settings:

- **Compute name**: aml-cluster
- **Virtual machine size**: STANDARD_DS11_V2
- **Compute type**: AmlCompute *(Creates a compute cluster)*
- **Maximum instances**: *Maximum number of nodes*
- **Azure Machine Learning workspace name**: mlw-dp100-labs
- **Resource group**: rg-dp100-labs

1. Use the following command to create a compute cluster in your workspace.
    
    ```azurecli
    az ml compute create --name "aml-cluster" --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute -w mlw-dp100-labs -g rg-dp100-labs
    ```

    <details>  
    <summary><b>Troubleshooting tip</b>: Compute creation error</summary><br>
    <p>If you receive an error when creating a compute cluster through the CLI, you need to provision the resource manually:</p>
    <ol>
        <li>In the Azure portal, navigate to the Azure Machine Learning workspace named <b>mlw-dp100-labs</b>.</li>
        <li>Select the Azure Machine Learning workspace, and in its <b>Overview</b> page, select <b>Launch studio</b>. Another tab will open in your browser to open the Azure Machine Learning studio.</li>
        <li>Close any pop-ups that appear in the studio.</li>
        <li>Within the Azure Machine Learning studio, navigate to the <b>Compute</b> page and select <b>+ New</b> under the <b>Compute clusters</b> tab.</li>
        <li>Choose the same region as the one where you created your workspace and then select <b>Standard_DS11_v2</b> as the virtual machine size. Select <b>Next</b></li>
        <li>Give the cluster a unique name and then select <b>Create</b>.</li>
    </ol>
    </details>

## Configure your workstation with the Azure Machine Learning studio

Though the Azure CLI is ideal for automation, you may want to review the output of the commands you executed. You can use the Azure Machine Learning studio to check whether resources and assets have been created, and to check whether jobs ran successfully or review why a job failed. 

1. In the Azure portal, navigate to the Azure Machine Learning workspace named **mlw-dp100-labs**.
1. Select the Azure Machine Learning workspace, and in its **Overview** page, select **Launch studio**. Another tab will open in your browser to open the Azure Machine Learning studio.
1. Close any pop-ups that appear in the studio.
1. Within the Azure Machine Learning studio, navigate to the **Compute** page and verify that the compute instance and cluster you created in the previous section exist. The compute instance should be running, the cluster should be in Succeeded state and have 0 nodes running.

## Use the Python SDK to train a model

Now that you've verified that the necessary compute has been created, you can use the Python SDK to run a training script. You'll install and use the Python SDK on the compute instance and train the machine learning model on the compute cluster.

1. In your **compute instance**, there are a number of options in the **Applications** field. Select the **Terminal** application to launch the terminal (you may need to click the ellipsis to expand the selection).
1. In the terminal, install the Python SDK on the compute instance by running the following commands in the terminal:

    ```
    pip uninstall azure-ai-ml
    pip install azure-ai-ml
    ```

    > Ignore any (error) messages that say that the packages were not installed.

1. Run the following command to clone a Git repository containing notebooks, data, and other files to your workspace:

    ```
    git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git azure-ml-labs
    ```

1. When the command has completed, in the **Files** pane, select **&#8635;** to refresh the view and verify that a new **Users/*your-user-name*/azure-ml-labs** folder has been created.
1. Open the **Labs/02/Run training script.ipynb** notebook.

    > Select **Authenticate** and follow the necessary steps if a notification appears asking you to authenticate.

1. Verify that the notebook uses the **Python 3.10 - AzureML** kernel on the upper right corner of the notebook environment. Each kernel has its own image with its own set of packages pre-installed.
1. Run all cells in the notebook.

A new job will be created in the Azure Machine Learning workspace. The job tracks the inputs defined in the job configuration, the code used, and the outputs like metrics to evaluate the model.

## Review your job history in the Azure Machine Learning studio

When you submit a job to the Azure Machine Learning workspace, you can review its status in the Azure Machine Learning studio.

1. Either select the job URL provided as output in the notebook, or navigate to the **Jobs** page in the Azure Machine Learning studio.
1. A new experiment is listed named **diabetes-training**. Select the latest job **diabetes-pythonv2-train**.
1. Review the job's **Properties**. Note the job **Status**:
    - **Queued**: The job is waiting for compute to become available.
    - **Preparing**: The compute cluster is resizing or the environment is being installed on the compute target.
    - **Running**: The training script is being executed.
    - **Finalizing**: The training script ran and the job is being updated with all final information.
    - **Completed**: The job successfully completed and is terminated.
    - **Failed**: The job failed and is terminated.
1. Under **Outputs + logs**, you'll find the output of the script in **user_logs/std_log.txt**. Outputs from **print** statements in the script will show here. If there's an error because of a problem with your script, you'll find the error message here too.
1. Under **Code**, you'll find the folder you specified in the job configuration. This folder includes the training script and dataset.

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should delete the resources you've created to avoid unnecessary Azure costs.

1. Close the Azure Machine Learning studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-labs** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**. 
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
